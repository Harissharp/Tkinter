#imports
import tkinter
import tkinter.messagebox

from tkinter import *
#defs
#makes sure thats the number is in range
def email_check():
    email.get()
    if email.find("@")<0:
        tkinter.messagebox.showinfo("Email Error","Please enter an actual email" )
def limit_num_check():
        if length1.get() < 1 or length2.get() < 1 or Length3.get() < 1 or Length4.get() < 1:#checks minimum
            label = tkinter.Label(window, text="Larger length(s) Required (Min 1m)", fg='red').grid(row=11, column=1, sticky=S)
        if length1.get() > 25 or length2.get() > 25 or Length3.get() > 25 or Length4.get() > 25:#checks max
            label = tkinter.Label(window, text="Smaller length(s) Required (Max 25m) ", fg='red').grid(row=13, column=1, sticky=S)#
        if height.get() < 2:
            label = tkinter.Label(window, text="Larger number (Min 2m)", fg='red').grid(row=15, column=1, sticky=S)
        if height.get() > 6:
            label = tkinter.Label(window, text="Smaller number (Max 6m)", fg='red').grid(row=16, column=1, sticky=E)
# Calculation
#checking the ISBN 1st
def perform_calc():
   try:
       area = int(height.get()) * int((length1.get() + length2.get() + Length3.get() + Length4.get()))
   except ValueError:
       tkinter.messagebox.showinfo("Input Error","Please enter all values and makes sure its numbers" )
   print_cost=0
   if paint_choice == 1:
      paint_cost = 1.90
   elif paint_choice == 2:
      paint_cost = 1.00
   else:
      paint_cost = 0.60

   if use_undercoat.get():
       paint_cost += 0.50
   try:
       limit_num_check()
   except:
       Label(window, text = "Values not in correct range ").grid(row = 1,column=5)
       error=True
   try:
       email_check()
   except:
       error=True
   if error==False:
       total_paint_cost = paint_cost * area
       itemised_total = f"total area = {area} \n" # appears in the message box
       itemised_total += f"Paint cost = {total_paint_cost}" # appears in the message box
       # Message box
       tkinter.messagebox.showinfo("Output", itemised_total)



#ISBN checker (check digit)
def ISBN_check():
   ISBN=ISBN_v.get()
   ISBN=str(ISBN)
   if len(ISBN)!=10:
        tkinter.messagebox.showinfo("ISBN Error","the ISBN value entered is not 10digits")
   try:#making sure its a number( could cause errors else wise)
       ISBN=int(ISBN)
   except:
       tkinter.messagebox.showinfo("ISBN Error","Please enter a number into the field")
   count=0#count for going through ISBN
   val=1#count for multiplying
   total=0#keeps track of numbers added
   while count!=9:                             #while loop for the "Q*1 + R*2 + S*3 + T*4 + U*5 + V*6 + W*7 + X*8 + Y*9" part of pesudocode
        temp_data=ISBN[count]                   #retives  value from ISBN
        #print("----------"+temp_data)                                      #logic testing
        temp_data=int(temp_data)*int(val)       #multiplies the select of ISBN to the var(secondary count)
        total=+total+int(temp_data)             #adds data to total
        #print(">>>>>>>>>>>>>>>"+str(total))                                 #logic testing
        count+=1
        val+=1
        #print(count)
        #print("==================="+str(val))
   count=9#10th index set to avoid system fails
   temp_data=ISBN[count]#retrives the 10th digit
   total=total%11  #mod11
   if int(total) == int(temp_data):# if it is the check digit....
        #print("Vaild ISBN")
        return True
   else:#if its not the check digit.....
        #print("not valid")
        #print(str(temp_data)+"////"+str(total))  #for logic checking
        return False
window = Tk()
window.title("Interior Decorator")

# The different grids
Label(window, text = "Name").grid(row = 0)#Name box
name = Entry(window)
name.grid(row = 0, column = 1)
#email
Label(window, text = "Email").grid(row = 1)
email = Entry(window)
email.grid(row = 1, column = 1)

Label(window, text = "Height").grid(row = 2)#Height Box
height = Entry(window)
height.grid(row = 2, column = 1)

Label(window, text = "Length 1").grid(row = 3)#Length Box
length1 = Entry(window)
length1.grid(row = 3, column = 1)

Label(window, text = "Length 2").grid(row = 4)#Length2 Box
length2 = Entry(window)
length2.grid(row = 4, column = 1)

Label(window, text = "Length 3").grid(row = 5)#Length3 Box
Length3 = Entry(window)
Length3.grid(row = 5, column = 1)

Label(window, text = "Length 4").grid(row = 6)#Length4 Box
Length4 = Entry(window)
Length4.grid(row = 6, column = 1)

Label(window, text = "ISBN 10 Code").grid(row = 0,column =3)#ISBN Box
ISBN_v = Entry(window)
ISBN_v.grid(row = 0, column = 4)
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
#                             TEXT                    Def                     position
tkinter.Button(window, text ="Check ISBN",command = ISBN_check).grid(row = 10, column = 2)
#tkinter.Button(window, text ="CHECK length", command = limit_num_check(True,length1,length2,Length3,Length4,height)).grid(row = 10, column = 1)
#tkinter.Button(window, text ="CHECK height", command = limit_num_check(False,length1,length2,Length3,Length4,height)).grid(row = 10, column = 1)
window.mainloop()


