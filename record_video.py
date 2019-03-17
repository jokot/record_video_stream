import numpy as np
import cv2
import time

def record_video(url,file_name,duration):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(url)

    # Check if ther is internet /  the link is correct
    if (cap.isOpened() == False):
        print("No internet conection or the link is broken")

    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create VideoWriter object.The output is stored in 'file_name' file.
    out = cv2.VideoWriter(file_name,cv2.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))

    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()

        if ret == True:
            # Write the frame into the file 'file_name'
            out.write(frame)
            
            # Display the resulting frame 
            cv2.imshow('recording....', frame)

            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break
        
    # When everything done, release the video capture and video write objects
    cap.release()
    out.release()
    

####------> Main Program <------####------> Main Program <------####------> Main Program <------####------> Main Program <------####------> Main Program <------####
url = 'http://cctv-dishub.sukoharjokab.go.id/zm/cgi-bin/nph-zms?mode=jpeg&monitor=8&scale=100&maxfps=15&buffer=1000&user=user&pass=user'
file_name = 'output.avi'
duration = 120 # durasi in sec
    
# Closes all the frames
cv2.destroyAllWindows() 
