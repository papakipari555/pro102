import cv2

def take_snapshot():
    vd = cv2.VideoCapture(0)
    result =  True

    while(result):
        ret, frame = vd.read()
        cv2.imwrite("NewPicture.png",frame)
        result = False

        vd.relealse()
        cv2.destroyAllwindows()


take_snapshot()