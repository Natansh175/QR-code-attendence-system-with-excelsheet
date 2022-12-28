import cv2
import csv
import datetime

today = datetime.datetime.now()
# Capturing frame in cap varibale
cap = cv2.VideoCapture(0)
# Creating detection function for QR Code
detection = cv2.QRCodeDetector()

while True:
    # Reading frame cap
    ret, frame = cap.read()
    # Decoding the frame for QR Code data
    data, box, point = detection.detectAndDecode(frame)
    # Printing frame
    cv2.imshow("QR Code Scanner", frame)

    if cv2.waitKey(1) & len(data) > 1:
        break

# Writing the QR Code data
l1 = data.split(",")
l1.append("P")
l1.append(today)
header = ['Name', 'Er_No','Batch', 'Attendance', 'Date']

with open('Attendance.csv', 'a+', encoding='UTF8', newline='\n') as f:
    writer = csv.writer(f)

    # write the header once at beginning
    #writer.writerow(header)

    # write multiple rows
    writer.writerow(l1)


print(l1)


cap.release()
cv2.destroyAllWindows()