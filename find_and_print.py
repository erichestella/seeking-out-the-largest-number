from tkinter import *
import customtkinter 
from tkinter import messagebox 

chisato= customtkinter.CTk()
chisato.title("FIND AND PRINT THE BIGGEST AMONG THEM")
chisato.geometry ("400x300")
chisato.config(bg="pink")
chisato.resizable(False, False)

# defines which is the largest number among the three numbers entered
def press():
   first_number = float(enter_firstnumber.get())
   second_number = float(enter_secondnumber.get())
   third_number = float(enter_thirdnumber.get())
   

   if first_number > second_number and first_number > third_number:
      print(f'{first_number} is the largest number')
   elif second_number > first_number and second_number > third_number:
      print(f'{second_number} is the highest numebr')
   elif third_number > first_number and third_number > second_number:
      print(f'{third_number} is the biggest numeber')





# button to press if the three numbers are done entering 
press_button= customtkinter.CTkButton(chisato, text='ENTER', text_color='black', command=press)
press_button.place(x=120, y=40)

# first number to enter
enter_firstnumber=customtkinter.CTkEntry(chisato, width=100, height=50)
enter_firstnumber.place(x= 20, y=150)

# second number to enter 
enter_secondnumber=customtkinter.CTkEntry(chisato, width=100, height=50)
enter_secondnumber.place(x= 270, y=150)

# third number to enter 
enter_thirdnumber=customtkinter.CTkEntry(chisato, width=100, height=50)
enter_thirdnumber.place(x= 150, y=150)



chisato.mainloop()
