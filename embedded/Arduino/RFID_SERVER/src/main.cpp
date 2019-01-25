#include <SPI.h>
#include <MFRC522.h>
#include <Arduino.h>
#include <ESP8266WiFi.h>

// Static defines
#define RST_PIN 9
#define SS_PIN 10

// Variables
byte* uid;
const char* ssid = "";
const char* password = "";

// Class init
MFRC522 rfid(SS_PIN, RST_PIN);

// WiFi functions
void wifi_init(const char* ssid, const char* password)
{

}

// RFID Functions
bool card_present()
{
    // Look for new cards
	if (!rfid.PICC_IsNewCardPresent())
		return false;

	// Verify if the NUID has been readed
	if (!rfid.PICC_ReadCardSerial())
		return false;

    Serial.println("[RFID: New card found]");
    return true;
}

byte* card_get_uid()
{
    Serial.println("[RFID: Getting UID]");
    MFRC522::Uid uidObj = rfid.uid;
    Serial.printf("[RFID: Uid is: ", uid);
    for (byte i = 0; i < uidObj.size; i++)
    {
        Serial.print(uidObj.uidByte[i] < 0x10 ? " 0" : " ");
        Serial.print(uidObj.uidByte[i], HEX);
    }
    return rfid.uid.uidByte;
}

// Server Functions
void send_server(byte* uid)
{

}



// Main functions
void setup()
{
    Serial.begin(11520);
    while (!Serial);
	SPI.begin();
	rfid.PCD_Init();
    wifi_init(ssid, password);
}

void loop()
{
    if (card_present())
    {
        uid = card_get_uid();
        Serial.println("[RFID: sending UID to server]");
        send_server(uid);
        uid = 0;
    }
}
