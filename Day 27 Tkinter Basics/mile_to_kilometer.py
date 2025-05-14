from tkinter import *

def convert():
    miles = round(float(miles_entry.get())*1.6, 2)
    km_label.config(text=f"{miles}")

root = Tk()
root.geometry("400x300")
root.title("Miles to Kilometer Convertor")

# Miles part
miles_entry = Entry()
miles_entry.grid(row=0, column=1)
Label(text="Miles").grid(row=0, column=2)

# Kilometer part
Label(text="is equal to").grid(row=1, column=0)
km_label = Label(text="0").grid(row=1, column=1)
Label(text="Km").grid(row=1, column=2)

# Creating the button to get km value corressponding km value
Button(text="Calculate", command=convert).grid(row=2, column=1)

root.mainloop()