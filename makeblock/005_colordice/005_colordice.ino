// Anatoly Mironov @mirontoli 2019-01-06
// Color dice like in babblarna game

#include <Arduino.h>
#include <Wire.h>
#include <MeAuriga.h>

MeRGBLed rgbled_0(0, 12);
MeBuzzer buzzer;

void setup() {
  buzzer.setpin(45);
  rgbled_0.setpin(44);
  rgbled_0.setColor(0,0,0,0); //turn it off
  rgbled_0.show();
  delay(3000);
  for (int i = 0; i < 3; i++) {
    buzzer.tone(700,500);
    delay(100);
  }
  showRandomColor();
}

void loop() {
}

void showRandomColor() {
  int dice_side = random(5);
  if (dice_side == 0) {
    rgbled_0.setColor(0,255,0,0); //red - bobbo
  } else if (dice_side == 1) {
    rgbled_0.setColor(0,0,255,0); //green - dadda
  } else if (dice_side == 2) {
    rgbled_0.setColor(0,0,255,255); //yellow - bibbi
  } else if (dice_side == 3) {
    rgbled_0.setColor(0,255,255,0); //pink - diddi
  } else if (dice_side == 4) {
    rgbled_0.setColor(0,255,255,255); //white - don't remember
  }
  rgbled_0.show();
}
