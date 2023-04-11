Bed leveling Ender 3 by imaprinterwholikestoprint
; Inspired by and remixed from elproducts CHEP FilamentFriday.com and Jacqueswww
; Version 2.0 Reduced cycles to twice around

G90 ; Use absolute positioning
G28 ; Home all axes
M0 ; Stop print

G1 Z5 ; Lift Z axis
G1 X29 Y29 F5000; Move to Position 1
G1 Z0 ; Lower Z axis
M0 ; Stop print
G1 Z5 ; Lift Z axis
G1 X200 Y29 F5000; Move to Position 2
G1 Z0 ; Lower Z axis
M0 ; Stop print
G1 Z5 ; Lift Z axis
G1 X200 Y199 F5000; Move to Position 3
G1 Z0 ; Lower Z axis
M0 ; Stop print
G1 Z5 ; Lift Z axis
G1 X29 Y199 F5000; Move to Position 4
G1 Z0 ; Lower Z axis
M0 ; Stop print

G1 Z5 ; Lift Z axis
G1 X29 Y29 F5000; Move to Position 1
G1 Z0 ; Lower Z axis
M0 ; Stop print
G1 Z5 ; Lift Z axis
G1 X200 Y29 F5000; Move to Position 2
G1 Z0 ; Lower Z axis
M0 ; Stop print
G1 Z5 ; Lift Z axis
G1 X200 Y199 F5000; Move to Position 3
G1 Z0 ; Lower Z axis
M0 ; Stop print
G1 Z5 ; Lift Z axis
G1 X29 Y199 F5000; Move to Position 4
G1 Z0 ; Lower Z axis
M0 ; Stop print


G28 ; Home all axes
G1 Z5 ; Lift Z axis
M84 ; Disable motors



