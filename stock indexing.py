from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser


root = Tk()
root.title('Stock Indexing')
root.geometry("500x500")

def primary_color():
	# Pick Color
	primary_color = colorchooser.askcolor()[1]

	# Update Treeview Color
	if primary_color:
		# Create Striped Row Tags
		my_tree.tag_configure('evenrow', background=primary_color)


def secondary_color():
	# Pick Color
	secondary_color = colorchooser.askcolor()[1]
	
	# Update Treeview Color
	if secondary_color:
		# Create Striped Row Tags
		my_tree.tag_configure('oddrow', background=secondary_color)
		

def highlight_color():
	# Pick Color
	highlight_color = colorchooser.askcolor()[1]

	#Update Treeview Color
	# Change Selected Color
	if highlight_color:
		style.map('Treeview',
			background=[('selected', highlight_color)])
# Add Menu
my_menu = Menu(root)
root.config(menu=my_menu)



# Configure our menu
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=option_menu)
# Drop down menu
option_menu.add_command(label="Primary Color", command=primary_color)
option_menu.add_command(label="Secondary Color", command=secondary_color)
option_menu.add_command(label="Highlight Color", command=highlight_color)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)

#Search Menu
search_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)
# Drop down menu
#search_menu.add_command(label="Search", command=lookup_records)

#search_menu.add_command(label="Reset", command=query_database)
search_menu.add_command(label="Search")
search_menu.add_command(label="Reset")
# Add Fake Data
'''
data = [
	["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
	["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
	["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
	["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]
	
]
'''

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Company Name", "Company Symbol")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Company Name", anchor=W, width=140)
my_tree.column("Company Symbol", anchor=W, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Company Name", text="Company Name", anchor=W)
my_tree.heading("Company Symbol", text="Company Symbol", anchor=W)


# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Select Record
def select_record(e):
	# Clear entry boxes
	

	# Grab record Number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	# outpus to entry boxes
	
# Update record
def update_record():
	# Grab the record number
	selected = my_tree.focus()
	# Update record
	#my_tree.item(selected, text="", values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get(),))

	# Clear entry boxes
	
	# Clear entry boxes
	
	# Clear The Treeview Table
	my_tree.delete(*my_tree.get_children())


def create_table_again():

	c.execute()
# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Stock List", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()