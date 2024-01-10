from tkinter import *
import customtkinter 
from PIL import Image, ImageTk

chisato= customtkinter.CTk()
chisato.title("WHICH IS BIGGEST NUMBER?")
chisato.geometry ("500x400")
chisato.config(bg='pink')
chisato.resizable(False, False)

taki= ('Britannic Bold', 45, 'bold')
inoue= ('Franklin Gothic Heavy', 30, 'bold')
chichi= ('Elephant', 30, 'bold')

# it opens the image
cutie_background = Image.open('computer background.png')

# resizing the image 
resized_image = cutie_background.resize((670, 550))  # Replace width and height with your desired dimensions

# displaying the background
cutie_background = ImageTk.PhotoImage(resized_image)
pretty_bg = customtkinter.CTkLabel(master=chisato, image=cutie_background, text='')
pretty_bg.pack()  


takichi_frame= customtkinter.CTkFrame(master=pretty_bg, width=400, height=300, fg_color='#00FFFF', corner_radius=0, border_width=0)
takichi_frame.place(relx= 0.5, rely= 0.5, anchor= CENTER)

# defines which is the largest number among the three numbers entered
def press():
   first_number = float(enter_firstnumber.get())
   second_number = float(enter_secondnumber.get())
   third_number = float(enter_thirdnumber.get())
   

   if first_number > second_number and first_number > third_number:
      print(f'{first_number} is the largest number')
      total_biggest= customtkinter.CTkLabel(master=pretty_bg, text=f'Largest Number: {enter_firstnumber.get()}', font= chichi, fg_color='#00FFFF')
      total_biggest.place(x= 85, y= 300)

   elif second_number > first_number and second_number > third_number:
      print(f'{second_number} is the highest number')
      total_largest= customtkinter.CTkLabel(master=pretty_bg, text=f'Highest Number: {enter_secondnumber.get()}', font=chichi, fg_color='#00FFFF')
      total_largest.place(x= 85, y=300)
   elif third_number > first_number and third_number > second_number:
      print(f'{third_number} is the biggest number')
      total_highest= customtkinter.CTkLabel(master=pretty_bg, text=f'Biggest Number: {enter_thirdnumber.get()}', font=chichi, fg_color='#00FFFF')
      total_highest.place(x= 85, y=300)

   




# first number to enter
enter_firstnumber=customtkinter.CTkEntry(chisato, width=100, height=50, font= taki, corner_radius=0, border_width=1, border_color='black')
enter_firstnumber.place(x= 70, y=150)

# second number to enter 
enter_secondnumber=customtkinter.CTkEntry(master=pretty_bg, width=100, height=50, font= taki, corner_radius=0, border_width=1, border_color='black')
enter_secondnumber.place(x= 330, y=150)

# third number to enter 
enter_thirdnumber=customtkinter.CTkEntry(master=pretty_bg, width=100, height=50, font=taki, corner_radius=0, border_width=1, border_color='black')
enter_thirdnumber.place(x= 200, y=150)

# button to press if the three numbers are done entering 
press_button= customtkinter.CTkButton(chisato, text='ENTER', text_color='black', command=press, font=inoue, corner_radius=0, border_width=1, border_color='black')
press_button.place(x=170, y=70)





chisato.mainloop()
