import socket		
import time
import sys	 
from tkinter import *
from tkinter import messagebox

# threshold setting
threshold1_setting = 100000 # Rate limitation
threshold2_setting = 100020 # System Shutdown

# accpetance rate setting
rate_setting = 0

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8000	
reached_threshold_1 = False
reached_threshold_2 = False
connections = []
blocked_socket = []

def alert_window2(threshold2_setting):
    window = Tk()
    window.lift()
    window.attributes('-topmost',True)
    window.withdraw()
    messagebox.showwarning('Alert', 'Reached the second threshold in server with ' + str(threshold2_setting) + ' connections.')
    window.deiconify()
    window.destroy()
    window.quit()


# defense
def firewall(threshold_1, threshold_2, addr, sock, connections):
    ClosedSock = 0

    # threshold 1 setting
    global reached_threshold_1
    if reached_threshold_1 == False:
        if len(connections) >= threshold_1:
            print(" ")
            print("---------------Acceptance Rate is limited!---------------")
            print(" ")
            global rate_setting
            rate_setting = 1
            reached_threshold_1 = True


    # threshold 2 setting
    global reached_threshold_2
    if reached_threshold_2 == False:
        if len(connections) >= threshold_2:
            print(" ")
            print("---------------Server has been Shut Down!---------------")
            print(" ")
            
            reached_threshold_2 = True
            alert_window2(threshold_2)
            sys.exit()

    
    
    
    # filtering 
    with open("blackList.txt", 'r') as file:
        for line in file:
            Aline = line.strip()
            if Aline == str(addr[1]):
                if str(addr[1]) != ClosedSock: 
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                    ClosedSock = str(addr[1])
                else:
                    break
                print("---------------", addr[1], " was terminated")
                blocked_socket.append(str(addr[1]))
                if str(addr[1]) in connections:
                    connections.remove(str(addr[1]))
                    with open('stoppedTraffic.txt', 'a') as file:
                        file.write(str(addr[1])+'\n')
                        
                        
                


             


s = socket.socket()		 	
s.bind((SERVER_IP, SERVER_PORT))		 
print ("The port of server is %s" %(SERVER_PORT)) 


s.listen(0)	 
print("Server is ready")
print ("Listening......")		 


while True: 
    time.sleep(rate_setting)
    sock, addr = s.accept()	 
    print('Received connection from', addr[1])
    connections.append(str(addr[1]))
    

    #defense
    firewall(threshold1_setting, threshold2_setting, addr, sock, connections)
    

    with open('tempHistory.txt', 'a') as file:
        file.write(str(addr[1])+'\n')
    



    


    
