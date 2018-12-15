// code based on https://github.com/miguelbalboa/rfid/blob/master/examples/DumpInfo/DumpInfo.ino

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9 // Configurable, see typical pin layout above
#define SS_PIN 10 // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

void setup()
{

}

void loop()
{

}