import backend
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

def plot(data):

	fig = Figure(figsize = (5, 5),
				dpi = 100)

	plot1 = fig.add_subplot(111)

	plot1.plot(data)

	canvas = FigureCanvasTkAgg(fig,
							master = window)
	canvas.draw()

	canvas.get_tk_widget().pack()

	toolbar = NavigationToolbar2Tk(canvas,
								window)
	toolbar.update()

	canvas.get_tk_widget().pack()

window = Tk()

window.title('Plotting in Tkinter')

window.geometry("500x500")

data = backend.stocks_aggregate("2020-07-10","2021-07-10","AAPL")
close_vals = []

for i in data["results"]:
	close_vals.append(i['c'])

plot_button = Button(master = window,
					command = lambda: plot(close_vals),
					height = 2,
					width = 10,
					text = "Plot")

plot_button.pack()

window.mainloop()
