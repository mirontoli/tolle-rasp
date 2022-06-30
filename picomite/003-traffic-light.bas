'traffic light
10 SetPin GP2, DOUT 'red
20 SetPin GP3, DOUT 'yellow
30 SetPin GP4, DOUT 'green
40 Pin(GP2) = 1
50 Pause 1000
60 Pin(GP2) = 0
70 Pin(GP3) = 1
80 Pause 1000
90 Pin(GP3) = 0
100 Pin(GP4) = 1
110 Pause 1000
120 Pin(GP4) = 0
130 Pin(GP3) = 1
140 Pause 1000
150 Pin(GP3) = 0
160 GoTo 40
