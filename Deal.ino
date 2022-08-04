const int servoPin = 16;  /* GPIO16 */

int dutyCycle = 0;
int playercycle[10] = {0,0,25,13,8,5,4,3,3,2};
int boarddist = 4;
int first_time = 2000;
int pic_time = 1000;
int second_time = 200;


/* Setting PWM properties */
const int PWMFreq = 50;
const int PWMChannel = 0;
const int PWMResolution = 8;
//const int MAX_DUTY_CYCLE = (int)(pow(2, PWMResolution) - 1);

void setup()
{  
  Serial.begin(115200);
  ledcSetup(PWMChannel, PWMFreq, PWMResolution);
  /* Attach the LED PWM Channel to the GPIO Pin */
  ledcAttachPin(servoPin, PWMChannel);
  ledcWrite(PWMChannel, dutyCycle);
}
void loop()
{
  ledcWrite(PWMChannel, 10);
  while(Serial.available())
  {
    String in_char = Serial.readStringUntil('\n');
    int code = in_char.toInt();
    String stage;
    int players;
    int wait = 0;
    /*positions 6-32 are the ones*/
    if (code < 7){
      stage = "deal";
      Serial.println(stage);
      players = code;
      
      for (int t = 0; t < 2; t++){
        dutyCycle = 6;
        for (int i = 0; i < players; i++){
          Serial.println(dutyCycle);
          ledcWrite(PWMChannel, dutyCycle);
          delay(500);
          dutyCycle = dutyCycle + playercycle[players];
        }
      }
    
    }
    else if (code < 8){
      stage = "flop";
      Serial.println(stage);
      dutyCycle = 6;
      for (int j = 0; j < 4; j++){
        Serial.println(dutyCycle);
        ledcWrite(PWMChannel, dutyCycle);
        delay(500);
        dutyCycle = dutyCycle + boarddist;
      }
    }
    else if (code < 9){
      stage = "turn";
      Serial.println(stage);
      dutyCycle = 6;
      Serial.println(dutyCycle);
      ledcWrite(PWMChannel, dutyCycle);
      delay(500);
      dutyCycle = 6 + 4*boarddist;
      Serial.println(dutyCycle);
      ledcWrite(PWMChannel, dutyCycle);
      delay(500);
    }
    else if (code < 10){
      stage = "river";
      Serial.println(stage);
      dutyCycle = 6;
      Serial.println(dutyCycle);
      ledcWrite(PWMChannel, dutyCycle);
      delay(500);
      dutyCycle = 6 + 5*boarddist;
      Serial.println(dutyCycle);
      ledcWrite(PWMChannel, dutyCycle);
      delay(500);
    }
    else if (code != 10 && code != 11){
      stage = "dispense";
      Serial.println(stage);
      
      dutyCycle = code;
      ledcWrite(PWMChannel, dutyCycle);
      Serial.println(dutyCycle);
      delay(first_time);
      
      dutyCycle = 0;
      ledcWrite(PWMChannel, dutyCycle);
      Serial.println(dutyCycle);
      delay(pic_time);
      
      dutyCycle = code;
      ledcWrite(PWMChannel, dutyCycle);
      Serial.println(dutyCycle);
      delay(second_time);
      
      dutyCycle=0;
      ledcWrite(PWMChannel, dutyCycle);     
    }
    else if (code == 10){
      stage = "test";
      Serial.println(stage);
      for (int i = 15; i < 30;){
        Serial.println(i);
        ledcWrite(PWMChannel, i);
        delay(2000);
        i = i+1;
      }
    }
    else if (code == 11){
      stage = "test 0";
      Serial.println(stage);
      ledcWrite(PWMChannel, 0);
      Serial.println(0);
    }
  }
}
