'flash 1 led
10 Print "Hello World"
20 SetPin GP21, DOUT
30 Pin(GP21) = 1
40 Pause 300
50 Pin(GP21) = 0
50 Pause 300
60 GoTo 30
