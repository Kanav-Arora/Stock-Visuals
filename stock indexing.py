from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
import backend

datalist = backend.refresh()
datalist.pop(0)
root = Tk()
root.title('Stock Indexing')
root.geometry("500x500")


def query_database():
    for record in my_tree.get_children():
        my_tree.delete(record)

    global count
    count = 0

    for i in range(len(datalist)):
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(
                datalist[i][1], datalist[i][0]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(
                datalist[i][1], datalist[i][0]), tags=('oddrow',))
        count += 1


def lookup_records():
    global search_entry, search

    search = Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")
    # search.iconbitmap('c:/gui/codemy.ico')

    search_frame = LabelFrame(search, text="Enter the Company Name")
    search_frame.pack(padx=10, pady=10)

    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(pady=20, padx=20)

    search_button = Button(search, text="Search Records",command=search_records)
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
                               values=(count,final[i][1], final[i][0]), tags=('evenrow',))
           else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(count,final[i][1], final[i][0]), tags=('oddrow',))
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
        style.map('Treeview',background=[('selected', highlight_color)])

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

tree_frame = Frame(root)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)

my_tree['columns'] = ("Company Name", "Company Symbol")

my_tree.column("#0", width=30, stretch=NO)
my_tree.column("Company Name", anchor=W, width=140)
my_tree.column("Company Symbol", anchor=W, width=140)

my_tree.heading("#0", text="S.no", anchor=W)
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

# Add Buttons
# button_frame = LabelFrame(root, text="Commands")
# button_frame.pack(fill="x", expand="yes", padx=20)

# update_button = Button(button_frame, text="Update Stock List", command=update_record)
# update_button.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()
