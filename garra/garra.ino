// --- Servo
#include <Servo.h>
Servo servo1;
int servo1Pin = 6;

int minesq = 40;
int maxesq = 135;

int maxdir = 140;
int mindir = 0;

int maxi = 180;
int mini = 0;



// --- Inicialização ---
void setup() {
  servo1.attach(servo1Pin);
  Serial.begin(9600);
  }

// --- Funçâo Principal ---
void loop() {
  for (int i=mini;i<maxi;i++) {
    servo1.write(i);
    delay(20);
    }
    delay(1000);
  for (int i=maxi;i>mini;i--) {
  servo1.write(i);
  Serial.println(i);
  delay(20);
  }
  delay(1000);
}
