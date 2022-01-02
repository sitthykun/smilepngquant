# SmilePngquant
That is a bridge of pngquant for python3

# Download
### Find package
- https://pkgs.org/download/pngquant
- Ex: https://ubuntu.pkgs.org/20.04/ubuntu-universe-amd64/pngquant_2.12.2-1_amd64.deb.html
- This document will cover

### Or build from github
```commandline
git clone --recursive git://github.com/kornelski/pngquant.git
cd pngquant
make
sudo make install
```

# Find
```commandline
which pngquant
```
$ /usr/local/bin/pngquant

# Check version
```commandline
pngquant --version
```
$ 2.17.0 (September 2021)

# Start to code
```
from smilepngquant.PNGQuant import PNGQuant

# initialize
smile = PNGQuant()

# test a filename
# quality value starts 20 to 100, and it's integer
smile.compress(
  filename  = '/home/thyda/Download/kara.png'
  , quality = 80
)

# verify before use
if smile.isError():
  print(f'Everything is okay, the file name is: {smile.getFilename()}')

else:
  print(f'{smile.getErrorMessage()}')
```

# Options
- dirname: can be None
set coy to a new directory for the new file

- newFilename: can be None
set a new copy name

Both can set any value, or None, or one of them.

Ex 1
```
smile.compress(
  filename      = '/home/thyda/Download/kara.png'
  , quality     = 80
  # move to new directory
  , dirname     = '/home/thyda/Document/'
  , newFilename = 'jojo'
)
```

Ex 2
```
smile.compress(
  filename      = '/home/thyda/Download/kara.png'
  , quality     = 80
  # move to new directory
  , dirname     = '/home/thyda/Document/'
)
```

Ex 3 
```
smile.compress(
  filename      = '/home/thyda/Download/kara.png'
  , quality     = 80
  # move to new directory
  , newFilename = 'jojo'
)
```


It is also available on https://pypi.org/project/smilepngquant \
To Support my work, please donate me via <a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/sitthykun"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a Pizza"><span style="margin-left:5px;font-size:28px !important;">Buy me a Coffee</span></a>


