// Anatoly Mironov @mirontoli 2019-01-06
// try rgb led

#include <Arduino.h>
#include <Wire.h>
#include <MeAuriga.h>

MeRGBLed rgbled_0(0, 12);


void setup() {
  rgbled_0.setpin(44);
}

void loop() {
  delay(3000);
  for (int i = 1; i <= 12; i++) {
    rgbled_0.setColor(i,255,0,0);
    rgbled_0.show();
    delay(1000);
  }
  rgbled_0.setColor(0,0,0,0); //turn it off
  rgbled_0.show();
}
