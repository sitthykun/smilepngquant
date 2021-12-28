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
from SmilePNGQuant import SmilePNGQuant

# initialize
smile = SmilePNGQuant()

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

It is available on **PyPi** store via https://pypi.org/project/SmilePngquant/ \
To Support my work, please donate me via <a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/sitthykun"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a Pizza"><span style="margin-left:5px;font-size:28px !important;">Buy me a Coffee</span></a>


