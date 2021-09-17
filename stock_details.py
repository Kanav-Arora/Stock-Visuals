from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import ImageTk,Image
import webbrowser;
import backend;
from datetime import datetime

def value():
    global tickerEnter
    global dateEnter, highEnter, lowEnter, openEnter, closeEnter
    date_today = datetime.today()
    date_entered = datetime.strptime(dateEnter.get(), "%Y-%m-%d")
    if(date_entered<=date_today):
        tickerval = tickerEnter.get()
        dateval = dateEnter.get()
        data_json = backend.daily_o_c(tickerval.upper(),dateval)
        highEnter.configure(text = data_json['high'])
        lowEnter.configure(text = data_json['low'])
        openEnter.configure(text = data_json['open'])
        closeEnter.configure(text = data_json['close'])
    else:
        tkinter.messagebox.showerror(title = "Invalid Input", message = "Date should be of format YYYY-MM-DD")

root = Tk()
root.title("Stock Details")
root.resizable(False, False)

window_height = 500
window_width = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

myFrame = LabelFrame(root,bg="#3b404e", text = "Stock Details",bd=3, fg = "white", padx=5, pady=5, labelanchor = "n")
myFrame.place(relx = 0.5, rely = 0.5, relwidth = 0.9, relheight = 0.9, anchor = CENTER)

ticker = Label(myFrame, text = "Stock Ticker:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
ticker.grid(row = 0, column = 0, padx= 60, pady = 5)

date = Label(myFrame, text = "Date:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
date.grid(row = 1, column = 0, padx= 60, pady = 5)

tickerEnter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg ="white")
tickerEnter.grid(row = 0, column = 1, padx= 60, pady = 5)

dateEnter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
dateEnter.grid(row = 1, column = 1, padx= 60, pady = 5)

search = Button(myFrame, text = "Search",  bg = "#3b404e", relief = GROOVE, borderwidth= 2, command= lambda: value())
search.grid(row = 2, column = 0, columnspan = 2, padx= 30, pady=20)
search.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")

high = Label(myFrame, text = "High:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 10)
high.grid(row = 3, column = 0, padx= 60, pady = 5)

low = Label(myFrame, text = "Low:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 10)
low.grid(row = 4, column = 0, padx= 60, pady = 5)

open = Label(myFrame, text = "Open:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 10)
open.grid(row = 5, column = 0, padx= 60, pady = 5)

close = Label(myFrame, text = "Close:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 10)
close.grid(row = 6, column = 0, padx= 60, pady = 5)

highEnter = Label(myFrame, text = " " ,highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
highEnter.grid(row = 3, column = 1, padx= 80, pady = 5)

lowEnter = Label(myFrame, text = " " ,highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
lowEnter.grid(row = 4, column = 1, padx= 80, pady = 5)

openEnter = Label(myFrame, text = " " ,highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
openEnter.grid(row = 5, column = 1, padx= 80, pady = 5)

closeEnter = Label(myFrame, text = " " ,highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
closeEnter.grid(row = 6, column = 1, padx= 80, pady = 5)

home = Button(myFrame, text = "Home",  bg = "#3b404e", relief = GROOVE, borderwidth= 2)
home.grid(row = 7, column = 0, columnspan = 2, padx= 30, pady=20)
home.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")

root.mainloop()