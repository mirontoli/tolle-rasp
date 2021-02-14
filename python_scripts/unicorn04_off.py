# it switches off the unicorn phat
# sudo python3 unicorn04_off.py
print('attempting to switch off the unicorn phat lights')
import unicornhat as uh
uh.set_layout(uh.PHAT)
uh.clear()
uh.show()

