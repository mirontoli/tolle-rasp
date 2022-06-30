picomite is an Basic interpreter.

picomite homepage: https://geoffg.net/picomite.html

## RPi Pico Pinout
```bash
curl https://gabmus.org/pico_pinout
```
Here is a somewhat simplified pinout diagram.
The numbering on the right is adjusted to the numbers on my breadboard
```
          ┌─────┃    ┃─────┐
 GP0  | 01│●  ┆ ┗━━━━┛    ●│40 (01) | VBUS
 GP1  | 02│●              ●│39 (02) | VSYS
 GND  | 03│■              ■│38 (03) | GND
 GP2  | 04│●    ╭─╮       ●│37 (04) | 3V3_EN
 GP3  | 05│●    │ │       ●│36 (05) | 3V3(OUT)
 GP4  | 06│●    ╰─╯       ●│35 (06) |          
 GP5  | 07│●              ●│34 (07) | GP28    
 GND  | 08│■              ■│33 (08) | GND  
 GP6  | 09│●   ┌─────┐    ●│32 (09) | GP27 
 GP7  | 10│●   │     │    ●│31 (10) | GP26 
 GP8  | 11│●   │     │    ●│30 (11) | RUN
 GP9  | 12│●   └─────┘    ●│29 (12) | GP22
 GND  | 13│■              ■│28 (13) | GND
 GP10 | 14│●              ●│27 (14) | GP21 
 GP11 | 15│●              ●│26 (15) | GP20
 GP12 | 16│●              ●│25 (16) | GP19 
 GP13 | 17│●              ●│24 (17) | GP18 
 GND  | 18│■              ■│23 (18) | GND
 GP14 | 19│●              ●│22 (19) | GP17
 GP15 | 20│●     ● ■ ●    ●│21 (20) | GP16 
 ```

## commands
* edit - edit current program
* flash save n - save a program in the flash memory
* flash load n - load a program from the flash memory
* flash overwrite n - save a new copy of a program in slot n
* run - run current program
* option autorun n - run automatically on start

## Flash slots

### 1 - 002-flash-led.bas

### 2 - 003-traffic-light.bas

