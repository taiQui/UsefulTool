# UsefulTool

## BF

Script to automate threading with custom bruteforce

```python
from bf import BF
# use case 1 : gobuster like
def brute(directory):
    r = requests.get(f"https://something/{directory}")
    if r.status_code == 200:
        print(f"[+] {directory} is present")
BF(brute,item1=directory_wordlist.txt)

#use case 2 : login brute force
def brute(username,password):
    r = requests.post("http://something",data={"username":username,"password":password})
    if good_one:
        print("[+] Creds found")
BF(brute,item1=username.lst,item2=password.lst)

#use case 3 : bruteforce hash
def brute(rockyou_item,hashfound):
    hash = # hashing rockyou_item with some custom hashing method
    if hash == hashfound:
        print("[+] found ")
        return True   #<=== return True will stop All thread because there is only one posibilities here
BF(brute,item1=rockyou.txt,item2=file_with_your_hash)
```









## Dirtool

Program to inspect your computer on linux, you can give as arguments extension '.pdf' , '.txt' or fullname of file

* search

  * you can search precise file

  * ex : dirtool search test.txt

    ```txt
    You are on Linux machine

    Enter your path - default '/home'

    executing...
    found test.txt at /home/XXXX/a

    we found 1 element for test.txt

    ```

* count

  * you can count number of file with precise extension, or some word in file's name and print if you want their path

  * ex : dirtool count .txt [yes]

    ```txt
    You are on Linux machine

    Enter your path - default '/home'

    executing...
    We found 401 times '.txt'
    ```

    dirtool count yo yes

    ```
    You are on Linux machine

    Enter your path - default '/home'

    executing...
     at /home/xxxx/testyo

    We found 1 times 'yo'

    ```
  * inspect

    * You can search any strings in any file with given path.

    * ex : dirtool inspect hello

    ```
    You are on Linux machine

    Enter your path - default '/home'
    .
    executing...
    Begin inpection of 'aaaaaaaaaaaa'
    regex : False
    PATH : .
        √ String : 'aaaaaaaaaaaa ' was found in :ch2.txt located in :/hello/test

    ```

    * ex : dirtool inspect "[0-9a-zA-Z]" yes

    ```
    You are on Linux machine

    Enter your path - default '/home'
    .
    executing...
    Begin inpection of '[0-9a-zA-Z]'
    regex : True
    PATH : .
        √ String : 'aaaaaaaaaaaa ' was found in :ch2.txt located in :/hello/test

    ```




## GEN

usefull tool to buffer overflow

program to generate string which element are different 4 by 4

option :

* -f : force programming format ( buf += ..... )
* -c : copy generated string in copy buffer

```python
#gen 10
Aa0Aa1Aa2A
#gen 10 0Aa1
2
#gen 10 -f
gen = ""
gen += "Aa0Aa1Aa2A"
```

## LSB
Algorithm to find some LSB stegano in picture
* find
just generate 8 images with 1 to 8 lsb
* extract
extract value with lsb bit
* decode
 LSB decode with key ( -k )
* filter
 generate image with specified filter ( blue, red, green )
* option
  * -rgb r: g: b: s

    r bit in red channel: g bits in green channel : b bits in blue channel : jump s pixel

  * -l
  how many line apply LSB
  * -k
  if LSB encoded

## PIT
Algorithm to decode PIT stegano technique

## PVD
Algorithm to decode PVD stegano technique

## TRYBASE
Use to test if arguments is encoded in some base in range [ 16 32 58 62 64 85]
Possibility to encode in base too 
