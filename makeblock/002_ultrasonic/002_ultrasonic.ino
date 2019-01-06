// Anatoly Mironov @mirontoli 2019-01-06
// Trying out ultrasonic distance

#include <Arduino.h>
#include <Wire.h>
#include <MeAuriga.h>

MeUltrasonicSensor ultrasonic_10(10);
float ultrasonicDistance = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  ultrasonicDistance = ultrasonic_10.distanceCm();
  Serial.println(ultrasonicDistance);
  delay(1000);
}
