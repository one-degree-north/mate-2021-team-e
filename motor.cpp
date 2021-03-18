Servo motL;
Servo motR;
Servo motU;
Servo serL;
Servo serR;
void setup() {
  Serial.begin(9600);
  serL.attach(5);
  serR.attach(6);
  motL.attach(7);
  motR.attach(8);
  motU.attach(9);
  serL.write(0);
  serR.write(0);
  motL.writeMicroseconds(1500);
  motR.writeMicroseconds(1500);
  motU.writeMicroseconds(1500);
  delayMicroseconds(7000);
  while (!Serial);
}
void loop() {
  if(Serial.available()) {
  int motor = Serial.parseInt();

    if(motor == 1) {
      if(Serial.available()) {
        delay(500);
        int fast = Serial.parseInt();
        motL.writeMicroseconds(1500 + fast);
        Serial.print("Left motor turning at ");
        Serial.println(fast);
      }
    }
    else if(motor == 2) {
      if(Serial.available()) {
        delay(500);
        int fast = Serial.parseInt();
        motR.writeMicroseconds(1500 + fast);
        Serial.print("Right motor turning at ");
        Serial.println(fast);
      }  
    }
    else if(motor == 3) {
      if(Serial.available()) {
        delay(500);
        int fast = Serial.parseInt();
        motU.writeMicroseconds(1500 + fast);
        Serial.print("Up motor turning at ");
        Serial.println(fast);
      }
    }
    else if(motor == 4) {
      if(Serial.available()) {
        delay(500);
        int deg = Serial.parseInt();
        serL.write(deg);
        Serial.print("Left servo at ");
        Serial.print(deg);
        Serial.println(" degrees.");
      }
    }
    else if(motor == 5) {
      if(Serial.available()) {
        delay(500);
        int deg = Serial.parseInt();
        serR.write(deg);
        Serial.print("Right servo at ");
        Serial.print(deg);
        Serial.println(" degrees.");
      }
    }
  }
}
