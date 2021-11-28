from tkinter import *
import tkinter
from PIL import ImageTk, Image
from tkinter import ttk
import backend
from tkinter import colorchooser
from tkinter import messagebox
import webbrowser
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import pandas as pd
import numpy as np
import yfinance
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas_ta as ta

import requests

plt.style.use('fivethirtyeight')

# -------------------------------- Home Window ---------------------------------------

def home_window(root):
    myFrame.config(text="Home Page")
    myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.4, anchor=CENTER)


    for child in myFrame.winfo_children():
        child.destroy()

    stock_index = Button(myFrame, text="Stock Index", bg="#3b404e",  
                         relief=GROOVE, borderwidth=2, command=lambda: stock_index_window(root))
    stock_index.config(highlightbackground="#3b404e",
                       highlightthickness=2, highlightcolor="#3b404e")
    stock_index.grid(row=1, padx=290, pady=12, sticky="nesw")

    crypto_index = Button(myFrame, text="Crypto Index",
                          bg="#3b404e",  relief=GROOVE, command=lambda:  crypto_index_window(root))
    crypto_index.config(highlightbackground="#3b404e",
                        highlightthickness=2, highlightcolor="#3b404e")
    crypto_index.grid(row=2, padx=290, pady=12, sticky="nesw")

    stock_details = Button(myFrame, text="Stock Details",
                           bg="#3b404e",  relief=GROOVE, command=lambda: stock_details_window(root))
    stock_details.config(highlightbackground="#3b404e",
                         highlightthickness=2, highlightcolor="#3b404e")
    stock_details.grid(row=3, padx=290, pady=12, sticky="nesw")

    crypto_details = Button(myFrame, text="Crypto Details",
                            bg="#3b404e",  relief=GROOVE, command=lambda: crypto_details_window(root))
    crypto_details.config(highlightbackground="#3b404e",
                          highlightthickness=2, highlightcolor="#3b404e")
    crypto_details.grid(row=4, padx=290, pady=12, sticky="nesw")

    plot_info = Button(myFrame, text="Analysis",
                       bg="#3b404e",  relief=GROOVE, command=lambda: plot_info_window(root))
    plot_info.config(highlightbackground="#3b404e",
                     highlightthickness=2, highlightcolor="#3b404e")
    plot_info.grid(row=5, padx=290, pady=12, sticky="nesw")

# -------------------------------------------------------------------------------------

# -------------------------------- Stock Index Window ---------------------------------------


def stock_index_window(root):
    myFrame.config(text="Stock Index")
    myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.53, anchor=CENTER)
    
    datalist = backend.refresh()
    for child in myFrame.winfo_children():
        child.destroy()

    def query_database():
        for record in my_tree.get_children():
            my_tree.delete(record)

        global count
        count = 1

        for i in range(1,len(datalist)):
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(count,
                                                                                   datalist[i][1], datalist[i][0]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(count,
                                                                                   datalist[i][1], datalist[i][0]), tags=('oddrow',))
            count += 1

    def lookup_records():
        global search_entry, search

        search = Toplevel(root)
        search.title("Lookup Records")

        window_height = 180
        window_width = 400

        screen_width = search.winfo_screenwidth()
        screen_height = search.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        search.geometry("{}x{}+{}+{}".format(window_width,
                        window_height, x_cordinate, y_cordinate))

        #search.iconbitmap('./DSC logo.ico')

        search_frame = LabelFrame(search, text="Enter the Company Name")
        search_frame.pack(padx=10, pady=10)

        search_entry = Entry(search_frame, font=("Helvetica", 18))
        search_entry.pack(pady=20, padx=20)

        search_button = Button(
            search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)

    def search_records():
        lookup_record = search_entry.get()
        final = []
        for i in datalist:
            if i[1] == lookup_record:
                final.append(i)

        search.destroy()
        for record in my_tree.get_children():
            my_tree.delete(record)

        global count
        count = 0

        for i in range(len(final)):
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(count, final[i][1], final[i][0]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(count, final[i][1], final[i][0]), tags=('oddrow',))
            count += 1

    def primary_color():
        primary_color = colorchooser.askcolor()[1]
        if primary_color:
            my_tree.tag_configure('evenrow', background=primary_color)

    def secondary_color():
        secondary_color = colorchooser.askcolor()[1]

        if secondary_color:
            my_tree.tag_configure('oddrow', background=secondary_color)

    def highlight_color():
        highlight_color = colorchooser.askcolor()[1]

        if highlight_color:
            style.map('Treeview', background=[('selected', highlight_color)])

    my_menu = Menu(root)
    root.config(menu=my_menu)

    option_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Primary Color", command=primary_color)
    option_menu.add_command(label="Secondary Color", command=secondary_color)
    option_menu.add_command(label="Highlight Color", command=highlight_color)
    option_menu.add_separator()
    option_menu.add_command(label="Exit", command=root.quit)

    search_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Search", menu=search_menu)

    search_menu.add_command(label="Reset", command=query_database)
    search_menu.add_command(label="Search", command=lookup_records)

    style = ttk.Style()

    style.theme_use('default')

    style.configure("Treeview",
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#D3D3D3")
    style.map('Treeview',
              background=[('selected', "#347083")])

    tree_frame = Frame(myFrame)
    tree_frame.pack(pady=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(
        tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ("S.no", "Company Name", "Company Symbol")

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("S.no", anchor=CENTER, width=35)
    my_tree.column("Company Name", anchor=W, width=700)
    my_tree.column("Company Symbol", anchor=W, width=105)

    my_tree.heading("#0", text="S.no", anchor=W)
    my_tree.heading("S.no", text="S.no", anchor=W)
    my_tree.heading("Company Name", text="Company Name", anchor=W)
    my_tree.heading("Company Symbol", text="Company Symbol", anchor=W)

    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    query_database()

    def select_record(e):
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')

    def update_record():
        selected = my_tree.focus()

        my_tree.delete(*my_tree.get_children())

    def create_table_again():

        c.execute()

    home = Button(myFrame, text="Home", bg="#3b404e",  
                  relief=GROOVE, command=lambda: home_window(root))
    home.config(highlightbackground="#3b404e",
                highlightthickness=2, highlightcolor="#3b404e")
    home.pack(pady=25)

# -------------------------------------------------------------------------------------


# -------------------------------- Crypto Index Window ---------------------------------------

def crypto_index_window(root):
    myFrame.config(text="Crypto Index")
    myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.53, anchor=CENTER)

    datalist = backend.crypto_refresh()
    for child in myFrame.winfo_children():
        child.destroy()

    def query_database():
        for record in my_tree.get_children():
            my_tree.delete(record)

        global count
        count = 1

        for i in range(1,len(datalist)):
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(count,
                                                                                   datalist[i][1], datalist[i][0]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(count,
                                                                                   datalist[i][1], datalist[i][0]), tags=('oddrow',))
            count += 1

    def lookup_records():
        global search_entry, search

        search = Toplevel(root)
        search.title("Lookup Records")

        window_height = 180
        window_width = 400

        screen_width = search.winfo_screenwidth()
        screen_height = search.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        search.geometry("{}x{}+{}+{}".format(window_width,
                        window_height, x_cordinate, y_cordinate))

        #search.iconbitmap('./DSC logo.ico')

        search_frame = LabelFrame(search, text="Enter the Company Name")
        search_frame.pack(padx=10, pady=10)

        search_entry = Entry(search_frame, font=("Helvetica", 18))
        search_entry.pack(pady=20, padx=20)

        search_button = Button(
            search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)

    def search_records():
        lookup_record = search_entry.get()
        final = []
        for i in datalist:
            if i[1] == lookup_record:
                final.append(i)

        search.destroy()
        for record in my_tree.get_children():
            my_tree.delete(record)

        global count
        count = 0

        for i in range(len(final)):
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(count, final[i][1], final[i][0]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(count, final[i][1], final[i][0]), tags=('oddrow',))
            count += 1

    def primary_color():
        primary_color = colorchooser.askcolor()[1]
        if primary_color:
            my_tree.tag_configure('evenrow', background=primary_color)

    def secondary_color():
        secondary_color = colorchooser.askcolor()[1]

        if secondary_color:
            my_tree.tag_configure('oddrow', background=secondary_color)

    def highlight_color():
        highlight_color = colorchooser.askcolor()[1]

        if highlight_color:
            style.map('Treeview', background=[('selected', highlight_color)])

    my_menu = Menu(root)
    root.config(menu=my_menu)

    option_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Primary Color", command=primary_color)
    option_menu.add_command(label="Secondary Color", command=secondary_color)
    option_menu.add_command(label="Highlight Color", command=highlight_color)
    option_menu.add_separator()
    option_menu.add_command(label="Exit", command=root.quit)

    search_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Search", menu=search_menu)

    search_menu.add_command(label="Reset", command=query_database)
    search_menu.add_command(label="Search", command=lookup_records)

    style = ttk.Style()

    style.theme_use('default')

    style.configure("Treeview",
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#D3D3D3")
    style.map('Treeview',
              background=[('selected', "#347083")])

    tree_frame = Frame(myFrame)
    tree_frame.pack(pady=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(
        tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ("S.no", "Company Name", "Company Symbol")

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("S.no", anchor=CENTER, width=35)
    my_tree.column("Company Name", anchor=W, width=700)
    my_tree.column("Company Symbol", anchor=W, width=105)

    my_tree.heading("#0", text="S.no", anchor=W)
    my_tree.heading("S.no", text="S.no", anchor=W)
    my_tree.heading("Company Name", text="Company Name", anchor=W)
    my_tree.heading("Company Symbol", text="Company Symbol", anchor=W)

    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    query_database()

    def select_record(e):
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')

    def update_record():
        selected = my_tree.focus()

        my_tree.delete(*my_tree.get_children())

    def create_table_again():

        c.execute()

    home = Button(myFrame, text="Home",  bg="#3b404e",   
                  relief=GROOVE, command=lambda: home_window(root))
    home.config(highlightbackground="#3b404e",
                highlightthickness=2, highlightcolor="#3b404e")
    home.pack(pady=25)

# -------------------------------------------------------------------------------------

# -------------------------------- Stock Detail Window ---------------------------------------


def stock_details_window(root):
    def value():
        tickerEnter
        dateEnter, highEnter, lowEnter, openEnter, closeEnter
        date_today = datetime.today()
        date_entered = datetime.strptime(dateEnter.get(), "%Y-%m-%d")
        if date_entered <= date_today:
            tickerval = tickerEnter.get()
            dateval = dateEnter.get()
            data_json = backend.daily_o_c(tickerval.upper(), dateval)
            highEnter.configure(text=data_json['high'])
            lowEnter.configure(text=data_json['low'])
            openEnter.configure(text=data_json['open'])
            closeEnter.configure(text=data_json['close'])
        else:
            tkinter.messagebox.showerror(
                title="Invalid Input", message="Date should be of format YYYY-MM-DD")

    myFrame.config(text="Stock Details")
    myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.57, anchor=CENTER)


    for child in myFrame.winfo_children():
        child.destroy()

    ticker = Label(myFrame, text="Stock Ticker:", relief=RAISED,  
                   bg="#3b404e", bd=0, font=("Calibri", 12), padx=90, pady=20)
    ticker.grid(row=1, column=0, padx=60, pady=5)

    date = Label(myFrame, text="Date:", relief=RAISED,  
                 bg="#3b404e", bd=0, font=("Calibri", 12))
    date.grid(row=2, column=0, padx=60, pady=5)

    tickerEnter = Entry(myFrame, highlightbackground="#3b404e",
                        bg="#3b404e", borderwidth=2, fg="white")
    tickerEnter.grid(row=1, column=1, padx=60, pady=5)

    dateEnter = Entry(myFrame, highlightbackground="#3b404e",
                      bg="#3b404e", borderwidth=2, fg="white")
    dateEnter.grid(row=2, column=1, padx=60, pady=5)

    search = Button(myFrame, text="Search",  bg="#3b404e",  
                    relief=GROOVE, borderwidth=2, command=lambda: value())
    search.grid(row=3, column=0, columnspan=3, padx=100, pady=20)
    search.config(highlightbackground="#3b404e",
                  highlightthickness=2, highlightcolor="#3b404e")

    high = Label(myFrame, text="High:", relief=RAISED,  
                 bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    high.grid(row=4, column=0, padx=60, pady=5)

    low = Label(myFrame, text="Low:", relief=RAISED,  
                bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    low.grid(row=5, column=0, padx=60, pady=5)

    open = Label(myFrame, text="Open:", relief=RAISED,  
                 bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    open.grid(row=6, column=0, padx=60, pady=5)

    close = Label(myFrame, text="Close:", relief=RAISED,  
                  bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    close.grid(row=7, column=0, padx=60, pady=5)

    highEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                      bg="#3b404e", borderwidth=2, fg="white")
    highEnter.grid(row=4, column=1, padx=80, pady=5)

    lowEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                     bg="#3b404e", borderwidth=2, fg="white")
    lowEnter.grid(row=5, column=1, padx=80, pady=5)

    openEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                      bg="#3b404e", borderwidth=2, fg="white")
    openEnter.grid(row=6, column=1, padx=80, pady=5)

    closeEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                       bg="#3b404e", borderwidth=2, fg="white")
    closeEnter.grid(row=7, column=1, padx=80, pady=5)

    home = Button(myFrame, text="Home",  bg="#3b404e",  
                  relief=GROOVE, borderwidth=2, command=lambda: home_window(root))
    home.grid(row=8, column=0, columnspan=2, padx=30, pady=20)
    home.config(highlightbackground="#3b404e",
                highlightthickness=2, highlightcolor="#3b404e")

# -------------------------------------------------------------------------------------

# -------------------------------- Crypto Detail Window ---------------------------------------


def crypto_details_window(root):
    myFrame.config(text="Crypto Details")
    myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.5, anchor=CENTER)


    for child in myFrame.winfo_children():
        child.destroy()

    def value():
        tickerEnter
        dateEnter, openEnter, closeEnter
        date_today = datetime.today()
        date_entered = datetime.strptime(dateEnter.get(), "%Y-%m-%d")
        if(date_entered <= date_today):
            tickerval = tickerEnter.get()
            dateval = dateEnter.get()
            data_json = backend.crypto_daily_o_c(tickerval.upper(), dateval)
            openEnter.configure(text=data_json['open'])
            closeEnter.configure(text=data_json['close'])
        else:
            tkinter.messagebox.showerror(
                title="Invalid Input", message="Date should be of format YYYY-MM-DD")

    ticker = Label(myFrame, text="Crypto Code:", relief=RAISED,  
                   bg="#3b404e", bd=0, font=("Calibri", 12), padx=90, pady=20)
    ticker.grid(row=0, column=0, padx=60, pady=5)

    date = Label(myFrame, text="Date:", relief=RAISED,  
                 bg="#3b404e", bd=0, font=("Calibri", 12))
    date.grid(row=1, column=0, padx=60, pady=5)

    tickerEnter = Entry(myFrame, highlightbackground="#3b404e",
                        bg="#3b404e", borderwidth=2, fg="white")
    tickerEnter.grid(row=0, column=1, padx=60, pady=5)

    dateEnter = Entry(myFrame, highlightbackground="#3b404e",
                      bg="#3b404e", borderwidth=2, fg="white")
    dateEnter.grid(row=1, column=1, padx=60, pady=5)

    search = Button(myFrame, text="Search",  bg="#3b404e",  
                    relief=GROOVE, borderwidth=2, command=lambda: value())
    search.grid(row=2, column=0, columnspan=2, padx=30, pady=20)
    search.config(highlightbackground="#3b404e",
                  highlightthickness=2, highlightcolor="#3b404e")

    open = Label(myFrame, text="Open:", relief=RAISED,  
                 bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    open.grid(row=3, column=0, padx=60, pady=5)

    close = Label(myFrame, text="Close:", relief=RAISED,  
                  bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    close.grid(row=4, column=0, padx=60, pady=5)

    openEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                      bg="#3b404e", borderwidth=2, fg="white")
    openEnter.grid(row=3, column=1, padx=80, pady=5)

    closeEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                       bg="#3b404e", borderwidth=2, fg="white")
    closeEnter.grid(row=4, column=1, padx=80, pady=5)

    home = Button(myFrame, text="Home",  bg="#3b404e",   
               relief=GROOVE,borderwidth=2, command=lambda: home_window(root))
    home.grid(row=7, column=0, columnspan=2, padx=30, pady=20)
    home.config(highlightbackground="#3b404e",
                highlightthickness=2, highlightcolor="#3b404e")

# -------------------------------------------------------------------------------------

# -------------------------------- Analysis Window ---------------------------------------


def plot_info_window(root):
    myFrame.config(text="Analysis")
    myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.6, anchor=CENTER)


    for child in myFrame.winfo_children():
        child.destroy()

    def value(tickerEnter, fromdateEnter, todateEnter):

        data = backend.stocks_aggregate(
            fromdateEnter.get(), todateEnter.get(), tickerEnter.get())

        plot = Button(myFrame, text="Plot",  bg="#3b404e",  
                      relief=GROOVE, borderwidth=2, command=lambda: plot_window(data, tickerEnter.get(), fromdateEnter.get(), todateEnter.get()))
        plot.grid(row=9, column=0, columnspan=2, padx=0, pady=20)
        plot.config(highlightbackground="#3b404e",
                    highlightthickness=2, highlightcolor="#3b404e")

        indicator1 = Button(myFrame, text="Support Resistance Indicator",  
                            bg="#3b404e", relief=GROOVE, borderwidth=2, command=lambda: support_resistance(data, tickerEnter.get(), fromdateEnter.get(), todateEnter.get()))
        indicator1.grid(row=10, column=0, columnspan=1, padx=0, pady=20)
        indicator1.config(highlightbackground="#3b404e",
                          highlightthickness=2, highlightcolor="#3b404e")

        indicator2 = Button(myFrame, text="Williams %R Indicator",  
                            bg="#3b404e", relief=GROOVE, borderwidth=2, command =  lambda: williams_window(data, tickerEnter.get(), fromdateEnter.get(), todateEnter.get()))
        indicator2.grid(row=10, column=1, columnspan=1, padx=0, pady=20)
        indicator2.config(highlightbackground="#3b404e",
                          highlightthickness=2, highlightcolor="#3b404e")

    ticker = Label(myFrame, text="Stock Ticker:", relief=RAISED,  
                   bg="#3b404e", bd=0, font=("Calibri", 12), padx=90, pady=20)
    ticker.grid(row=0, column=0, padx=60, pady=5)

    fromdate = Label(myFrame, text="From Date:", relief=RAISED,
                       bg="#3b404e", bd=0, font=("Calibri", 12))
    fromdate.grid(row=1, column=0, padx=60, pady=5)

    todate = Label(myFrame, text="To Date:", relief=RAISED,
                     bg="#3b404e", bd=0, font=("Calibri", 12))
    todate.grid(row=2, column=0, padx=60, pady=20)

    tickerEnter = Entry(myFrame, highlightbackground="#3b404e",
                        bg="#3b404e", borderwidth=2, fg="white")
    tickerEnter.grid(row=0, column=1, padx=60, pady=5)

    fromdateEnter = Entry(myFrame, highlightbackground="#3b404e",
                          bg="#3b404e", borderwidth=2, fg="white")
    fromdateEnter.grid(row=1, column=1, padx=60, pady=5)

    todateEnter = Entry(myFrame, highlightbackground="#3b404e",
                        bg="#3b404e", borderwidth=2, fg="white")
    todateEnter.grid(row=2, column=1, padx=60, pady=20)

    next = Button(myFrame, text="Next",  bg="#3b404e",    relief=GROOVE, borderwidth=2,
                  command=lambda: value(tickerEnter, fromdateEnter, todateEnter))
    next.grid(row=4, column=0, columnspan=2, padx=0, pady=5)
    next.config(highlightbackground="#3b404e",
                highlightthickness=2, highlightcolor="#3b404e")

    home = Button(myFrame, text="Home",  bg="#3b404e",   relief=GROOVE,
                  borderwidth=2, command=lambda: home_window(root))
    home.grid(row=5, column=0, columnspan=2, padx=0, pady=5)
    home.config(highlightbackground="#3b404e",
                highlightthickness=2, highlightcolor="#3b404e")
# -------------------------------------------------------------------------------------

# -------------------------------- Plot Window ---------------------------------------


def plot_window(data, tickerEnter, fromdateEnter, todateEnter):
    myFrame.config(text="Plot")
    myFrame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor=CENTER)
    for child in myFrame.winfo_children():
        child.destroy()

        
    def plotter(data1):
        plt.rc('xtick', labelsize=9) 
        plt.rc('ytick', labelsize=9) 
        fig, ax = plt.subplots()
        fig.set_size_inches(7.8, 4.3)
        
        candlestick_ohlc(ax, df.values, width=0.6,
                         colorup='green', colordown='red', alpha=0.8)
        date_format = mpl_dates.DateFormatter('%d %b %Y')
        ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig,
                                   master=myFrame)
        canvas.draw()

        canvas.get_tk_widget().pack()
        back = Button(myFrame, text="Back", bg="#3b404e",   relief=GROOVE,
                      borderwidth=2, command=lambda: plot_info_window(root))
        back.config(highlightbackground="#3b404e",
                    highlightthickness=2, highlightcolor="#3b404e")
        back.pack(pady=5)

        indicator1 = Button(myFrame, text="Support Resistance Indicator", bg="#3b404e",   relief=GROOVE,
                            borderwidth=2, command=lambda: support_resistance(data, tickerEnter, fromdateEnter, todateEnter))
        indicator1.config(highlightbackground="#3b404e",
                          highlightthickness=2, highlightcolor="#3b404e")
        indicator1.pack(pady=5)

        indicator2 = Button(myFrame, text="Williams %R Indicator",bg="#3b404e",   relief=GROOVE,
                borderwidth=2, command=lambda: williams_window(data, tickerEnter, fromdateEnter, todateEnter))
        indicator2.config(highlightbackground="#3b404e",
                        highlightthickness=2, highlightcolor="#3b404e")
        indicator2.pack(pady=5)

        toolbar = NavigationToolbar2Tk(canvas,
                                       myFrame)
        toolbar.update()

        canvas.get_tk_widget().pack()

    ticker = yfinance.Ticker(tickerEnter)
    df = ticker.history(interval="1d", start=fromdateEnter, end=todateEnter)
    df['Date'] = pd.to_datetime(df.index)
    df['Date'] = df['Date'].apply(mpl_dates.date2num)
    df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]

    plotter(df)

# -------------------------------- Support Resistance Window ---------------------------------------


def support_resistance(data, ticker_name, from_date, to_date):
    myFrame.config(text="Support Resistance")
    myFrame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor=CENTER)
    for child in myFrame.winfo_children():
        child.destroy()
    plt.rcParams['figure.figsize'] = [12, 7]
    plt.rc('font', size=14)
    ticker = yfinance.Ticker(ticker_name)
    df = ticker.history(interval="1d", start=from_date, end=to_date)
    df['Date'] = pd.to_datetime(df.index)
    df['Date'] = df['Date'].apply(mpl_dates.date2num)
    df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]

    def isSupport(df, i):
        support = df['Low'][i] < df['Low'][i-1] and df['Low'][i] < df['Low'][i +
                                                                             1] and df['Low'][i+1] < df['Low'][i+2] and df['Low'][i-1] < df['Low'][i-2]
        return support

    def isResistance(df, i):
        resistance = df['High'][i] > df['High'][i-1] and df['High'][i] > df['High'][i +
                                                                                    1] and df['High'][i+1] > df['High'][i+2] and df['High'][i-1] > df['High'][i-2]
        return resistance

    levels = []
    for i in range(2, df.shape[0]-2):
        if isSupport(df, i):
            levels.append((i, df['Low'][i]))
        elif isResistance(df, i):
            levels.append((i, df['High'][i]))

    s = np.mean(df['High'] - df['Low'])

    def isFarFromLevel(l):
        return np.sum([abs(l-x) < s for x in levels]) == 0

    levels = []
    for i in range(2, df.shape[0]-2):
        if isSupport(df, i):
            l = df['Low'][i]
            if isFarFromLevel(l):
                levels.append((i, l))
        elif isResistance(df, i):
            l = df['High'][i]
            if isFarFromLevel(l):
                levels.append((i, l))

    def plot_all():
        fig, ax = plt.subplots()
        fig.set_size_inches(7.8, 4.7)
        plt.rc('xtick', labelsize=9) 
        plt.rc('ytick', labelsize=9) 
        candlestick_ohlc(ax, df.values, width=0.6,
                         colorup='green', colordown='red', alpha=0.8)
        date_format = mpl_dates.DateFormatter('%d %b %Y')
        ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()
        fig.tight_layout()
        for level in levels:
            plt.hlines(level[1], xmin=df['Date'][level[0]],
                       xmax=max(df['Date']), colors='blue', linewidth = 1)

        canvas = FigureCanvasTkAgg(fig,
                                   master=myFrame)
        canvas.draw()

        canvas.get_tk_widget().pack()
        back = Button(myFrame, text="Back", bg="#3b404e",   relief=GROOVE,
                      borderwidth=2, command=lambda: plot_info_window(root))
        back.config(highlightbackground="#3b404e",
                    highlightthickness=2, highlightcolor="#3b404e")
        back.pack(pady=5)

        indicator1 = Button(myFrame, text="Turn off Indicator", bg="#3b404e",   relief=GROOVE,
                            borderwidth=2, command=lambda: plot_window(data, ticker_name, from_date, to_date))
        indicator1.config(highlightbackground="#3b404e",
                          highlightthickness=2, highlightcolor="#3b404e")
        indicator1.pack(pady=5)

        toolbar = NavigationToolbar2Tk(canvas,
                                       myFrame)
        toolbar.update()

        canvas.get_tk_widget().pack()

    plot_all()

# -----------------------------------Williams %R Window------------------------------------------------------------------------


def williams_window(data, ticker_name, from_date, to_date):
    myFrame.config(text="Williams_window")
    myFrame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor=CENTER)
    for child in myFrame.winfo_children():
        child.destroy()
    
    plt.rcParams['figure.figsize'] = [12, 7]
    plt.rc('font', size=14)
    def get_historical_data(ticker_name, from_date):
        api_key = '019c9fc7c4a94b279fe9b864b5ce8f7a'
        api_url = f'https://api.twelvedata.com/time_series?symbol={ticker_name}&interval=1day&outputsize=5000&apikey={api_key}'
        raw_df = requests.get(api_url).json()
        df = pd.DataFrame(raw_df['values']).iloc[::-1].set_index('datetime').astype(float)
        df = df[df.index >= from_date]
        df.index = pd.to_datetime(df.index)
        return df

    def get_wr(high, low, close, lookback):
            highh = high.rolling(lookback).max() 
            lowl = low.rolling(lookback).min()
            wr = -100 * ((highh - close) / (highh - lowl))
            return wr

    ticker = get_historical_data(ticker_name, from_date)

    ticker['wr_14'] = get_wr(ticker['high'], ticker['low'], ticker['close'], 14)
    ticker = ticker.dropna()


    def implement_wr_strategy(prices, wr):    
        buy_price = []
        sell_price = []
        wr_signal = []
        signal = 0

        for i in range(len(wr)):
            if wr[i-1] > -80 and wr[i] < -80:
                if signal != 1:
                    buy_price.append(prices[i])
                    sell_price.append(np.nan)
                    signal = 1
                    wr_signal.append(signal)
                else:
                    buy_price.append(np.nan)
                    sell_price.append(np.nan)
                    wr_signal.append(0)
            elif wr[i-1] < -20 and wr[i] > -20:
                if signal != -1:
                    buy_price.append(np.nan)
                    sell_price.append(prices[i])
                    signal = -1
                    wr_signal.append(signal)
                else:
                    buy_price.append(np.nan)
                    sell_price.append(np.nan)
                    wr_signal.append(0)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                wr_signal.append(0)
                
        return buy_price, sell_price, wr_signal

    buy_price, sell_price, wr_signal = implement_wr_strategy(ticker['close'], ticker['wr_14'])

    def plot_all():
        plt.rc('xtick', labelsize=9) 
        plt.rc('ytick', labelsize=9) 
        fig, (ax1,ax2) = plt.subplots(2,1)
        fig.set_size_inches(7.5, 4.8)
        ax1.plot(ticker['close'], linewidth = 2)
        ax1.plot(ticker.index, buy_price, marker = '^', markersize = 4, linewidth = 0, color = 'green', label = 'BUY SIGNAL')
        ax1.plot(ticker.index, sell_price, marker = 'v', markersize = 4, linewidth = 0, color = 'r', label = 'SELL SIGNAL')
        ax1.legend(prop={"size":8})
        ax1.set_title(ticker_name+' CLOSING PRICE', fontsize = 12)
        ax2.plot(ticker['wr_14'], color = 'orange', linewidth = 2)
        ax2.axhline(-20, linewidth = 1.5, linestyle = '--', color = 'grey')
        ax2.axhline(-80, linewidth = 1.5, linestyle = '--', color = 'grey')
        ax2.set_title(ticker_name+' WILLIAMS %R 14', fontsize = 12)
        plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

        canvas = FigureCanvasTkAgg(fig,
                                   master=myFrame)
        canvas.draw()

        canvas.get_tk_widget().pack()
        back = Button(myFrame, text="Back", bg="#3b404e",   relief=GROOVE,
                      borderwidth=2, command=lambda: plot_info_window(root))
        back.config(highlightbackground="#3b404e",
                    highlightthickness=2, highlightcolor="#3b404e")
        back.pack(pady=5)

        indicator1 = Button(myFrame, text="Turn off Indicator", bg="#3b404e",   relief=GROOVE,
                            borderwidth=2, command=lambda: plot_window(data, ticker_name, from_date, to_date))
        indicator1.config(highlightbackground="#3b404e",
                          highlightthickness=2, highlightcolor="#3b404e")
        indicator1.pack(pady=5)

        toolbar = NavigationToolbar2Tk(canvas,
                                       myFrame)
        toolbar.update()

        canvas.get_tk_widget().pack()

    plot_all()




root = Tk()
root.title("Stock Visualizer")
root.geometry("600x500")
root.resizable(0, 0)

window_height = 775
window_width = 900

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width,
              window_height, x_cordinate, y_cordinate))

bg = ImageTk.PhotoImage(Image.open("images/stock.png"))
myLabel = Label(root, image=bg)
myLabel.place(x=0, y=0, relwidth=1, relheight=1)

myFrame = LabelFrame(root, bg="#3b404e", text="Home Page",
                     bd=3,   padx=5, pady=5, labelanchor="n")
myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.7, anchor=CENTER)

home_window(root)

root.mainloop()
