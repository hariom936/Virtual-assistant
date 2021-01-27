from tkinter import *
from PIL import ImageTk,Image
import turtle
import hari

root=Tk()
root.title('hari')
root.geometry('1280x720')

img=ImageTk.PhotoImage(Image.open(r'im.png'))
panel=Label(root,image=img)
panel.pack(side='right',fill='both',expand='no')

compText=StringVar()
userText=StringVar()

userText.set('click Run hari to Give command')

userFrame=LabelFrame(root,text='User',font=('Black ops one',10,'bold'))
userFrame.pack(fill='both',expand='yes')

left=Message(userFrame,textvariable=userText,bg='#FF0000',fg='black')
left.config(font=("Century Gothic",24,'bold'))
left.pack(fill='both', expand='yes')

compFrame=LabelFrame(root,text="hari",font=('Black ops one',10,'bold'))
compFrame.pack(fill='both',expand='yes')

left2=Message(compFrame,textvariable=compText,bg='#FF0000',fg='black')
left2.config(font=("Century Gothic",24,'bold'))
left2.pack(fill='both', expand='yes')

compText.set('Hello I am Hari !!! what can i do for you sir ??')
btn1=Button(root,text='Run Hari',font=('Black ops one',10,'bold'),bg='#800000',fg='white',command=hari.main()).pack(fill='x',expand='no')
btn2=Button(root,text='Close',font=('Black ops one',10,'bold'),bg='#800000',fg='white',command=root.destroy).pack(fill='x',expand='no')


root.mainloop()


