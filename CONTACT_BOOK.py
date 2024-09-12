import tkinter as tk
from turtle import right
from CONTACT_BOOK_MAIN import _Database
import customtkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#*******GUI***************

window = customtkinter.CTk()
window.title("Contact Book")
window.geometry("600x505")
window.config(bg="#2a2b2a")
window.resizable(width=FALSE, height=FALSE)

font1= ('Arial',20,'bold')
font2= ('Arial',13,'bold')

#*******Frames**************

frame_up = customtkinter.CTkFrame(window, width=700, height=50,fg_color="#191a19")
frame_up.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

frame_down = customtkinter.CTkFrame(window, width=6700, height=200)
frame_down.grid(row=1, column=0, padx=0, pady=0, sticky="ew")


##******functions***********

def add_to_treeview():
    Contacts = _Database.fetch_contacts()
    tree.delete(*tree.get_children())
    for Contact in Contacts:
        tree.insert("",END, values = Contact)

def insert():
    First_Name = e_first_name.get()
    Last_Name  = e_last_name.get()
    Gender = variable1.get()
    Ph_Number = e_pnum.get()
    Email = e_email.get()
    if not (Ph_Number and First_Name and Last_Name and Gender and Email):
        messagebox.showerror("Error","Enter all fields.")
    elif _Database.contact_exists(Ph_Number):
        messagebox.showerror("Error","Phone Number already exists.")
    else:
        _Database.insert_contact(First_Name, Last_Name, Gender, Ph_Number, Email)
        add_to_treeview()
        clear()
        messagebox.showinfo("Success","Contact has been inserted.")

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    e_first_name.delete(0,END)
    e_last_name.delete(0,END)
    variable1.set("")
    e_pnum.delete(0,END)
    e_email.delete(0,END)


def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)["values"]
        clear()
        e_first_name.insert(0,row[0])
        e_last_name.insert(0,row[1])
        variable1.set(row[2])
        e_pnum.insert(0,row[3])
        e_email.insert(0,row[4])
    else:
        pass

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Error","Choose a contact to delete.")
    else:
        Ph_Number = e_pnum.get()
        _Database.delete_contact(Ph_Number)
        add_to_treeview()
        clear()
        messagebox.showinfo("Success","Contact has been deleted.")

def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Error","Choose a contact to update.")
    else:
        First_Name = e_first_name.get()
        Last_Name = e_last_name.get()
        Gender = variable1.get()
        Ph_Number = e_pnum.get()
        Email = e_email.get()
        _Database.update_contact(First_Name, Last_Name, Gender, Ph_Number, Email)
        add_to_treeview()
        clear()
        messagebox.showinfo("Success","Contact has been updated.")

def search_contact():
    Ph_Number = e_search.get().strip()
    if not Ph_Number:
        messagebox.showerror("Error", "Enter a phone number to search.")
    else:
        found = False
        for row in tree.get_children():
            row_values = tree.item(row)["values"]
            tree_ph_number = str(row_values[3]).strip()
            if Ph_Number == tree_ph_number:
                tree.selection_set(row)
                tree.focus(row)
                tree.see(row)
                found = True
                break

        if not found:
            messagebox.showinfo("Info", "No contact found with this phone number.")

style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview",font=font2, foreground="#fff",background="#000", fieldbackground="#313837")
style.map("Treeview", background=[("selected","#1A8F2D")])


tree = ttk.Treeview(window,height=15)
tree["columns"]=("First Name", "Last Name", "Gender", "Ph_Number", "Email")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("First Name",  width=140)
tree.column("Last Name", width=140)
tree.column("Gender", width=100)
tree.column("Ph_Number", width=140)
tree.column("Email", width=210)

tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Gender", text="Gender")
tree.heading("Ph_Number", text="Ph_Number")
tree.heading("Email", text="Email")

tree.place(x=10,y=300)

add_to_treeview()
tree.bind("<ButtonRelease>", display_data)


#********frame_up widget************

app_name  = customtkinter.CTkLabel(frame_up, text="Contact Book", height=1, font=font1, text_color = "#fff", padx=3, pady=9)
app_name.place(x=5,y=5)

#********frame_down widget************

lb_first_name = customtkinter.CTkLabel(frame_down, text="First Name *",  height=1, font=font2, bg_color="#2a2b2a", text_color="#fff", anchor=NW)
lb_first_name.place(x=10, y=27)
e_first_name = customtkinter.CTkEntry(frame_down, width=180, justify="left", text_color="#000", fg_color="#fff", border_color="#0C9295", border_width=2)
e_first_name.place(x=90, y=20)

lb_last_name = customtkinter.CTkLabel(frame_down, text="Last Name *", height=1, font=font2, bg_color="#2a2b2a", text_color="#fff",  anchor=NW)
lb_last_name.place(x=10, y=59)
e_last_name = customtkinter.CTkEntry(frame_down, width=180, justify="left", text_color="#000", fg_color="#fff", border_color="#0C9295", border_width=2)
e_last_name.place(x=90, y=52)

lb_gender = customtkinter.CTkLabel(frame_down, text="Gender *", height=1, font=font2, bg_color="#2a2b2a", text_color="#fff", anchor=NW)
lb_gender.place(x=10, y=90)
options=["Male","Female"]
variable1 = StringVar()
e_gender = customtkinter.CTkComboBox(frame_down, width=180, text_color="#000", fg_color="#fff", dropdown_hover_color="#0C9295", button_hover_color="#0C9295",border_color="#0C9295",variable=variable1,  values=options,state="readonly")
e_gender.set("")
e_gender.place(x=90, y=84)

lb_pnum = customtkinter.CTkLabel(frame_down, text="Ph Number *", height=1, font=font2, bg_color="#2a2b2a", text_color="#fff", anchor=NW)
lb_pnum.place(x=10, y=122)
e_pnum = customtkinter.CTkEntry(frame_down, width=180, justify="left", text_color="#000", fg_color="#fff", border_color="#0C9295", border_width=2)
e_pnum.place(x=90, y=116)

lb_email = customtkinter.CTkLabel(frame_down, text="Email *", height=1, font=font2, bg_color="#2a2b2a", text_color="#fff", anchor=NW)
lb_email.place(x=10, y=155)
e_email = customtkinter.CTkEntry(frame_down, width=180, justify="left", text_color="#000", fg_color="#fff", border_color="#0C9295", border_width=2)
e_email.place(x=90, y=148)

b_search = customtkinter.CTkButton(frame_down, text="Search",height=25, width=100, text_color="#fff", fg_color="#2a2b2a", hover_color="#FF5002", bg_color="#2a2b2a",border_color="#F15704", border_width=2, corner_radius=15, cursor="hand2", font=font2, command=search_contact)
b_search.place(x=300, y=21)
e_search = customtkinter.CTkEntry(frame_down, width=180, justify="left", font=("Ivy",11), text_color="#000", fg_color="#fff", border_color="#0C9295", border_width=2)
e_search.place(x=410, y=20)

b_clear = customtkinter.CTkButton(frame_down, text="Clear",height=25, width=100, text_color="#fff", fg_color="#2a2b2a", hover_color="#FF5002", bg_color="#2a2b2a",border_color="#F15704", border_width=2, corner_radius=15, cursor="hand2", font=font2, command=clear)
b_clear.place(x=300, y=60)

b_add = customtkinter.CTkButton(frame_down, text="Add",height=25, width=100, text_color="#fff", fg_color="#05A312", hover_color="#00850B", bg_color="#2a2b2a",corner_radius=15, cursor="hand2", font=font2, command=insert)
b_add.place(x=485, y=60)

b_update = customtkinter.CTkButton(frame_down, text="Update",height=25, width=100, text_color="#fff", fg_color="#2a2b2a", hover_color="#FF5002", bg_color="#2a2b2a",corner_radius=15,border_color="#F15704", border_width=2, cursor="hand2", font=font2, command=update)
b_update.place(x=485, y=98)

b_delete = customtkinter.CTkButton(frame_down, text="Delete",height=25, width=100, text_color="#fff", fg_color="#E40404", hover_color="#AE0000", bg_color="#2a2b2a",corner_radius=15,border_color="#E40404", border_width=2, cursor="hand2", font=font2, command=delete)
b_delete.place(x=485, y=136)

window.mainloop()