// Anatoly Mironov @mirontoli
// If ultrasonic detects something, scream and light

#include <Arduino.h>
#include <Wire.h>
#include <MeAuriga.h>

MeUltrasonicSensor ultrasonic_10(10);
MeRGBLed rgbled_0(0, 12);
MeBuzzer buzzer;

void setup() {
  rgbled_0.setpin(44);
  buzzer.setpin(45);
}

void loop() {
  if(ultrasonic_10.distanceCm() < 100){
      rgbled_0.setColor(0,255, 0, 0 );
      rgbled_0.show();
      buzzer.tone(262,0.25*1000);
      delay(20);

  }else{
      rgbled_0.setColor(0,0,0,0);
      rgbled_0.show();

  }
  delay(1000);
}
