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
  'Forms',
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
  result = subprocess.run(['m365', 'tenant status list', '--output', 'json'], stdout=subprocess.PIPE)
  body = result.stdout.decode('utf-8')
  data = json.loads(body)
  return { x['Id']: x for x in data['value'] }

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
