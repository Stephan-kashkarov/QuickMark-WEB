// code based on https://github.com/miguelbalboa/rfid/blob/master/examples/DumpInfo/DumpInfo.ino

#include <SPI.h>
#include <MFRC522.h>
#include <ESP8266WiFi.h>

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

void postToHost(char* host, int port, char* data)
{
	if (connectToHost(host, port))
	{
		
	}
}

void getToHost(char *host, int port, char* data)
{
	if (connectToHost(host, port))
	{
		Serial.println("[Sending a request]");
		client.print(String("GET /") + " HTTP/1.1\r\n" +
					 "Host: " + host + "\r\n" +
					 "Connection: close\r\n" +
					 "\r\n");

		Serial.println("[Response:]");
		while (client.connected() || client.available())
		{
			if (client.available())
			{
				String line = client.readStringUntil('\n');
				Serial.println(line);
			}
		}
		client.stop();
		Serial.println("\n[Disconnected]");
	}
}