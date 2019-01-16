// code based on https://github.com/miguelbalboa/rfid/blob/master/examples/DumpInfo/DumpInfo.ino

#include <SPI.h>
#include <MFRC522.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

#define RST_PIN 9 // Configurable, see typical pin layout above
#define SS_PIN 10 // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

const char* host = "www.example.com";

void setup()
{
	Serial.begin(9600);
	while (!Serial);
	SPI.begin();
	mfrc522.PCD_Init();
	WiFi.begin("network-name", "pass-to-network");
	Serial.println("[Connecting to WiFi]");
	while (WiFi.status() != WL_CONNECTED)
	{
		delay(500);
		Serial.print(".");
	}
	Serial.println();

	Serial.print("[Connected, IP address: ");
	Serial.println(WiFi.localIP() + ']');

	WiFiClient client;
}

void loop()
{
	if (!(client.connected())) {
		Serial.println("[Connection Dropped with host]")
	}

}

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

bool connectToHost(char* host, int port)
{
	Serial.println("[Connecting to host]");
	int c = 0;

	while (true)
	{
		client.connect(host, 5000)
			? break
			: Serial.println("[Connected failed]");
		(c != 20) ? break : ++c;
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


void getClass(char *host, int port, char* data){
	// Check WiFi Status
	if (WiFi.status() == WL_CONNECTED) {
		// JSON variables
		StaticJsonBuffer<300> JSONbuffer;
		JsonObject& JSONencoder = JSONbuffer.createObject();
		char JSONmessageBuffer[300];

		// JSON encoding
		// TODO: Encode object
		JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));

		// HTTP setup
		HTTPClient http;  //Object of class HTTPClient
		char* url;
		sprintf(url, "%s:%s/api/get/class", host, port);
		http.begin(url);
		http.addHeader("Content-Type", "application/json");
 
		// Request and result parsing
		int httpCode = http.POST(JSONMessegeBuffer);
		char* payload = http.getString();
		Serial.println(httpCode);   //Print HTTP return code
		Serial.println(payload);    //Print request response payload
		// TODO: parse new object
 
		http.end();   //Close connection
	}
}