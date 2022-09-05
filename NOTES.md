# [photosdup](https://github.com/peter-sk/photosdup)

* Papelera tiene que estar vacía, por error en tags si hay en papelera duplicados.
* extensions like *.gif need a patch

run `osascript -e 'tell application "Photos"' -e 'set currentTimeInSeconds to (time of (current date))' -e 'end tell'` 
and authorize in Settings

````shell
pip3 install photosdup
brew install python-tk@3.10
python -m photosdup /Users/j5pu/Pictures/js5puer.photoslibrary --tag  # to compute from existing thumbnails
python -m photosdup Pictures/Photos.photoslibrary --no-thumbs --tag  # to compute from originals
````

# Test

```shell
osxphotos import --walk pictures/
./idupes
````
