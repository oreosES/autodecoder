from utils.decoder import Decoder
from itertools import product
from colorama import Fore
import argparse

def banner():
    print(Fore.WHITE)
    print("\n\
                          (                                     \n\
   (             (        )\ )                  (               \n\
   )\       (    )\ )    (()/(     (            )\ )   (   (    \n\
((((_)(    ))\  (()/(  (  /(_))   ))\  (   (   (()/(  ))\  )(   \n\
 )\ _ )\  /((_)  ((_)) )\(_))_   /((_) )\  )\   ((_))/((_)(()\  \n\
 (_)_\(_)(_))(   _| | ((_)|   \ (_))  ((_)((_)  _| |(_))   ((_) \n\
  / _ \  | || |/ _` |/ _ \| |) |/ -_)/ _|/ _ \/ _` |/ -_) | '_| \n\
 /_/ \_\  \_,_|\__,_|\___/|___/ \___|\__|\___/\__,_|\___| |_|   \n\n\
                    Author: oreos | Twitter: @oreos_ES\n\n")

def decodefunc(message, key, levels, pattern, show_all):
    decoder = Decoder()
    decoders = [ 
        "base16",
        "base32",
        "base64",
        "base85",
        "morse",
        "rot13",
        "rot47",
        "vigenere"
    ]
    combdecs = list(product(decoders, repeat=levels))
    for arraydecs in combdecs:
        translated = message
        flow = ""
        for dec in arraydecs:
            translated = decoder.decode(dec, translated, key)
            if translated is None:
                if show_all is not None and show_all:
                    print(Fore.RED+" > ".join(arraydecs))
                break
        if translated is not None:
            if pattern is None or (pattern and pattern in translated):
                print(Fore.WHITE+" > ".join(arraydecs)+": "+Fore.BLUE+translated)

def main():
    banner()

    parser = argparse.ArgumentParser(description='AutoDecoder.py')
    parser.add_argument("-l", "--levels", type=int, help='Number of decoding levels [1-6], default = 2', default=2)
    parser.add_argument("-k", "--key", type=str, help='Key used to decode')
    parser.add_argument("-s", "--show_all", help='Show chains with errors during decoding', action='store_true')
    parser.add_argument("-p", "--pattern", type=str, help='Search pattern in decoded string')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-m', '--message', help='Message to decode', required=True)
    args = parser.parse_args()
    
    decodefunc(args.message, args.key, args.levels, args.pattern, args.show_all)

if __name__== "__main__":
    main()
