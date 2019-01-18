import machine
import urequests
import ujson
import mfrc522

# Constant Variables
URL = "https://steph-rfid-quickmark.herokuapp.com/"
DEVICE_ID = 1
DEVICE_PASSWORD = "admin123"


# Lib inits
rfid = mfrc522.MFRC522(5, 7, 6, 1, 2)


def get_class(class_id):
    data = {
        "auth": {
            "id": DEVICE_ID,
            "password": DEVICE_PASSWORD,
        },
        "payload": {
            "class_id": class_id,
        },
    }
    urequests.post(URL+"/api/get/class", ujson.dumps(data))

def get_uid():

    print("Reading!")

    while True:
        stat, tag_type = rfid.request(rfid.REQIDL)
        if stat == rfid.OK:
            stat, raw_uid = rfid.anticoll()
            if stat == rfid.OK:
                print("tag type: " + tag_type)
                print("uid: " + raw_uid)
                return raw_uid
            else:
                print("Something went wrong")
        else:
            print("No Card maybe?")

print("Hello!")
