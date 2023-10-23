# sprucepy
[![Tests](https://github.com/Hunter87ff/sprucepy/actions/workflows/python-application.yml/badge.svg)](https://github.com/Hunter87ff/sprucepy/actions/workflows/python-application.yml)
![Language](https://img.shields.io/badge/lang-Python%203.5|3.8|3.10-blue)
![API Version](https://img.shields.io/badge/Version-1.0.0-violet)

## Installing
To install the library you can just run the following command:
```sh
# Linux/macOS
python3 -m pip install -U sprucepy

# Windows
py -3 -m pip install -U sprucepy
```
To install the development version, do the following:
```sh
$ git clone https://github.com/hunter87ff/sprucepy
$ cd sprucepy
```
## Quich Example
```py
from sprucepy import Spruce
while True:
	msg = str(input("You : "))
	print("Spruce : " + Spruce().ask(msg))
```
