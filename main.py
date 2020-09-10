import tkinter as tk
from imgs import get_image
from logicHandler.file_reader import unpack
from tkinter.filedialog import askopenfilename
from logicHandler import email_sender


class EmailSender:
    def __init__(self,master):
        # GUI programming start
        # Initializing and configuring windows
        self.window = master
        self.window.title("Gmail client")
        self.window.configure(bg='#C6C6C6')
        self.window.rowconfigure([0,1],weight=1,minsize=100)
        self.window.columnconfigure(0,weight=1,minsize=1050)


        # Initializing Frames
        self.frm_base1 = tk.Frame(master=self.window,bg="#4285F4")
        self.frm_base2 = tk.Frame(master=self.window,bg="#C6C6C6")
        self.frm_base3 = tk.Frame(master=self.window,bg="#C6C6C6",relief="sunken",width=270)


        # Initializing widgets
        self.lbl_GmailHead1 = tk.Label(master=self.frm_base1,text=" Gmail",font=("Sans-serif",42),bg="#4285F4",fg="#F4B400")
        self.lbl_GmailHead2 = tk.Label(master=self.frm_base1,text="    Multiple Email Sender",font=("Sans-serif",14),bg="#4285F4",fg="#F4B400")
        self.lbl_to = tk.Label(master=self.frm_base2,text="To:",bg="#C6C6C6",font=("Sans-serif",14),fg="#0F9D58")
        self.lbl_subject = tk.Label(master=self.frm_base2,text="Subject:",bg="#C6C6C6",font=("Sans-serif",14),fg="#0F9D58")
        self.lbl_message = tk.Label(master=self.frm_base2,text="Message:",bg="#C6C6C6",font=("Sans-serif",14),fg="#0F9D58")
        self.lbl_logs = tk.Label(master=self.frm_base3,text="Logs",bg="#C6C6C6",font=("Sans-serif",14),fg="#0F9D58")
        self.btn_browse = tk.Button(master=self.frm_base2,text="BROWSE",bg="#C6C6C6",command=self.open_file)
        self.btn_send = tk.Button(master=self.frm_base2,text="SEND",bg="#C6C6C6",width=10,command=self.send_email)
        self.btn_browse['state'] = 'disabled'
        self.ent_to = tk.Entry(master=self.frm_base2,width=85)
        self.ent_subject = tk.Entry(master=self.frm_base2,width=100)
        self.txt_message = tk.Text(master=self.frm_base2,width=75,height=20)
        self.txt_logs = tk.Text(master=self.frm_base3,width=34,height=26)
        self.cnv_gmail_logo = tk.Canvas(master=self.frm_base1,width=150,height=100,highlightthickness=0,bg="#4285F4")
        self.img = get_image.getImageIcon()
        self.cnv_gmail_logo.create_image(75,50,image=self.img,anchor='center')

        self.v = tk.IntVar()
        self.rdo_single = tk.Radiobutton(master=self.frm_base2,text="Single",variable=self.v,value=1,bg="#C6C6C6",font=("Sans-serif",10),fg="#B23121",command=self.disable_btn)
        self.rdo_multiple = tk.Radiobutton(master=self.frm_base2,text="Multiple",variable=self.v,value=2,bg="#C6C6C6",font=("Sans-serif",10),fg="#B23121",command=self.disable_btn)

        # Layout
        # Placing Frame and widgets using grid method
        self.frm_base1.grid(row=0,column=0,sticky="ewn")
        self.frm_base2.grid(row=1,column=0,sticky="nsw")
        self.frm_base3.grid(row=1,column=0,sticky="nse")

        self.cnv_gmail_logo.grid(row=0,column=0,sticky="nw")
        self.lbl_GmailHead1.grid(row=0,column=1,sticky="nw")
        self.lbl_GmailHead2.grid(row=0,column=1,sticky="sw")
        self.rdo_single.grid(row=0,column=1,sticky="nse",padx=10,pady=10)
        self.rdo_multiple.grid(row=0,column=1,sticky="nse",padx=100,pady=10)
        self.lbl_to.grid(row=1,column=0,sticky="en",padx=10,pady=10)
        self.lbl_subject.grid(row=2,column=0,sticky="en",padx=10,pady=10)
        self.lbl_message.grid(row=3,column=0,sticky="en",padx=10,pady=10)
        self.ent_to.grid(row=1,column=1,padx=10,pady=10,sticky="nsw")
        self.btn_browse.grid(row=1,column=1,padx=10,pady=10,sticky="nse")
        self.ent_subject.grid(row=2,column=1,padx=10,pady=10,sticky="nsw")
        self.txt_message.grid(row=3,column=1,padx=10,pady=10,sticky="nsw")
        self.lbl_logs.grid(row=0,column=0,sticky='nw',padx=10,pady=8)
        self.txt_logs.grid(row=1,column=0,sticky='sew',padx=10,pady=10)
        self.btn_send.grid(row=4,column=1,sticky='ens',padx=10,pady=10)


        # Disabling editing in the logs text widget
        self.txt_logs.insert(tk.END,"---------------LOGS---------------")
        self.txt_logs.config(state='disable')


    def disable_btn(self):
        if self.v.get() == 1:
            self.btn_browse['state'] = "disabled"
            self.txt_logs.config(state='normal')
            self.txt_logs.insert(tk.END,"\nSingle Mode selected")
            self.txt_logs.config(state='disable')
            self.ent_to['state'] = 'normal'
            
        else:
            self.btn_browse['state'] = "active"
            self.txt_logs.config(state='normal')
            self.txt_logs.insert(tk.END,"\nMultiple Mode selected")
            self.txt_logs.config(state='disable')
            self.ent_to['state'] = 'disable'

    def open_file(self):
        self.filename = askopenfilename(filetype=[("Excel File","*.xlsx"),("csv Files","*.csv")])

        if not self.filename:
            return
            

        unpack.unpack_address(self.filename)

    def send_email(self):
        if self.v.get() == 1:
            to = self.ent_to.get()
            subject = self.ent_subject.get()
            msg = self.txt_message.get("0.0",tk.END)
            if not to.strip():
                self.txt_logs.config(state='normal')
                self.txt_logs.insert(tk.END,"\nEnter to email address")
                self.txt_logs.config(state='disable')
                return

            if not msg.strip():
                self.txt_logs.config(state='normal')
                self.txt_logs.insert(tk.END,"\nEnter the mail content")
                self.txt_logs.config(state='disable')
                return

            if email_sender.main():
                message = email_sender.create_message(to,subject,msg)
                result = email_sender.send_message(message)
                self.txt_logs.config(state='normal')
                self.txt_logs.insert(tk.END,f"\n{result}")
                self.txt_logs.config(state='disable')
            else:
                self.txt_logs.config(state='normal')
                self.txt_logs.insert(tk.END,"\nToken received")
                self.txt_logs.config(state='disable')


        elif self.v.get() == 2:
            if not unpack.address:
                self.txt_logs.config(state='normal')
                self.txt_logs.insert(tk.END,"\nAdd .csv or .xlsx file for emails")
                self.txt_logs.config(state='disable')
                return
            
            subject = self.ent_subject.get()
            msg = self.txt_message.get("0.0",tk.END)
            if not msg.strip():
                self.txt_logs.config(state='normal')
                self.txt_logs.insert(tk.END,"\nEnter the mail content")
                self.txt_logs.config(state='disable')
                return
            
            if email_sender.main():
                for e in unpack.address:
                    message = email_sender.create_message(e,subject,msg)
                    email_sender.send_message(message)
                self.txt_logs.config(state='normal')
                self.txt_logs.insert(tk.END,"\nMail sent")
                self.txt_logs.config(state='disable')
            else:
                self.txt_logs.config(state='normal')
                self.txt_logs.insert(tk.END,"\nToken received")
                self.txt_logs.config(state='disable')

        else:
            self.txt_logs.config(state='normal')
            self.txt_logs.insert(tk.END,"\nSELECT MODE")
            self.txt_logs.config(state='disable')



window = tk.Tk()
app = EmailSender(window)
window.mainloop()