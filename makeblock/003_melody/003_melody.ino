// Anatoly Mironov @mirontoli 2019-01-06
// Play the melody Kukamipe kukasi, Chuvash folk song

#include <Arduino.h>
#include <Wire.h>
#include <MeAuriga.h>

MeBuzzer buzzer;
const int pace = 500;
const int tone_A3 = 220;
const int tone_B3 = 247;
const int tone_C4 = 262;
const int tone_D4 = 294;
const int tone_E4 = 330;

void setup() {
  buzzer.setpin(45);
  delay(5000); //delay otherwise it will play the first phrase twice
  play();
}

void loop() {
  
  delay(5000);
}

void play() {
  playRepeatedTones(tone_A3, pace, 3);
  playRepeatedTones(tone_C4, pace, 1);
  playRepeatedTones(tone_A3, pace, 2);
  playRepeatedTones(tone_A3, pace*2, 1);

  for (int i = 0; i < 2; i++) {
    playRepeatedTones(tone_E4, pace, 2);
    playRepeatedTones(tone_C4, pace, 1);
    playRepeatedTones(tone_E4, pace, 1);
    playRepeatedTones(tone_D4, pace*2, 2);   
  }

  playRepeatedTones(tone_C4, pace, 2);
  playRepeatedTones(tone_B3, pace, 2);
  playRepeatedTones(tone_A3, pace*2, 2);
}

void playRepeatedTones(int tone, int pace, int times) {
  for(int i = 0; i < times; i++) {
    buzzer.tone(tone,pace);
    delay(20);
  }
}
