from tkinter import *
import customtkinter 


chisato= customtkinter.CTk()
chisato.title("FIND AND PRINT THE BIGGEST AMONG THEM")
chisato.geometry ("800x600")
chisato.config(bg="pink")
chisato.resizable(False, False)

# defines which is the largest number among the three numbers entered
def press():
   first_number = float(enter_firstnumber.get())
   second_number = float(enter_secondnumber.get())
   third_number = float(enter_thirdnumber.get())

   if first_number > second_number and first_number > third_number:
      print(f'{first_number} is the largest')
   elif second_number > first_number and second_number > third_number:
      print(f'{second_number} is the largest')
   elif third_number > first_number and third_number > second_number:
      print(f'{third_number} is the largest')

   else: 
      print("NUMBERS CAN'T DEFINED, PLEASE TRY AGAIN")



# button to press if the three numbers are done entering 
press_button= customtkinter.CTkButton(chisato, text='ENTER', text_color='black', command=press)
press_button.place(x=30, y=40)

# first number to enter
enter_firstnumber=customtkinter.CTkEntry(chisato, width=200, height=30)
enter_firstnumber.place(x= 100, y=100)

# second number to enter 
enter_secondnumber=customtkinter.CTkEntry(chisato, width=200, height=30)
enter_secondnumber.place(x= 500, y=100)

# third number to enter 
enter_thirdnumber=customtkinter.CTkEntry(chisato, width=200, height=30)
enter_thirdnumber.place(x= 300, y=100)



chisato.mainloop()
