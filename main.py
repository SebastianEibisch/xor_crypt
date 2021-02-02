import os
import filetypes
import sys, getopt


def keygen(orig_path, enc_path, key_path):
    equalize(orig_path, enc_path)
    original = open(orig_path, 'rb').read()
    encrypted = open(enc_path, 'rb').read()
    key = bytes(a ^ b for (a, b) in zip(original, encrypted))
    with open(key_path + 'key', 'wb') as key_file:
        key_file.write(key)


def decrypt(enc_path, key_path, dec_path):
    encrypted = open(enc_path, 'rb').read()
    key = open(key_path, 'rb').read()
    decrypted = bytes(a ^ b for (a, b) in zip(encrypted, key))
    with open(dec_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


def decrypt2(enc_path, key_path):
    encrypted = open(enc_path, 'rb').read()
    key = open(key_path, 'rb').read()
    decrypted = bytes(a ^ b for (a, b) in zip(encrypted, key))

    for filetype in filetypes.filetypes:
        byte_length = len(filetype[1])
        if decrypted[:byte_length] == filetype[1]:  # TODO offset
            with open(enc_path + '_encrypted.' + filetype[0], 'wb') as decrypted_file:
                decrypted_file.write(decrypted)


def equalize(path1, path2):
    file1 = open(path1, 'rb').read()
    file2 = open(path2, 'rb').read()
    len1 = len(file1)
    len2 = len(file2)

    if len1 < len2:
        file1 += os.urandom(len2 - len1)
        with open(path1, 'wb') as file:
            file.write(file1)
    if len2 < len1:
        file2 += os.urandom(len1 - len2)
        with open(path2, 'wb') as file:
            file.write(file2)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'cdx', ["crypt", "decrypt", "decrypt2"])
    except getopt.GetoptError:
        print('invalid flag')
        sys.exit()

    option = opts.pop()[0]

    if option in ('-c', '--crypt'):
        if len(args) != 3:
            print('function awaits 3 parameters')
            sys.exit()
        keygen(args[0], args[1], args[2])

    if option in ('-d', '--decrypt'):
        if len(args) != 3:
            print('function awaits 3 parameters')
            sys.exit()
        decrypt(args[0], args[1], args[2])

    if option in ('-x', '--decrypt2'):
        if len(args) != 2:
            print('function awaits 2 parameters')
            sys.exit()
        decrypt2(args[0], args[1])


if __name__ == '__main__':
    main(sys.argv[1:])

    #keygen('test/public_image.jpg', 'test/secret_image.jpg', 'test/')
    #decrypt('test/yolo/public_image.jpg', 'test/yolo/key', 'test/yolo/secret.jpg')
    #decrypt2('test/yolo/public_image.jpg', 'test/yolo/key')
