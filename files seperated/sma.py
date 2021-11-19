from tkinter import *
import tkinter
from PIL import ImageTk, Image
from tkinter import ttk
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

root = Tk()
root.title("Stock Visualizer")
root.geometry("600x500")
root.resizable(0, 0)

window_height = 800
window_width = 900

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width,
              window_height, x_cordinate, y_cordinate))

bg = ImageTk.PhotoImage(Image.open("images/0_mMD5SlIbFvgkGo3l.jpeg"))
myLabel = Label(root, image=bg)
myLabel.place(x=0, y=0, relwidth=1, relheight=1)

myFrame = LabelFrame(root, bg="#3b404e", text="Home Page",
                     bd=3, fg="white", padx=5, pady=5, labelanchor="n")
myFrame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.7, anchor=CENTER)

# ------------------------------------------------------------------------------------------------------------------


myFrame.config(text="Plot")
plt.rcParams['figure.figsize'] = [12, 7]
plt.rc('font', size=14)
nvda = yfinance.Ticker("AAPL")
df = nvda.history(period='1y')[['Open', 'High', 'Low', 'Close', 'Volume']]
df['SMA_10'] = df['Close'].rolling(window=10).mean()
df.ta.sma(close='close', length=5, append=True)
df.ta.sma(close='close', length=10, append=True)
df.ta.sma(close='close', length=20, append=True)
print(df)
moving_averages = ta.Strategy(
        name="SMA_5_10_20",
        ta=[
            {"kind": "sma", "length": 5},
            {"kind": "sma", "length": 10},
            {"kind": "sma", "length": 20}
        ]
    )
df.ta.cores = 0
df.ta.strategy(moving_averages, append=True)
df.ta.cores = 0
df.ta.strategy(moving_averages)
fig = go.Figure(data=[
        go.Candlestick(
            x=df.index,
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            increasing_line_color='#ff9900',
            decreasing_line_color='black',
            showlegend=False,
        ),
    ])
layout = go.Layout(
        plot_bgcolor='#efefef',
        font_family='Monospace',
        font_color='#000000',
        font_size=20,
        xaxis=dict(
            rangeslider=dict(
                visible=False
            ))
    )
fig.update_layout(layout)


# ------------------------------------------------------------------------------------------------------------------------------

canvas = FigureCanvasTkAgg(fig,
                             master=myFrame)
canvas.draw()

canvas.get_tk_widget().pack()

root.mainloop()