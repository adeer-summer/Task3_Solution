#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Server  code 
# Lets import the libraries

import cv2, pandas, numpy, socket, pickle, struct, imutils

# Socket Create
con = socket.socket()
con.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)

port = 3333
ip = ""

# Socket Bind
con.bind( (ip , port))
print('Socket bind complete...')
print("\n\n")

# Socket Listen
con.listen()
print('Socket now listening......')

csession , addr = con.accept()


# Socket Accept
while True:
    print('GOT CONNECTION FROM:',addr)
    if csession:
        cap = cv2.VideoCapture(0)
        
        while (cap.isOpened()):
            ret,frame = cap.read()
            frame = imutils.resize(frame,width=320)
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            csession.sendall(message)
            
            cv2.imshow('TRANSMITTING VIDEO',frame)
            key = cv2.waitKey(1) 
            if key ==ord('q') or key == 13:
                 break
                
cv2.destroyAllWindows()
csession.close()






