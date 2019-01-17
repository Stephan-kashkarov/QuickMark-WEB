// RFID libs
#include <SPI.h>
#include <MFRC522.h>

// Web stuff
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

#define RST_PIN 9 // Configurable, see typical pin layout above
#define SS_PIN 10 // Configurable, see typical pin layout above
#define DEVICE_ID 1
#define DEVICE_PASSWORD "admin123"
#define NETWORK_NAME "BudiiLite-primary6537AF"
#define NETWORK_PASS "********"
#define HOST "https://steph-rfid-quickmark.herokuapp.com"
#define THUMBPRINT "2F 0E 48 24 F8 BA 05 3E 42 40 77 76 55 61 50 F0 2A DA 58 D2 05 FB 16 90 B8 1D A6 6D DD 76 C1 E4"

MFRC522 rfid(SS_PIN, RST_PIN); // Create MFRC522 instance
WiFiClient client;

int currentClassId = 1;

void scanForRfid()
{
	// Look for new cards
	if (!rfid.PICC_IsNewCardPresent())
		return;

	// Verify if the NUID has been readed
	if (!rfid.PICC_ReadCardSerial())
		return;
}

void getUid()
{

}



void getClass(int port = 10000 ){
	// Check WiFi Status
	if (WiFi.status() == WL_CONNECTED)
	{
		// JSON variables
		StaticJsonBuffer<300> JSONbuffer;
		JsonObject& JSONencoder = JSONbuffer.createObject();
		char JSONmessageBuffer[300];

		// * EXAMPLE JSON POST OBJECT
		//{
		//	"auth": {
		//		"id": int,
		//		"password": String,
		//	},
		//	"payload": {
		//		"class_id": int,
		//	},
		//}
		// * JSON encoding
		JsonObject& auth = JSONencoder.createNestedObject("auth");
		auth["id"] = DEVICE_ID;
		auth["password"] = DEVICE_PASSWORD;
		JsonObject& payload = JSONencoder.createNestedObject("payload");
		payload["class_id"] = currentClassId;
		JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));


		// * HTTP setup
		// POST /api/get/class HTTP/1.1
		// Host: steph-rfid-quickmark.herokuapp.com
		// Content-Type: application/json
		// cache-control: no-cache
		// Postman-Token: 8620daf9-d12a-47a5-b766-4e222902249c
		// {
		// "auth": {
		// 	"id": 1,
		// 	"password": "admin123"
		// },
		// "payload": {
		// 	"class_id": 0
		// }
		// }------WebKitFormBoundary7MA4YWxkTrZu0gW--
		
		HTTPClient http;  //Object of class HTTPClient
		http.begin(HOST, THUMBPRINT);
		http.addHeader("Content-Type", "application/json");
 
		// * Request and result parsing
		Serial.println("Sending object: ");
		JSONencoder.prettyPrintTo(Serial);
		// if (client.connect(HOST, 80)){
		// 	Serial.println("Connecting to host");
		// 	Serial.println("_______________________________________");
		// 	client.print("POST /api/get/class HTTPS/1.1\r\n");
		// 	client.print("Host: steph-rfid-quickmark.herokuapp.com\r\n");
		// 	client.print("Content-Type: application/json\r\n");
		// 	client.print("Content-Length: 300\r\n");
		// 	client.print("cache-control: no-cache\r\n");
		// 	client.print(JSONmessageBuffer);
		// 	client.println("------WebKitFormBoundary7MA4YWxkTrZu0gW--");
		// 	Serial.println("_______________________________________");
		// 	Serial.println("HTTP sent");

		// }
		// long interval = 2000;
		// unsigned long currentMillis = millis(), previousMillis = millis();
		// Serial.println("Waiting for reponse");
		// while(!client.available()){

		// 	if((currentMillis - previousMillis) > interval)
		// 	{

		// 		Serial.println("Timeout");
		// 		client.stop();     
		// 		return;
		// 	}
		// 	currentMillis = millis();
		// }

		// while (client.connected())
		// {
		// 	if (client.available())
		// 	{
		// 		char str = client.read();
		// 		Serial.print(str);
		// 	}      
		// }
		int httpCode = http.POST(JSONmessageBuffer);
		Serial.println("\n Data sent");
		String output = http.getString();
		Serial.print("Response code: ");
		Serial.println(httpCode);   // Print HTTP return code
		Serial.print("Response JSON: ");
		http.writeToStream(&Serial);
		// TODO: parse new object
 
		http.end();   // Close connection
	}
}

void setup()
{
	Serial.begin(9600);
	while (!Serial);
	SPI.begin();
	rfid.PCD_Init();
	WiFi.begin(NETWORK_NAME, NETWORK_PASS);
	Serial.println("[Connecting to WiFi]");
	Serial.print("[Network Name: ");
	Serial.print(NETWORK_NAME);
	Serial.printf("Network Pass: %s]\n", NETWORK_PASS);
	while (WiFi.status() != WL_CONNECTED)
	{
		delay(500);
		Serial.print(".");
	}
	Serial.println();

	Serial.print("[Connected, IP address: ");
	Serial.print(WiFi.localIP());
	Serial.println("]");


	getClass();
}

void loop()
{
	// if (!(client.connected()))
	// {
	// 	Serial.println("[Connection Dropped with host]");
	// }

}
