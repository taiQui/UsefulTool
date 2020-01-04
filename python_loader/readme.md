# Loading screen for terminal



```python
from loading import Loading

loader = Loading()

# Some parameter are available for constructor
""""
	max : int
			range max of loading  0  - max 
	show_percent : boolean
    		show or not the percent of progressing
    adaptative : boolean
    		when you chose size which exceeds max widght of terminal
    		not raise an Exception, adjuste the max size to max we can use
""""

```



## Square Loading 

Simple Loading screen, progress state => self.state

[#####                     ]  20%

```python
from loading import Loading
import time
loader = Loading()
for i in range(100):
    loader.square_loading()
    loader.state += 1
    time.sleep(0.05)
    
""""
	text : str
			text to print before the progression bar
""""
```



## Turning pipe

Simple waiting screen  : Text    | => / => — => \ => | 

```python
from loading import Loading
loader = Loading()
while True
    loader.turning_pipe()
    
""""
	text : str
			text before the turning pipe
	speed : float
			speed of pipe turning animation
""""  
```



## Bar loading

Simple bar moving to the right until reaching right border then moving to the left until reaching left border ...

[**                                    ]

[   **                                 ]

[                                    **]

[                                  **  ]

```python
from loading import Loading
loader = Loading()
while True
    loader.bar_loading()
    
""""
	text : Str
			text to print before animation
	speed : float
			speed of animation
	bar : Str
			body of the bar 
	bar_size : int
			size of the bar
	size : int
			size of the bar's world => [     ] size = 5 ( 5 spaces)
	color_switch : boolean 
					change the color when the bar reach one border
	rainbow : boolean
    			change each piece of bar on each iteration
""""
```



## Up Down Letter

Waiting

wAiting

waIting

waiTing

waitIng

waitiNg

waitinG [...]

```python
from loading import Loading
loader = Loading()
while True
    loader.up_down_waiting()
    
""""
	text : Str
			text to print
	speed : float
			speed of animation
""""
```

## Dot waiting

Waiting 

Waiting .

Waiting ..

Waiting ...

Waiting 

```python
from loading import Loading
loader = Loading()
while True
    loader.dot_waiting()
    
""""
	text : str
			text to Write before animation 
	dot : str
			body of animation ( default : '.')
	dot_max : int
			number of successive time printing 'dot'
	speed :float
			speed of the animation
""""
```

## Mountain waiting

Waiting .

Waiting .:

Waiting .:.

Waiting .:.::

[...]

```python
from loading import Loading
loader = Loading()
while True
    loader.mountain_waiting()
    
""""
	text : str
			text to write before animation
	speed :float
			speed of animation
	max : int
			width max of the mountain
""""
```

