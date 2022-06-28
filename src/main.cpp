#include <Arduino.h>
#include <WiFi.h>
#include <TFT_eSPI.h>
#include <WiFiServer.h>
#include <stdlib.h>
#define LED_PIN1 12
#define LED_PIN2 13

TFT_eSPI tft = TFT_eSPI();

const char* ssid="nova 5 Pro";
const char* pwd="12345678";
const int port = 34567;

WiFiServer server(port);

void setup() {
  Serial.begin(115200);
  tft.init();
  tft.setRotation(1);
  tft.setTextFont(2);
  tft.setTextColor(TFT_WHITE,TFT_BLACK);
  tft.fillScreen(TFT_BLACK);

  pinMode(LED_PIN1,OUTPUT);
  pinMode(LED_PIN2,OUTPUT);

  tft.setCursor(0,0);
  tft.println("Start connecting WIFI");
  WiFi.disconnect(false);
  delay(300);
  WiFi.begin(ssid,pwd);
  for(int i=0;WiFi.status() != WL_CONNECTED;i++){
    delay(300);
    tft.print(".");
    if (i%30==0&&i!=0)
    {
      Serial.println("......................");
      tft.println("?");
    }
    // WiFi.begin(ssid,pwd);
  }
  digitalWrite(LED_PIN1,HIGH);
  digitalWrite(LED_PIN2,HIGH);
  Serial.println("Connection established");
  Serial.print(WiFi.localIP());

  // tft.setCursor(0,0);
  tft.fillScreen(TFT_BLACK);
  tft.setCursor(0,0);
  tft.println("Network IP: ");
  tft.print(WiFi.localIP());
  tft.print(":");
  tft.print(port);

  server.begin();
  delay(3000);
}

void loop() {

  WiFiClient client = server.available();
  if(!client) return;
  Serial.println("new client connected!");
  tft.fillScreen(TFT_BLACK);
  tft.setCursor(0,0);
  tft.println("new client connected!");
  tft.print("remote IP: ");
  tft.println(client.remoteIP());
  client.setTimeout(5000);
  while(client.connected()){
    if(client.available()){
      String req = client.readStringUntil('\0');
      if(tft.getCursorY()>=80){
        tft.fillScreen(TFT_BLACK);
      }
      tft.setCursor(0,0);
      tft.println(req);
    }
    delay(5);
  }
  tft.fillScreen(TFT_BLACK);
  tft.setCursor(0,0);
  tft.println("\nNetwork IP: ");
  tft.print(WiFi.localIP());
  tft.print(":");
  tft.print(port);
  client.stop();
  delay(5);
  // while(1) delay(100);
  // put your main code here, to run repeatedly:
}
