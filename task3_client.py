#!/usr/bin/env python
# coding: utf-8

# In[3]:


import socket , struct, pickle, cv2, numpy, struct, sys

cap = cv2.VideoCapture(0)

s = socket.socket()
ip = "192.168.43.32"
port = 3333

#data = b""
#payload_siz = struct.calcsize("Q")

s.connect( (ip , port))
print(' SUCCESSUFULLY CONNECTED TO SERVER :   ', ip)

print("\n\n")

data = b""
payload_size = struct.calcsize("Q")
    
print("NB: Press 'q' or 'Enter' to close connection............. ")

while True:
    while len(data) < payload_size:
        print( "Start receiving Server Packet............")
        packet = s.recv(4*1024) # 4K
        if not packet: 
            break
            
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]

    while len(data) < msg_size:
        data += s.recv(4*1024)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("RECEIVING VIDEO",frame)
    key = cv2.waitKey(1)

# Press 'q' or 'Enter' to close the connection     
    if key  == ord('q') or key == 13:
        break
        
cv2.destroyAllWindows()        
s.close()

