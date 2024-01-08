from tkinter import *
import customtkinter 


chisato= customtkinter.CTk()
chisato.title("FIND AND PRINT THE BIGGEST AMONG THEM")
chisato.geometry ("800x600")
chisato.config(bg="pink")
chisato.resizable(False, False)


# button to press if the three numbers are entered 
press_button= customtkinter.CTkButton(chisato, text='ENTER', text_color='black')
press_button.place(x=30, y=40)

# first number to enter
enter_number=customtkinter.CTkEntry(chisato, width=200, height=30)
enter_number.place(x= 100, y=100)

# second number to enter 
enter_number=customtkinter.CTkEntry(chisato, width=200, height=30)
enter_number.place(x= 500, y=100)

# third number to enter 
enter_number=customtkinter.CTkEntry(chisato, width=200, height=30)
enter_number.place(x= 300, y=100)



chisato.mainloop()
