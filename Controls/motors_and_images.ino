
// deals a card on a button press 
// coordinates timing of photo from ESP32-CAM and motors so that the motors hold the card out enough for a photo, and then deals it
// this works, but it just turns them both on after you press the button and its at full speed cuz we digital wrote the enable pins to high

#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include "esp_timer.h"
#include "img_converters.h"
#include "Arduino.h"
#include "fb_gfx.h"
#include "soc/soc.h" //disable brownout problems
#include "soc/rtc_cntl_reg.h"  //disable brownout problems 
#include "esp_http_server.h"


//Replace with your network credentials
const char* ssid = "iPhone";
const char* password = "1234567890";

//Your Domain name with URL path or IP address with path
const char* serverName = "http://172.20.10.8:8888/ESP"; // this is aum's IP

// Photo File Name
#define FILE_PHOTO "/photo.jpg"


// Physical Button
#define Button 14

// LED
#define blueLED 2


// motor pins
#define mpinL 4 //motor in1 and in3
#define mpinR 15 //motor in2 and in4

// enable pins
#define epin1 13 //blue wheel
#define epin2 12 //black wheel

const int freq = 30000;
const int pwmChannel_blue = 0;
const int pwmChannel_black = 1;
//const int resolution = 8;
int dutyCycle = 200;

// Variables will change: 
int ledState = LOW;          // the current state of the output pin
int buttonState;             // the current reading from the input pin
int lastButtonState = LOW;   // the previous reading from the input pin

// Button pushing counter
int counter = 3;

// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers


// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 5 seconds (5000)
unsigned long timerDelay = 5000;

#define CAMERA_MODEL_AI_THINKER // Has PSRAM
#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27

#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22


void setup() {
  pinMode(mpinL, OUTPUT);
  pinMode(mpinR, OUTPUT);
  pinMode(epin1, OUTPUT);
  pinMode(epin2, OUTPUT);

  pinMode(Button, INPUT);

  pinMode(blueLED, OUTPUT);
  // initialize the LED to be off
  digitalWrite(blueLED, LOW);
  
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  
  //ledcSetup(pwmChannel, freq, resolution);
  ledcSetup(pwmChannel_blue, freq, 8);
  ledcSetup(pwmChannel_black, freq, 8);
  
  Serial.println("Testing DC Motor..");
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(epin1, pwmChannel_blue);
  ledcAttachPin(epin2, pwmChannel_black);

  Serial.println(WiFi.macAddress());
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
 
  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_SVGA;
  config.jpeg_quality = 12;
  config.fb_count = 1;

  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
    
}
sensor_t * s = esp_camera_sensor_get();
  // initial sensors are flipped vertically and colors are a bit saturated
  if (s->id.PID == OV3660_PID) {
    s->set_vflip(s, 1); // flip it back
    s->set_brightness(s, 1); // up the brightness just a bit
    s->set_saturation(s, -2); // lower the saturation
  }
  // drop down frame size for higher initial frame rate
  s->set_framesize(s, FRAMESIZE_QVGA);
}

void loop() {
  
  // read the state of the switch into a local variable:
  int reading = digitalRead(Button);

  // check to see if you just pressed the button
  // (i.e. the input went from LOW to HIGH), and you've waited long enough
  // since the last press to ignore any noise:

  // If the switch changed, due to noise or pressing:
  if (reading != lastButtonState) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // whatever the reading is at, it's been there for longer than the debounce
    // delay, so take it as the actual current state:

    // if the button state has changed:
    if (reading != buttonState) {
      buttonState = reading;

      // only toggle the LED if the new button state is HIGH
      if (buttonState == HIGH) {
        ledState = !ledState;
        // if the button is pushed
        Serial.println("button pushed");
        digitalWrite(blueLED, HIGH); //turn on LED when button is pushed
        if ((counter % 2) == 1){ //if the coutner is odd, run the motors
        //code to run motors:
        
        //clockwise
        digitalWrite(mpinL, LOW);
        digitalWrite(mpinR, HIGH);
        
        // this turns on the blue then the black 
        ledcWrite(pwmChannel_blue, 200);
        delay(500);
        ledcWrite(pwmChannel_blue, 0);
        delay(500);
        ledcWrite(pwmChannel_black, 200);
        delay(500);
        ledcWrite(pwmChannel_black, 0);
        
        counter = counter+1;
        Serial.print(counter);
        }
        if ((counter % 2) == 0){ //if the coutner is even, run the image capture
          //take an image
        camera_fb_t * fb = NULL;
        fb = esp_camera_fb_get();
        if(!fb) {
          counter = counter -1;
          Serial.println("Camera capture failed");
          delay(1000);
          //ESP.restart();
          }
          
          //Check WiFi connection status
          if(WiFi.status()== WL_CONNECTED){
            
            WiFiClient client;
            
            HTTPClient http;
    
            // Your Domain name with URL path or IP address with path
            http.begin(client, serverName); // i commented this one out

          
            Serial.println("Trying to send a pic...");
            http.addHeader("Content-Type", "image/jpg");
            int httpResponseCode = http.POST(fb->buf, fb->len);

            if (httpResponseCode>0) {
              String payload = http.getString();
              Serial.println(payload);
              }
            else {
                Serial.print("Error:");
                Serial.println(httpResponseCode);
                Serial.println("Sent Picture");
             }
   
                http.end();
              }
              
              else {
                 Serial.println("WiFi Disconnected");
               }
               lastTime = millis();
        counter = counter+1;
        Serial.print(counter);
        }
       
             }
           }
    }
 

  // save the reading. Next time through the loop, it'll be the lastButtonState:
  lastButtonState = reading;
  digitalWrite(blueLED, LOW);
  
  
}
