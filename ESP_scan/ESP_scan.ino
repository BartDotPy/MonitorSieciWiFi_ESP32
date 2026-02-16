#include <WiFi.h>
#include <ESPping.h>

void setup(){
  Serial.begin(115200); //upload speed
  WiFi.mode(WIFI_STA); //tryb stacji
  WiFi.disconnect(); //reset
}

void loop() {
  //Instrukcje warunkowe do obsługi komend ze strony (streamlit)
  if (Serial.available() > 0){
    String command = Serial.readStringUntil('\n');

    if(command == "SCAN"){
      Serial.println("Start_list");
      int n = WiFi.scanNetworks();

      for(int i=0; i<n; i++){
        Serial.print(WiFi.SSID(i));
        Serial.print("|");
        Serial.println(WiFi.RSSI(i));
      }
      Serial.println("END_LIST");
    }

  }
}