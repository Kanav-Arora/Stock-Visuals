import backend
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from matplotlib.figure import Figure
import pandas as pd
import tkinter as tk
from tkinter import ttk

root = tk.Tk()


dlf = ttk.Labelframe(root, text='Plot Area')
dlf.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)

t = np.arange(0.0,3.0,0.01)
df = pd.DataFrame({'t':t, 's':np.sin(2*np.pi*t)})

fig = Figure(figsize=(5,4), dpi=100)
ax = fig.add_subplot(111)

df.plot(x='t', y='s', ax=ax)


# start_date = '2015-01-01'
# end_date = '2016-12-31'

# fig, ax = plot.subplots(figsize=(16,9))

# ax.plot(data.loc[start_date:end_date, :].index, data.loc[start_date:end_date, 'MSFT'], label='Price')
# ax.plot(long_rolling.loc[start_date:end_date, :].index, long_rolling.loc[start_date:end_date, 'MSFT'], label = '100-days SMA')
# ax.plot(short_rolling.loc[start_date:end_date, :].index, short_rolling.loc[start_date:end_date, 'MSFT'], label = '20-days SMA')

# ax.legend(loc='best')
# ax.set_ylabel('Price in $')
# ax.xaxis.set_major_formatter(my_year_month_fmt)


canvas = FigureCanvasTkAgg(fig, master=dlf)
canvas.show()
canvas.get_tk_widget().grid(row=0, column=0)

root.mainloop()

