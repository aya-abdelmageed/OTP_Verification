import os
from tkinter import *
from tkinter import messagebox
import random
import smtplib
from email.message import EmailMessage

#smtp
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_sender = 'youremail@gmail.com'
smtp_password = 'yourPassword'

#generate random OTP verification
otp =str(random.randint(100000, 999999))

#message 
# Set the subject and body of the email
subject = 'OTP Verification!'
body = f"Your OTP code is: {otp}"

em = EmailMessage()
em['Subject'] = subject
em.set_content(body)

#send email
def send_email():
    send.config(text="Resend")
    message = f'Subject: "OTP Verification"\n\n Your OTP code is: {otp}'
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls() # Secure the connection
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, email_receiver.get(), em.as_string())
        server.quit()
    messagebox.showinfo('Email Sent successfully', 'We have been sent your OTP code to your email.')


#verify the entered otp
def verify_otp():
    if otp_input.get() == otp:
        messagebox.showinfo('Success', 'OTP verification successful!')
        email_receiver.set("")
        otp_input.set("")
        send.config(text="Send OTP")
    else:
        messagebox.showerror('Error', 'Incorrect OTP code. Please try again.')
        otp_input.set("")
        

# window 
win = Tk()
win.title("OTP Verification!")
win.geometry('360x330')
win.configure(bg = "#ffffff")


#frames
line = Frame(win, width=400, height=5, bg="#ffffff")
line.grid(row=0, column=0)

body = Frame(win, width=400, height=400, bg="#ffffff")
body.grid(row=1, column=0)

#lables and inputs
title = Label(win,text="OTP Verification",font=("timesnewroman",18,"bold"),bg="#36454f",fg="#ffffff",relief=GROOVE)
title.place(x=100,y=30)

#label for  email
email = Label(win,text="Email ",bg="#ffffff",fg="#000000",font=("timesnewroman",12,"bold"),relief=RIDGE)
email.place(x=10,y=90)

#email input
email_receiver = StringVar()

Entry(win,textvariable = email_receiver ,font=("timesnewroman",12),bg="#ffffff",fg="#000000",relief=RAISED).place(x=100,y=90)

#send otp button
send = Button(win,text="Send OTP",fg="#ffffff",bg="#36454f",font=("timesnewroman",12,"bold"),relief=RAISED,command= send_email)
send.place(x=100,y=120)

#Label for OTP
Label(win,text="Enter OTP",bg="#ffffff",fg="#000000",font=("timesnewroman",12,"bold"),relief=RIDGE).place(x=10,y=170)

#input otp
otp_input = StringVar()
Entry(win,textvariable = otp_input,font=("timesnewroman",12),bg="#ffffff",fg="#000000",relief=RAISED,width=18).place(x=100,y=170)

#verify button
Button(win,text="Verify",fg="#ffffff",bg="#36454f",font=("timesnewroman",12,"bold"),relief=RAISED,command=verify_otp).place(x=100,y=200)



win.mainloop()