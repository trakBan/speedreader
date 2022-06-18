# speedreader

https://user-images.githubusercontent.com/81049050/174282132-b56044ec-f3af-4001-8702-b4231156420f.mp4

# installation

## For UNIX based systems (linux, macOS)
```
# Root is only required for the last line
git clone https://github.com/trakBan/speedreader.git

cd speedreader
chmod +x speedreader
sudo python setup.py install
```
### One line
```
git clone https://github.com/trakBan/speedreader.git && cd speedreader && chmod +x speedreader && sudo python setup.py install
```

# Usage

```
--wpm | -w , usage: -w {number}, WPM - words per minute
--help | -h , usage -h, this will print what each argument does
```

# Config file
You can change colors, default WPM and other things in ```config.py```. documentation is contained inside the config file in the form of the comments.
