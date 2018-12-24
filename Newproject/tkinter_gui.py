from Tkinter import *
import socket
def getGlobalIP():
    import urllib
    external_ip = urllib.urlopen('https://ident.me').read().decode('utf8')
    e1.config(text=str(external_ip))
def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    e2.config(text=str(s.getsockname()[0]))

window=Tk()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
b1=Button(window,text="Get global IP",command=getGlobalIP)
b1.grid(row=0,column=0)
b2=Button(window,text="Get local IP",command=getLocalIP)
b2.grid(row=1,column=0)

e1=Label(window,text="N/A")
e1.grid(row=0, column=1)
e2=Label(window,text="N/A")
e2.grid(row=1, column=1)

window.mainloop()