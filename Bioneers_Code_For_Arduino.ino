#include <dht.h>

int photoSensorPin = A0;
dht DHT;

#define DHT11_PIN 9

void setup() {
  pinMode(A0, INPUT);
  pinMode(9, INPUT);
  Serial.begin(9600);
  Serial.println("");
  Serial.println("TERRARIUM 4 DATA: "); // change terrarium number appropriately
  Serial.println("LIGHT ; TEMPERATURE ; HUMIDITY ; WARNING");
}

int lightValue = 0;
int temperatureValue = 0;
int humidityValue = 0;

void loop() {
  String data = "";
  lightValue = analogRead(photoSensorPin);
  //uncomment if using photoresistor sensors instead of photodiode
  lightValue = map(lightValue, 0, 1023, 1023, 0);
  DHT.read11(DHT11_PIN);
  temperatureValue = DHT.temperature;
  humidityValue = DHT.humidity;

  data += String(lightValue) + " ; " + String(temperatureValue) + " ; " + String(humidityValue);

  if(temperatureValue < 16 or temperatureValue > 20){
    data += " ; TEMP.RANGE_WARNING";
  }

  Serial.println(data);
  delay(2000);
  Serial.flush();
}
