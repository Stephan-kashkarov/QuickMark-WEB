import machine
import mfrc522
# Lib inits
rfid = mfrc522.MFRC522(0, 2, 4, 5, 14)

def get_uid():

    print("Reading!")

    while True:
        stat, tag_type = rfid.request(rfid.REQIDL)
        if stat == rfid.OK:
            stat, raw_uid = rfid.anticoll()
            if stat == rfid.OK:
                print("tag type: {}".format(tag_type))
                print("uid: {}".format(raw_uid))
                return raw_uid
            else:
                print("Something went wrong")
        else:
            print("No Card maybe?")

while True:
    get_uid()