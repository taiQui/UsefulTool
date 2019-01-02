# UsefullTool

## Dirtool

Program to inspect your computer on linux, you can give as arguments extension '.pdf' , '.txt' or fullname of file

* search 

  * you can search precise file

  * ex : dirtool search test.txt

    ```txt
    You are on Linux machine
    
    Enter your path - default '/home'
    
    executing...
    found test.txt at /home/taiqui/XXXX/a
    
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

