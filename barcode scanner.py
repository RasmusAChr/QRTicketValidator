import cv2
from pyzbar import pyzbar
import sqlite3

found_code = False

"""
Looking for a barcode and retrieving the data.
"""
def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    global found_code
    
    for barcode in barcodes:
        found_code = True
        x, y , w, h = barcode.rect

        # Decoding the barcode and retrieving the data.
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
            
        validate_code(barcode_info)
    
    return frame

"""
Checking the barcode to see if it is valid.
"""
def validate_code(barcode_info):
    record = None
    # Checking if the barcode data exists in the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()    
    for row in c.execute('SELECT * FROM codetable WHERE code=:barcode_info', {'barcode_info': barcode_info.encode('iso-8859-15')}):
        try:
            record = row
        except:
            record = None
        
    conn.commit()
    conn.close()

    if record == None:
        print("Code is NOT valid.")
    elif barcode_info.encode('iso-8859-15') == record[3]:
        print("Name: {0}.".format(record[1]))
        print("Email: {0}.".format(record[2]))
        print("Code is valid.")
    else:
        print("Unexpected error")
        

"""
Initializing the camera setup
"""
def main():
    global found_code

    # Initializing camera popup window.
    camera = cv2.VideoCapture(1)
    ret, frame = camera.read()

    # Searching for a barcode until found or escape is pressed.
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        if found_code == True:
            break
        
    # If code is found or user pressed escape, then close the camera window.    
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
