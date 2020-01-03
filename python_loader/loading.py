
#!/bin/env python3
# coding:utf-8
import time,os,random
"""
    Author : taiQui
    github : https://github.com/taiQui/
"""
class Loading:
    def __init__(self,max=100,show_percent=False,load_color="default"):
        class Color:
            red = '\033[31m'
            green = '\033[32m'
            brown = '\033[33m'
            blue = '\033[34m'
            purple = '\033[35m'
            black = '\033[30m'
            default = '\033[0m'
        # BASIC
        self.AllColor = [Color.red,Color.green,Color.brown,Color.blue,Color.purple,Color.black]
        self.color = Color.default
        self.state = 0
        self.range_max = max
        self.show_percent = show_percent
        # Turning pipe
        self.current = "|"
        # Bar
        self.bar = []
        self.bar_direction = "right"
        self.bar_color = Color.default
        # Up down letter
        self.text = ""
        self.udl_direction = "right"
    def square_loading(self,text=""):
        """
            text : text printed before loading  | ex :   text  [■■■■■   ]
        """
        self.check_range()
        space = self.range_max - self.state
        if self.show_percent:
            print(text+ "["+"■"*self.state+" "*space+"]",end="\r")
        else:
            print(text+" ["+"■"*self.state+" "*space+"]  "+str(int((self.state/self.range_max)*100))+"%",end="\r")

    def turning_pipe(self,text="Wainting ",speed=0.2):
        """
            speed : smaller the number is, faster the pipe turn
        """
        print(text+self.current,end="\r")
        time.sleep(speed)
        self.next_pipe()

    def next_pipe(self):
        if self.current == "|":
            self.current = "/"
        elif self.current == "/":
            self.current = "—"
        elif self.current == "—":
            self.current = "\\"
        elif self.current == "\\":
            self.current = "|"

    def bar_loading(self,text="",bar="*",bar_size=5,size=-1,speed=0.1,color_switch=False,rainbow=False):
        """
            text : text to print before the loading screen
            bar  : bar body
            speed : speed of the animation, less than the number is, faster the animation is
            color_switch : change the bar color when it reach one border
            raibow : change the color or every piece of his body in each iteration
            size : length of bar world  => [      size      ]
        """
        l,c = self.getSizeScreen()
        if size == -1:
            size = int(c*0.9)
        else:
            if size < 1 and size > c:
                raise Exception("Size of map > size of screen")
        if bar_size >= c :
            raise Exception("Size of bar > size of screen")
        if len(self.bar)==0:
            for i in range(bar_size):
                self.bar.append(bar)
            for i in range(size-bar_size):
                self.bar.append(" ")
            self.state = bar_size
        if self.state == size and self.bar_direction == "right":
            self.bar_direction = "left"
            if color_switch:
                self.bar_color = self.AllColor[random.randrange(0,len(self.AllColor))]
            self.state = self.state - bar_size
        elif self.state == 0 and self.bar_direction == "left":
            self.bar_direction = "right"
            if color_switch:
                self.bar_color = self.AllColor[random.randrange(0,len(self.AllColor))]
            self.state = self.state + bar_size
        if self.bar_direction == "right":
            for i in range(size-1,1,-1):
                self.bar[i] = self.bar[i-1]
            self.bar[self.state-bar_size] = " "
            self.state += 1
        elif self.bar_direction == "left":
            for i in range(0,size-2):
                self.bar[i] = self.bar[i+1]
            self.state -= 1
            self.bar[self.state+bar_size] = " "
        toPrint = ""
        for i in self.bar:
            if rainbow:
                if i == bar:
                    toPrint += self.AllColor[random.randrange(0,len(self.AllColor))]+i+self.color
                else:
                    toPrint += " "
            else:
                if i == bar:
                    toPrint += self.bar_color+i
                elif i == " ":
                    toPrint += i+self.color
        print(text+" ["+toPrint+"]",end="\r")
        time.sleep(speed)


    def up_down_waiting(self,text="waiting screen",speed=0.1):
        if self.text == "":
            self.text = text.lower()
            self.state = 0
        tmp = []
        for i in range(len(text)):
            if i == self.state:
                tmp.append(self.text[i].upper())
            else:
                tmp.append(self.text[i])
        if self.udl_direction == "right":
            if self.state != 0:
                tmp[self.state-1] = tmp[self.state-1].lower()
            self.state += 1
        elif self.udl_direction == "left":
            if self.state < len(self.text)-1:
                tmp[self.state+1] = tmp[self.state+1].lower()
            self.state -= 1
        if self.state > len(self.text):
            self.udl_direction = "left"
            self.state-=1
        elif self.state == -1:
            self.udl_direction = "right"
            self.state = 0
        self.text = "".join(tmp)
        print(self.text,end="\r")
        time.sleep(speed)
    def check_range(self):
        if self.state > self.range_max:
            raise Exception("Range max reached")

    def getSizeScreen(self):
        ts = os.get_terminal_size()
        return ts.lines,ts.columns

if __name__ == "__main__":
    a = Loading()
    while True:
        a.bar_loading(speed=0.05)
