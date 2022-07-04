# QRTicketValidator
## A program where you can create tickets with QR codes and check if they are valid.

### Overview
**barcode_maker.py** <br />
This is used by clients, when they create their tickets. When they enter their name and email, the program will create their personal qr code ticket.

**barcode_scanner.py** <br />
When the ticket needs to be validated, it can be checked with this program.

**db_create.py** <br />
This file creates a local database with sqlite3, in which all the data will be stored.

**db_view.py** <br />
In here you can see what is stored in the database.

###Common errors:

**Camera is not showing** <br />
If your camera is not showing, it is most likely because you need to change which camera source you are using.
If you are using an integrated webcam, you have to set `camera = cv2.VideoCapture(0)` in `barcode_scanner.py`.
If you are using an external webcam, your have to set `camera = cv2.VideoCapture(0)` in `barcode_scanner.py`.
