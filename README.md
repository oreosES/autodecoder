# AutoDecoder.py
Tool to automatically decode/decrypt a message for CTFs

# Installation
git clone https://github.com/oreosES/autodecoder.git

# Usage
python3 audodecoder.py -h

usage: audodecoder.py [-h] [-l LEVELS] [-k KEY] [-p PATTERN] -m MESSAGE

AutoDecoder.py

optional arguments:
  -h, --help            show this help message and exit
  -l LEVELS, --levels LEVELS
                        Number of decoding levels [1-6], default = 2
  -k KEY, --key KEY     Key used to decode
  -p PATTERN, --pattern PATTERN
                        Search pattern in decoded string

required named arguments:
  -m MESSAGE, --message MESSAGE
                        Message to decode

# Contact
https://www.twitter.com/oreos_es
