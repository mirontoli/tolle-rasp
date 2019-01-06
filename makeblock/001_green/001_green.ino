// Anatoly Mironov @mirontoli
// Show the green light on mBot Ranger

#include <Arduino.h>
#include <Wire.h>
#include <MeAuriga.h>

MeRGBLed rgbled_0(0, 12); 

void setup() {
  rgbled_0.setpin(44);
  rgbled_0.setColor(0,0,255,0); //show the green light on MeAuriga
  rgbled_0.show();
}

void loop() {
}
