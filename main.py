import cv2
import webbrowser


cap=cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

try:
    while True:
        _,img=cap.read()
        data,one, _=detector.detectAndDecode(img)
        if data:
            a=data
            break
        cv2.imshow('QrCode Scanner App',img)
        if cv2.waitKey(1)==ord('q'):
            break
    b=webbrowser.open(str(a))
    cap.release(a)
except Exception as e:
    print("Error occured",e)

cv2.destroyAllWindows()
    