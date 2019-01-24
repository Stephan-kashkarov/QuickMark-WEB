#include <Arduino.h>
#include <SPI.h>
#include <MFRC522.h>
#include <ESP8266WiFi.h>

// Static defines
#define RST_PIN 9
#define SS_PIN 10

// Variable declaration and Class init
int64_t uid;

MFRC522 rfid(SS_PIN, RST_PIN);

// RFID Functions

bool read_card(int64_t* uid)
{
    // Look for new cards
	if (!rfid.PICC_IsNewCardPresent())
		return false;

	// Verify if the NUID has been readed
	if (!rfid.PICC_ReadCardSerial())
		return false;

    
}

// Server Functions
void send_server(int64_t* uid)
{

}


void setup()
{
    Serial.begin(11520);
    while (!Serial);
	SPI.begin();
	rfid.PCD_Init();
}

void loop()
{
    if (read_card(uid))
    {
        send_server(uid);
    }
}
