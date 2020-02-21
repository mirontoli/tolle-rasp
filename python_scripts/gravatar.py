#!/usr/bin/env python3
"""
 2020-01-04
 show an avatar from the Gravatar API
 by creating a MD5 hash from an email address and providing size 8px
 to fit it into the sense hat led monitor
 http://en.gravatar.com/site/implement/images/
 https://pythonhosted.org/sense-hat/api/#load_image
 __author__ = "Anatoly Mironov @mirontoli"
 
"""

import urllib.request
from sense_hat import SenseHat
import time
import hashlib

#set up avatars directory
from pathlib import Path
Path("avatars").mkdir(exist_ok=True)

# set up sense
sense = SenseHat()
sense.set_rotation(180)
sense.clear()

email = b'donald.duck@gmail.com'.lower()

hash_obj = hashlib.md5(email)
hash = hash_obj.hexdigest()
print(hash)

url = f'https://www.gravatar.com/avatar/{hash}?s=8'
print(url)

filepath = f'avatars/{hash}.jpg'
urllib.request.urlretrieve(url, filepath)

sense.load_image(filepath)
time.sleep(10)
sense.clear()