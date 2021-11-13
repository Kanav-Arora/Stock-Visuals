from tkinter import *
from tkinter import messagebox
import tkinter
import webbrowser;
import backend;
from datetime import datetime

def value():
    global tickerEnter
    global indicator1,indicator2,indicator3,indicator4
    indicator1 = Button(myFrame, text = "Indicator 1",  bg = "#3b404e", relief = GROOVE, borderwidth= 2)
    indicator1.grid(row = 9, column = 0, columnspan = 1, padx= 0, pady=20)
    indicator1.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    
    indicator2 = Button(myFrame, text = "Indicator 2",  bg = "#3b404e", relief = GROOVE, borderwidth= 2)
    indicator2.grid(row = 9, column = 1, columnspan = 1, padx= 0, pady=20)
    indicator2.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")

    indicator3 = Button(myFrame, text = "Indicator 3",  bg = "#3b404e", relief = GROOVE, borderwidth= 2)
    indicator3.grid(row = 10, column = 0, columnspan = 1, padx= 0, pady=20)
    indicator3.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")

    indicator4 = Button(myFrame, text = "Indicator 4",  bg = "#3b404e", relief = GROOVE, borderwidth= 2)
    indicator4.grid(row = 10, column = 1, columnspan = 1, padx= 0, pady=20)
    indicator4.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
        
    home = Button(myFrame, text = "Home",  bg = "#3b404e", relief = GROOVE, borderwidth= 2)
    home.grid(row = 15, column = 0, columnspan = 2, padx= 0, pady=0)
    home.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    


root = Tk()
root.title("Plot Details")
root.resizable(False, False)

window_height = 500
window_width = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

myFrame = LabelFrame(root,bg="#3b404e", text = "Enter the Plot Details",bd=3, fg = "white", padx=5, pady=5, labelanchor = "n")
myFrame.place(relx = 0.5, rely = 0.5, relwidth = 0.9, relheight = 0.9, anchor = CENTER)

ticker = Label(myFrame, text = "Stock Ticker:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
ticker.grid(row = 0, column = 0, padx= 60, pady = 5)

fromdate = Label(myFrame, text = "From Date:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
fromdate.grid(row = 1, column = 0, padx= 60, pady = 5)

todate = Label(myFrame, text = "To Date:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
todate.grid(row = 2, column = 0, padx= 60, pady = 20)

tickerEnter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg ="white")
tickerEnter.grid(row = 0, column = 1, padx= 60, pady = 5)

fromdateEnter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
fromdateEnter.grid(row = 1, column = 1, padx= 60, pady = 5)

todateEnter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
todateEnter.grid(row = 2, column = 1, padx= 60, pady = 20)

next = Button(myFrame, text = "Next",  bg = "#3b404e", relief = GROOVE, borderwidth= 2, command= lambda: value())
next.grid(row = 4, column = 0, columnspan = 2, padx= 0, pady=0)
next.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")


root.mainloop()