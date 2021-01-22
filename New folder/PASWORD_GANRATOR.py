from tkinter import*
import random, string
import pyperclip
#2 intialize Window
root = Tk()
root.geometry("400x400")
root.resizable(1,1)
root.title("PASSWORD GENRATOR")
Label(root, text = 'PASSWORD GENRATOR', font = 'Serif  16 bold underline'). pack()
Label(root, text = 'VIVEK- PASSWORD GENRATOR', font = 'arial 8 ').pack(side = BOTTOM)
#3 Select password length
pass_label =Label(root, text ='PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
lenght = Spinbox(root, from_ =8, to_=32, textvariable=pass_len, width = 16).pack()

pass_str = StringVar()
def Generator():
    password = ''

    for x in range (0,5):
        Password =""
        for y in range(pass_len.get()- 5):
            password = password +random.choice(string.ascii_uppercase+ string.ascii_lowercase + string.digits + string.punctuation)
            pass_str. set(password)
            
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 10)

Entry(root, textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO THE PASSWORD' , command = Copy_password ).pack(pady= 10)
root.mainloop()




