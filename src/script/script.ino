// main.ino

#include <Servo.h>
#include "Ultrasonic.h"


#define MOTOR_PIN A0
#define TRIGGER_PIN A1
#define ECHO_PIN A2

Servo servo_motor;
Ultrasonic sonar_sensor(TRIGGER_PIN, ECHO_PIN);

int distance;
int speed = 1;

void setup() {
  
  servo_motor.attach(MOTOR_PIN);
  servo_motor.write(0);
  
  
  Serial.begin(9600);
}

void loop() {

   if (Serial.available() > 0) {
    speed = Serial.parseInt(); 
   }
  
  for(int i = 15; i <= 165; i+=speed) {
    
    servo_motor.write(i);
    
    
   if (Serial.available() > 0) {
    speed = Serial.parseInt(); 
   }

   
    distance = sonar_sensor.get_distance();

    delay(30);
    Serial.print(i);
    Serial.print(",");
    if(distance == 0) {Serial.print(250.); continue;}
    Serial.print(distance);
    Serial.print(".");

  }
  
  
  for(int i = 165; i >= 15; i-=speed) {
    servo_motor.write(i);
    
   if (Serial.available() > 0) {
    speed = Serial.parseInt(); 
   }
   
    distance = sonar_sensor.get_distance();
    
    delay(30);
    Serial.print(i);
    Serial.print(",");
    if(distance == 0) {Serial.print(250.); continue;}
    Serial.print(distance);
    Serial.print(".");

  }
  
  
  
  
}
