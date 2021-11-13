from tkinter import *
import tkinter
from PIL import ImageTk, Image
from tkinter import ttk
import backend
from tkinter import messagebox
import webbrowser
from datetime import datetime


# -------------------------------- Home Window ---------------------------------------

def home_window(root):
    myFrame.config(text="Home Page")

    for child in myFrame.winfo_children():
        child.destroy()

    stock_index = Button(myFrame, text="Stock Index", fg="#FFFFFF", bg="#3b404e",
                         relief=GROOVE, borderwidth=2, command=lambda: stock_index_window(root))
    stock_index.config(highlightbackground="#3b404e",
                       highlightthickness=2, highlightcolor="#3b404e")
    stock_index.grid(row=0, padx=290, pady=10, sticky="nesw")

    crypto_index = Button(myFrame, text="Crypto Index", fg="#FFFFFF",
                          bg="#3b404e", relief=GROOVE, command=lambda:  crypto_index_window(root))
    crypto_index.config(highlightbackground="#3b404e",
                        highlightthickness=2, highlightcolor="#3b404e")
    crypto_index.grid(row=1, padx=290, pady=10, sticky="nesw")

    stock_details = Button(myFrame, text="Stock Details", fg="#FFFFFF",
                           bg="#3b404e", relief=GROOVE, command=stock_details_window)
    stock_details.config(highlightbackground="#3b404e",
                         highlightthickness=2, highlightcolor="#3b404e")
    stock_details.grid(row=2, padx=290, pady=10, sticky="nesw")

    crypto_details = Button(myFrame, text="Crypto Details", fg="#FFFFFF",
                            bg="#3b404e", relief=GROOVE, command=crypto_details_window)
    crypto_details.config(highlightbackground="#3b404e",
                          highlightthickness=2, highlightcolor="#3b404e")
    crypto_details.grid(row=3, padx=290, pady=10, sticky="nesw")


# -------------------------------------------------------------------------------------

# -------------------------------- Stock Index Window ---------------------------------------


def stock_index_window(root):
    myFrame.config(text="Home Page")
    datalist = backend.refresh()
    for child in myFrame.winfo_children():
        child.destroy()

    def query_database():
        for record in my_tree.get_children():
            my_tree.delete(record)

        global count
        count = 0

        for i in range(len(datalist)):
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

        search.iconbitmap('./DSC logo.ico')

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

    home = Button(myFrame, text="Home", fg="#FFFFFF", bg="#3b404e",
                  relief=GROOVE, command=lambda: home_window(root))
    home.config(highlightbackground="#3b404e",
                highlightthickness=2, highlightcolor="#3b404e")
    home.pack(pady=25)

# -------------------------------------------------------------------------------------


# -------------------------------- Crypto Index Window ---------------------------------------

def crypto_index_window(root):
    myFrame.config(text="Home Page")
    datalist = backend.crypto_refresh()
    for child in myFrame.winfo_children():
        child.destroy()

    def query_database():
        for record in my_tree.get_children():
            my_tree.delete(record)

        global count
        count = 0

        for i in range(len(datalist)):
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

        search.iconbitmap('./DSC logo.ico')

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

    home = Button(myFrame, text="Home", fg="#FFFFFF", bg="#3b404e",
                  relief=GROOVE, command=lambda: home_window(root))
    home.config(highlightbackground="#3b404e",
                highlightthickness=2, highlightcolor="#3b404e")
    home.pack(pady=25)

# -------------------------------------------------------------------------------------

# -------------------------------- Stock Detail Window ---------------------------------------


def stock_details_window():
    def value():
        tickerEnter
        dateEnter, highEnter, lowEnter, openEnter, closeEnter
        date_today = datetime.today()
        date_entered = datetime.strptime(dateEnter.get(), "%Y-%m-%d")
        if date_entered <= date_today :
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

    for child in myFrame.winfo_children():
        child.destroy()


    ticker = Label(myFrame, text="Stock Ticker:", relief=RAISED, fg="white",
                   bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=20)
    ticker.grid(row=0, column=0, padx=60, pady=5)

    date = Label(myFrame, text="Date:", relief=RAISED, fg="white",
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

    high = Label(myFrame, text="High:", relief=RAISED, fg="white",
                 bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    high.grid(row=3, column=0, padx=60, pady=5)

    low = Label(myFrame, text="Low:", relief=RAISED, fg="white",
                bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    low.grid(row=4, column=0, padx=60, pady=5)

    open = Label(myFrame, text="Open:", relief=RAISED, fg="white",
                 bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    open.grid(row=5, column=0, padx=60, pady=5)

    close = Label(myFrame, text="Close:", relief=RAISED, fg="white",
                  bg="#3b404e", bd=0, font=("Calibri", 12), padx=20, pady=10)
    close.grid(row=6, column=0, padx=60, pady=5)

    highEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                      bg="#3b404e", borderwidth=2, fg="white")
    highEnter.grid(row=3, column=1, padx=80, pady=5)

    lowEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                     bg="#3b404e", borderwidth=2, fg="white")
    lowEnter.grid(row=4, column=1, padx=80, pady=5)

    openEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                      bg="#3b404e", borderwidth=2, fg="white")
    openEnter.grid(row=5, column=1, padx=80, pady=5)

    closeEnter = Label(myFrame, text=" ", highlightbackground="#3b404e",
                       bg="#3b404e", borderwidth=2, fg="white")
    closeEnter.grid(row=6, column=1, padx=80, pady=5)

    home = Button(myFrame, text="Home",  bg="#3b404e",
                  relief=GROOVE, borderwidth=2, command = lambda : home_window(root))
    home.grid(row=7, column=0, columnspan=2, padx=30, pady=20)
    home.config(highlightbackground="#3b404e",
                highlightthickness=2, highlightcolor="#3b404e")

# -------------------------------------------------------------------------------------

# -------------------------------- Crypto Detail Window ---------------------------------------


def crypto_details_window():
    myFrame.config(text="Home Page")

    for child in myFrame.winfo_children():
        child.destroy()

# -------------------------------------------------------------------------------------


root = Tk()
root.title("Book Worm")
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

home_window(root)

root.mainloop()
