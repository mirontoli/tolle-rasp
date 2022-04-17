"""
this script gets office 365 status every 5 minutes
and shows the status on the unicorn phat
Author @mirontoli 2021-02-11
Blog Post: https://chuvash.eu/2021/04/20/monitoring-microsoft-365-using-raspberry-pi-and-m365-cli/
Prerequisites
- Raspberry Pi Zero W with Raspberry Pi OS
- Unicorn Phat and its software
- node and npm (https://hassancorrigan.com/blog/install-nodejs-on-a-raspberry-pi-zero/)
- @pnp/cli-microsoft365 npm package
- login to m365 as sudo (since sudo is required for gpio in the same script)
- admin consent for m365 (PnP Management Shell) in the target tenant


My environment:
OS: Raspbian GNU/Linux 11 (bullseye)
Architecture: armv61
python3 3.9.2
node v12.22.12
npm 6.14.16
@pnp/cli-microsoft365@5.1.0

Steps from scratch:
* Flash SD Card with Raspberry Pi OS Bullseye
* Setup the OS, wifi, enable ssh
* sudo apt update && sudo apt upgrade -y
* curl -sS https://get.pimoroni.com/unicornhat | bash
* wget https://unofficial-builds.nodejs.org/download/release/v12.22.12/node-v12.22.12-linux-armv6l.tar.xz
* tar xvfJ node-v12.22.12-linux-armv6l.tar.xz
* sudo cp -R node-v12.22.12-linux-armv6l/* /usr/local
* rm -rf node-*
* sudo reboot
* sudo npm i -g @pnp/cli-microsoft365
* sudo apt install git -y
* git config --global user.name "Anatoly Mironov"
* git config --global user.email "someone@something.com"
* mkdir Workspace
* cd Workspace
* git clone https://github.com/mirontoli/tolle-rasp.git
* cd tolle-rasp/python_scripts



Run it by hitting
sudo nohup python3 unicorn03_m365.py &

"""
import subprocess
import unicornhat as uh
import time
import urllib, json

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

def make_row(row, colors):
  for y in range(4):
    r, g, b = colors[y]
    uh.set_pixel(row, y, r, g, b)

services = [
  'SharePoint',
  'microsoftteams',
  'Exchange',
  'OneDriveForBusiness',
  'yammer',
  'Viva', # change 2022-01-23 Viva instead of Forms
  'PowerBIcom',
  'Intune'
]

green = [0,255,0]
yellow = [255,255,0]
purple = [128,0,128]
red = [255,0,0]
grey = [192,192,192]
blue = [0,0,255]

color_codes = {
  'ServiceOperational': [green, green, green, green],
  'ServiceRestored': [green, green, green, yellow],
  'Investigating': [purple, purple, purple, purple],
  'FalsePositive': [green, green, green, purple],
  'InformationUnavailable': [grey, grey, grey, grey],
  'ServiceInterruption': [red, red, red, red],
  'ExtendedRecovery': [red, red, red, yellow],
  'ServiceDegradation': [red, red, yellow, green],
  'PIRPublished': [green, green, green, blue],
  'RestoringService': [red, yellow, yellow, green]
}

def show_test():
  make_row(0, color_codes['ServiceOperational'])
  make_row(1, color_codes['ServiceRestored'])
  make_row(2, color_codes['Investigating'])
  make_row(3, color_codes['FalsePositive'])
  uh.show()

def tenant_status():
  #make sure you login with sudo first: sudo m365 login
  result = subprocess.run(['m365', 'tenant serviceannouncement health list', '--output', 'json'], stdout=subprocess.PIPE)
  body = result.stdout.decode('utf-8')
  data = json.loads(body)
  # change 2022-01-23 json format data['value'] -> data
  return { x['id']: x for x in data }

def show(all_services):
  for row in range(8):
    service = services[row]
    status = all_services[service]['Status']
    colors = color_codes[status]
    make_row(row, colors)
  uh.show()

while True:
  #just for debugging, clear while loading new status
  uh.clear()
  uh.show()
  all_services = tenant_status()
  show(all_services)
  time.sleep(5*60)
