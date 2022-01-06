import cv2
import dropbox
import time
import random

starttime=time.time()
def take_snapshot():
    number=random.randint(0,100)
    #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        #print(ret) 
        img_name="img"+str(number)+".png"

        #cv2.imwrite() method is used to save  an image to any storage device
        cv2.imwrite(img_name,frame)
        #starttime=time.time()

        result=False
    return img_name
    print("snapshot taken")
    #release the camera
    videoCaptureObject.release()
    #close all the windows that might have been opened in the process
    cv2.destroyAllWindows()

def upload_file(img):
    acces_token="sl.A_lDYvtCIDIRoSYNgxqyPn3B_MBKiIlix0OjsScTXn4RLVuZ-9nKGi5r1env3Xym1DaDvfncDFqT86kpDpgrE57_K8gR4y5dpR9JJ9yVeYtz9_8jaLMyzsTaQ_0lkdQQZ_dUiY4"
    fileFrom=img
    fileTo="/new folder 1/"+img
    dbx=dropbox.Dropbox(acces_token)

    with open(fileFrom,"rb") as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)

def main():
    counter=1
    while(counter<=5):
        if(time.time()-starttime>=5):
            name=take_snapshot()
            upload_file(name)
            counter=counter+1

main()