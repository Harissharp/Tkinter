#imports
import tkinter
import tkinter.messagebox

from tkinter import *
#defs
#makes sure thats the number is in range
def limit_num_check(len_or_hei,length_num,length_num2,length_num3,length_num4,height_num):
    if len_or_hei==True:#lengh field
        if length_num < 1 or length_num2 < 1 or length_num3 < 1 or length_num4 < 1:#checks minimum
            label = tkinter.Label(window, text="Larger length(s) Required (Min 1m)", fg='red').grid(row=11, column=1, sticky=S)
        if length_num > 25 or length_num2 > 25 or length_num3 > 25 or length_num4 > 25:#checks max
            label = tkinter.Label(window, text="Smaller length(s) Required (Max 25m) ", fg='red').grid(row=13, column=1, sticky=S)

    if len_or_hei==False:#hight
        if height_num < 2:
            label = tkinter.Label(window, text="Larger number (Min 2m)", fg='red').grid(row=15, column=1, sticky=S)
        if height_num > 6:
            label = tkinter.Label(window, text="Smaller number (Max 6m)", fg='red').grid(row=16, column=1, sticky=E)
# Calculation
def perform_calc():
   print(use_undercoat.get())
   paint_quality = paint_choice.get()
   try:
       area = int(height.get()) * int((length1.get() + length2.get() + Length3.get() + Length4.get()))
   except ValueError:
       tkinter.messagebox.showinfo("Input Error","Please enter all values and makes sure its numbers" )
   print_cost=0
   if paint_quality == 1:
      paint_cost = 1.90
   elif paint_quality == 2:
      paint_cost = 1.00
   else:
      paint_cost = 0.60

   if use_undercoat.get():
       paint_cost += 0.50

   total_paint_cost = paint_cost * area
   itemised_total = f"total area = {area} \n" # appears in the message box
   itemised_total += f"Paint cost = {total_paint_cost}" # appears in the message box

# Message box
   tkinter.messagebox.showinfo("Output", itemised_total)
   try:
       limit_num_check()
       limit_num_check()
   except:
       Label(window, text = "Values not in correct range, ").grid(row = 1,column=5)

window = Tk()
window.title("Interior Decorator")

# The different grids
Label(window, text = "Name").grid(row = 0)
name = Entry(window)
name.grid(row = 0, column = 1)

Label(window, text = "Height").grid(row = 1)
height = Entry(window)
height.grid(row = 1, column = 1)

Label(window, text = "Length 1").grid(row = 2)
length1 = Entry(window)
length1.grid(row = 2, column = 1)

Label(window, text = "Length 2").grid(row = 3)
length2 = Entry(window)
length2.grid(row = 3, column = 1)

Label(window, text = "Length 3").grid(row = 4)
Length3 = Entry(window)
Length3.grid(row = 4, column = 1)

Label(window, text = "Length 4").grid(row = 5)
Length4 = Entry(window)
Length4.grid(row = 5, column = 1)

# The options
paint_choice = IntVar()
paint_choice.set(2)
Radiobutton(window, text = "Luxury", variable = paint_choice, value = 1).grid(row = 4, column = 3)
Radiobutton(window, text = "Standard", variable = paint_choice, value = 2).grid(row = 3, column = 3)
Radiobutton(window, text = "Economy", variable = paint_choice, value = 3).grid(row = 2, column = 3,)


# Undercoat option
use_undercoat = IntVar()
undercoat = Checkbutton(window, text = "Undercoat", variable = use_undercoat)
undercoat.grid(row = 6, column = 3)


tkinter.Button(window, text ="Calculate", command = perform_calc).grid(row = 10, column = 1)
#tkinter.Button(window, text ="CHECK length", command = limit_num_check(True,length1,length2,Length3,Length4,height)).grid(row = 10, column = 1)
#tkinter.Button(window, text ="CHECK height", command = limit_num_check(False,length1,length2,Length3,Length4,height)).grid(row = 10, column = 1)
window.mainloop()
