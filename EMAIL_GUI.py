import  tkinter as tk
import yagmail
import  sys

def send_email():
    send_e=e1.get()
    pass_e=e2.get()
    rec_e=e3.get()
    #print(send_e + pass_e + rec_e)
    yag_smtp_connection = yagmail.SMTP(user=send_e, password=pass_e, host='smtp.gmail.com')
    subject = 'Hello from Anurag ! '
    contents = ['Hello tom this is ANURAG speaking . Hows it going in JALANDHAR ?']
    # send the email
    yag_smtp_connection.send(rec_e, subject, contents)
    sys.exit()


window=tk.Tk()
window.geometry("400x200")

sender_email=tk.StringVar()
sender_password=tk.StringVar()
receiver_email=tk.StringVar()

label1=tk.Label(text="Sender Email Address")
label1.grid(row=0,column=0)

e1=tk.Entry(window,textvariable=sender_email)
e1.grid(row=0,column=1,padx=10,pady=10)


label2=tk.Label(text="Sender Password")
label2.grid(row=1,column=0)



e2=tk.Entry(window,textvariable=sender_password)
e2.grid(row=1,column=1,padx=10,pady=10)



label3=tk.Label(text="Receiver Email")
label3.grid(row=2,column=0)

e3=tk.Entry(window,textvariable=receiver_email)
e3.grid(row=2,column=1,padx=10,pady=10)


button_1=tk.Button(window,text="SEND",command=send_email)
button_1.grid(row=3,column=1)


window.mainloop()

