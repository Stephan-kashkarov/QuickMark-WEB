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
#define NETWORK_PASS "PASSWORD"
#define HOSTSTART https://steph-rfid-quickmark.herokuapp.com
#define HOSTEND

MFRC522 rfid(SS_PIN, RST_PIN); // Create MFRC522 instance
WiFiClient client;

int currentClassId;

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

bool connectToHost(char* host, int port = 5000)
{
	Serial.println("[Connecting to host]");
	int c = 0;

	while (true)
	{
		if(client.connect(host, port))
		{
			break;
		}
		else
		{
			Serial.println("[Connected failed]");
		}
		if (c != 20)
		{
			break;
		}
		else
		{
			++c;
		}
		delay(1000);
	}

	if (client.connected()){
		Serial.println("[Connected to host]");
		return true;
	} else {
		Serial.println("[Connection timed out]");
		return false;
	}
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
		HTTPClient http;  //Object of class HTTPClient
		char* url = "https://steph-rfid-quickmark.herokuapp.com/api/get/class";
		// if (port > 9999)
		// {
		// 	sprintf(url, "%s/api/get/class", host);
		// }
		// else
		// {
		// 	sprintf(url, "%s:%04d/api/get/class", host, port);
		// }
		http.begin(url);
		http.addHeader("Content-Type", "application/json");
 
		// * Request and result parsing
		Serial.println("Sending object: ");
		JSONencoder.prettyPrintTo(Serial);
		int httpCode = http.POST(JSONmessageBuffer);
		Serial.println("\n Data sent");
		String output = http.getString();
		Serial.print("Response code: ");
		Serial.println(httpCode);   // Print HTTP return code
		Serial.print("Response JSON");
		Serial.println(output);    // Print request response output
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
