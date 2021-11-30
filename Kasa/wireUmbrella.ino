#include <ESP32Servo.h>

Servo servo1; // create four servo objects 
int servo1Pin = 26;

// Published values for SG90 servos; adjust if needed
int minUs = 500;
int maxUs = 2400;

int pos = 0;      // position in degrees

void setup() {
  servo1.setPeriodHertz(50);      // Standard 50hz servo
  servo1.attach(servo1Pin, minUs, maxUs);
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // sweep from 0 degrees to 180 degrees
    // in steps of 1 degree
    servo1.write(pos);
    delay(2);             // waits 20ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // sweep from 180 degrees to 0 degrees
    servo1.write(pos);
    delay(2);
  }
}
