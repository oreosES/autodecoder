# AutoDecoder.py
Tool to automatically decode/decrypt a message for CTFs

# Installation
git clone https://github.com/oreosES/autodecoder.git

# Dependencies
Python3 pyperclip and colorama libraries. To install them using pip3:

pip3 install pyperclip colorama

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

# Example

echo -n "TEST" | base64 | base64
VkVWVFZBPT0K

python3 autodecoder.py --message VkVWVFZBPT0K --levels 2
- base64 > base64 > TEST
- base64 > rot13 > IRIGIN==
- base64 > rot47 > 't'%'pll
- rot13 > base64 > #	!m
- rot13 > rot13 > VkVWVFZBPT0K
- rot13 > rot47 > xIxyx$|~rv_)
- rot47 > rot13 > '<'('h+d!%_m
- rot47 > rot47 > VkVWVFZBPT0K

# Contact
https://www.twitter.com/oreos_es
