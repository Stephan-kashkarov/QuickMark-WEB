/*
RFID Server
====================================================================
Description:
 * rfid server is a program designed to be run on the node mcu v2.
 * Its purpose is to talk to a server and send across rfid uids.
 * This was made to create a marking system for school teacher with
 * rfid enabled student ids. This will make marking really quick.

Typical pin layout used:
 * -------------------------------------
 *             MFRC522      Expressif   
 *             Reader/PCD   ESP8266     
 * Signal      Pin          Pin         
 * -------------------------------------
 * RST/Reset   RST          D1        
 * SPI SS      SDA(SS)      D2          
 * SPI MOSI    MOSI         D7
 * SPI MISO    MISO         D6
 * SPI SCK     SCK          D5

Credits:
 * Written by Stephan kashkarov
 * In January, 2019
 * source: https://github.com/Stephan-kashkarov/QuickMark-RIFD/blob/master/embedded/Arduino/RFID_SERVER/src/main.cpp

*/

// Lib lnclude
#include <SPI.h>
#include <MFRC522.h>
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <stdio.h>


// Static defines
#define RST_PIN 5
#define SS_PIN  4

// Variables
std::vector<byte> uid;
std::vector<byte> prev_uid;
const char* ssid = "";
const char* password = "";

// Class init
MFRC522 rfid(SS_PIN, RST_PIN);


// General functions
void printHex(std::vector<byte> buffer, byte size)
/*
    Prints out byte vector in hex
*/
{
    for (byte i = 0; i < size; i++)
    {
        Serial.print(buffer[i] < 0x10 ? " 0" : " ");
        Serial.print(buffer[i], HEX);
    }
    Serial.println();
}

bool check_equal_vector(std::vector<byte> a, std::vector<byte> b)
/*
    Checks for equality between two byte vectors
*/
{
    Serial.println("[System: checking equality]");
    
    if (a.size() != b.size()){
        Serial.printf("[System: Size difference, A: %d, B: %d]\n", a.size(), b.size());
        return false;
    }
    Serial.println("[System: Sizes where correct!]");
    for(byte i = 0; i < a.size(); ++i)
    {
        Serial.printf("[System: Row %d, Byte A: %#04x, Byte B: %#04x]\n", i, a[i], b[i]);
        if (a[i] != b[i])
        {
            return false;
        }
    }
    Serial.println("[System: Check passed]");
    return true;
}

// WiFi functions
void wifi_init(const char* ssid, const char* password)
{

}

// RFID Functions
bool card_present()
{
    Serial.println("[RFID: Looking for card]");
    // Look for new cards
	if (!rfid.PICC_IsNewCardPresent())
		return false;

	// Verify if the NUID has been readed
	if (!rfid.PICC_ReadCardSerial())
		return false;

    Serial.println("[RFID: New card found]");
    return true;
}

void card_get_uid(std::vector<byte>& uuid)
{
    Serial.println("[RFID: Getting UID]");
    MFRC522::Uid uidObj = rfid.uid;
    uuid.resize(uidObj.size);
    for (byte i = 0; i < uidObj.size; i++)
    {
        uuid[i] = uidObj.uidByte[i];
    }
}



// Server Functions
void send_server(std::vector<byte> uuid)
{

}



// Main functions
void setup()
{
    Serial.begin(9600);
    while (!Serial);
	SPI.begin();
	rfid.PCD_Init();
    wifi_init(ssid, password);
}

void loop()
{
    if (card_present())
    {
        card_get_uid(uid);
        printHex(uid, uid.size());
        printHex(prev_uid, prev_uid.size());
        if (!check_equal_vector(prev_uid, uid)){
            Serial.println("[RFID: sending UID to server]");
            send_server(uid);
            Serial.println("[RFID: copying byte vector]");
            // byte_vec_cpy(uid, prev_uid);
            prev_uid.resize(uid.size());
            memcpy(&prev_uid[0], &uid[0], uid.size());
            Serial.println("Checking size outside byte vec copy");
            printHex(uid, uid.size());
            printHex(prev_uid, prev_uid.size());
            Serial.println("[RFID: Byte vector copied]");
        }
        else
        {
            Serial.println("[RFID: duplicate card]");
        }
        
    }
}
