from urllib.request import urlopen 
from bs4 import BeautifulSoup
from tkinter import*
from tkinter import Button
import tkinter
t=tkinter.Tk()
t.iconbitmap("")
t.wm_title("Simple Quote")
frame=Frame(t,bg="grey")
entry=Entry(frame,bd=5)
frame.pack()
entry.pack()
def searchbox():
   quote=entry.get()
   html = urlopen("https://www.google.com/finance?q="+quote.upper()) 
   bsOBJ=BeautifulSoup(html.read(),"html.parser")
   name=bsOBJ.head.title
   quote=bsOBJ.find(attrs={"class":"pr"})
   var=StringVar()
   stock=Label(t,textvariable=var,bg="green")
   if quote:
      aname=str(name.get_text())
      aquote=str(quote.get_text())
      var.set(aname+" "+aquote)
   else:
      var.set('Please enter a valid ticker')
   stock.pack()
search=tkinter.Button(frame,text="Search for Ticker",command=searchbox)
search.pack()
t.mainloop()