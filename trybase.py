import argparse
from sys import exit
import base64
import base58
import base62
parser = argparse.ArgumentParser()
parser.add_argument('-f','--file',help='File to test base',type=str)
parser.add_argument('-s','--string',help='String to test base',type=str)
parser.add_argument('-e','--encode',help='Encode string, give base number',type=str)
parser.add_argument('-v','--verbose',help='More verbose',action="store_true")
arg = parser.parse_args()

verbose = False

def decod(text):
    #Try if base32
    try:
        a = base64.b32decode(text)
        print("[+] Seems to be base 32")
        print(a)
    except:
        print("[-] Base 32 tested")
    #try if base64
    try:
        a = base64.b64decode(text)
        print("[+] Seems to be base 64")
        print(a)
    except:
        print("[-] Base 64 tested")
    #Try if base85 or ascii 85
    try:
        a = base64.a85decode(text)
        print("[+] Seems to be Base85")
        print(a)
    except:
        print("[-] Base 85 tested")
    #Try if base58
    try:
        a = base58.b58decode(text)
        print("[+] Seems to be base 58")
        print(a)
    except:
        print("[-] Base 58 tested")
    #Try if base62
    try:
        a = base62.encode(int(text))
        print("[+] Seems to be base 62")
        print(a)
    except:
        print("[-] Base 62 tested")
    #Try if base16
    try:
        a = bytearray.fromhex(text).decode()
        print("[+] Seems to be base 16")
        print(a)
    except:
        print("[-] Hex tested")
if __name__ == '__main__':
    if arg.verbose != None and arg.verbose:
        verbose = True
    text = ""
    if arg.file != None :
        file = open(arg.file,'r')
        text = file.read()
        file.close()
    elif arg.string != None:
        text = arg.string
    else:
        text = input()
    if arg.encode != None:
        if arg.encode == "64":
            if verbose:
                print("[+] Encoding to base64")
            print(base64.b64encode(text.encode('ascii')).decode('utf-8'))
        elif arg.encode == "32":
            if verbose:
                print("[+] Encoding to base32")
            print(base64.b32encode(text.encode('ascii')).decode('utf-8'))
        elif arg.encode == "85":
            if verbose:
                print("[+] Encoding to base85")
            print(base64.a85encode(text.encode('ascii')).decode('utf-8'))
        elif arg.encode == "58":
            if verbose:
                print("[+] Encoding to base58")
            print(base58.b58encode(text.encode('ascii')).decode('utf-8'))
        elif arg.encode == "62":
            if verbose:
                print("[+] Encoding to base62")
            print(base62.decode(text))
        elif arg.encode == "16":
            if verbose:
                print("[+] Encoding to base16")
            print(hex(int.from_bytes(text.encode(),'big')))
        else:
            print("[-] Error in arguments")
            exit()
    else:
        decod(text)
