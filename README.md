# xor_crypt
python-script to crypt files

## About
Crypt your super secret files super sneaky with this script. It calculates a key via xor from your super secret file and a dummy one. Everybody who has this key and one of your two files can generate the other file. This is a slightly enhanced version from youtubechannel [Algorithmen verstehen](https://www.youtube.com/c/Algorithmenverstehen).

## Enhancements
* commandline-interface for easy use in your terminal
* automatic filetype recovery for supported filetypes (so you dont need to know what type of file is hidden)
  * .7z
  * .aif
  * .bmp
  * .bz2
  * .class
  * .deb
  * .dmg
  * .exe
  * .flac
  * .gif
  * .ico
  * .jpg
  * .midi / .mid
  * .mkv / .mka / .mks / .mk3d / .webm
  * .mp3
  * .mp4
  * .nes
  * .ogg
  * .pdf
  * .png
  * .ps
  * .psd
  * .rar
  * .rtf
  * .sqlite
  * .tar.gz
  * .tif
  * .wma / .asf / .wmv
  * .xml
  * .zip
  * .z
  * .zlib

## How to use
### crypt 
```
main.py --crypt <path_to_public_file> <path_to_private_file> <destination_path_key>
```

### decrypt 
```
main.py --decrypt <path_to_public_file> <path_to_key_file> <destination_path_private_file>
```

### decrypt (with filetype recovery)
```
main.py --decrypt2 <path_to_public_file> <path_to_key_file>
```

## Note
* Keep in mind to use files with nearly the same size. A 25gb large image is kinda sus
* the filetype recovery feature is experimental (it might be dont work is some cases)
