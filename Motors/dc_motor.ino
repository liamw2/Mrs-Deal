//DC Motor Driver
/* analogWrite(PIN_ENA, speed);
 * analogWrite(PIN_ENB, speed);
 * speed is 0-255
 * IN1  IN2
 * H    L   clockwise
 * L    H   counter
 * H    H   stop
 * L    L   stop
 * digitalWrite(IN1, HIGH);
 * digitalWrite(IN2, LOW); clockwise
 * 
 */

int mpin1 = 27;
int mpin2 = 26;
int epin1 = 14;
int mpin3 = 18;
int mpin4 = 19;
int epin2 = 15;

const int freq = 30000;
const int pwmChannel = 0;
const int resolution = 8;
int dutyCycle = 200;


void setup() {
  Serial.begin(115200);
  pinMode(mpin1, OUTPUT);
  pinMode(mpin2, OUTPUT);
  pinMode(epin1, OUTPUT);
  pinMode(mpin3, OUTPUT);
  pinMode(mpin4, OUTPUT);
  pinMode(epin2, OUTPUT);

  ledcSetup(pwmChannel, freq, 8);
  

  Serial.println("Testing DC Motor..");

}

void loop() {
  String in_char = Serial.readStringUntil('\n');
  int code = in_char.toInt();
  //clockwise
  digitalWrite(mpin1, HIGH);
  digitalWrite(mpin2, LOW);
  digitalWrite(mpin3, HIGH);
  digitalWrite(mpin4, LOW);
  if(code < 256 && code > 0){
    analogWrite(epin2, 150);
    analogWrite(epin1,code);
    Serial.println(code);
    delay(100);
  }
  analogWrite(epin1,0);
  delay(100);
   analogWrite(epin2,0);
  

  /*for (int pace=55; pace <=100; pace++){
    analogWrite(epin, pace);
    Serial.println(pace);
    delay(200);
  }
  delay(2000);

  digitalWrite(mpin1, LOW);
  digitalWrite(mpin2, HIGH);

  delay(2000);

  for (int pace=255; pace >=0; pace--){
    analogWrite(epin, pace);
    Serial.println(pace);
    delay(50);
  }
  delay(2000);*/
}
