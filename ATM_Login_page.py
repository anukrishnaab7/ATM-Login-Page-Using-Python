# ATM

import sqlite3
from tkinter import *
from tkinter import messagebox
import string

# LOGIN PAGE

root = Tk()
root.title('LOGIN PAGE')
root.geometry('1280x1080')

f = Frame(bg='grey', height=1080, width=1200)
f.place(x=40, y=10)

Label(f, text='PUNJAB NATIONAL BANK (PNB)', fg='white', bg='grey',
      font=('times new roman', 30, 'bold')).place(x=320, y=50)

Label(f, text='Welcome', fg='yellow', bg='grey',
      font=('times new roman', 30, 'bold')).place(x=520, y=100)

Label(f, text='Enter Phone No :', fg='white', bg='grey',
      font=('times new roman', 20, 'bold')).place(x=300, y=250)

Label(f, text='Enter PIN :', fg='white', bg='grey',
      font=('times new roman', 20, 'bold')).place(x=300, y=350)

Label(f, text='(Sign in for New user)', fg='white', bg='grey',
      font=('times new roman', 15, 'bold')).place(x=280, y=450)

entry1 = Entry(f, width=60, bg='white')
entry1.place(x=520, y=260)

entry2 = Entry(f, width=60, bg='white')
entry2.place(x=520, y=360)

conn = sqlite3.connect('ATM_Database.db')  # database login_info
cursor = conn.cursor()


# SIGN IN PAGE

def signin():
    root1 = Toplevel(root)
    root1.title('SIGN IN')
    root1.geometry('1280x1080')

    f1 = Frame(root1, bg='grey', height=1080, width=1200)
    f1.place(x=40, y=10)

    Label(f1, text='PUNJAB NATIONAL BANK (PNB)', fg='white', bg='grey',
          font=('times new roman', 30, 'bold')).place(x=320, y=50)

    Label(f1, text='Welcome', fg='white', bg='grey',
          font=('times new roman', 25, 'bold')).place(x=520, y=100)

    Label(f1, text='(All field should be mandatory filled. )', fg='yellow', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=100, y=180)

    # ENTER FIRST NAME

    Label(f1, text='First Name :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=100, y=250)
    en1 = Entry(f1, width=40, bg='white')
    en1.place(x=210, y=255)

    def check_first():

        s = en1.get()
        invalid_characters = set(string.punctuation)

        if any(char in invalid_characters for char in s):
            messagebox.showerror('Error', 'Invalid name')

        else:
            messagebox.showinfo('Valid', 'Continue.')
        signin()

    Button(f1, text='Check', fg='black', bg='white', font=('times new roman', 10, 'bold'),
           bd=3, width=5, command=check_first).place(x=460, y=250)

    # ENTER LAST NAME

    Label(f1, text='Last Name :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=590, y=250)
    en7 = Entry(f1, width=30, bg='white')
    en7.place(x=720, y=250)

    def check_last():

        s = en1.get()
        invalid_characters = set(string.punctuation)

        if any(char in invalid_characters for char in s):
            messagebox.showerror('Error', 'Invalid name')

        else:
            messagebox.showinfo('Valid', 'Continue.')
        signin()

    Button(f1, text='Check', fg='black', bg='white', font=('times new roman', 10, 'bold'),
           bd=3, width=5, command=check_last).place(x=910, y=245)

    # ENTER GENDER

    Label(f1, text='Gender :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=590, y=300)

    v = IntVar()

    Radiobutton(root1, text='MALE', bg="grey", variable=v, value=1).place(x=780, y=310)
    Radiobutton(root1, text='FEMALE', bg="grey", variable=v, value=2).place(x=840, y=310)
    Radiobutton(root1, text='OTHERS', bg="grey", variable=v, value=3).place(x=920, y=310)

    # ENTER DATE OF BIRTH

    Label(f1, text='Date of Birth :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=590, y=340)
    en2 = Entry(f1, width=40, bg='white')
    en2.place(x=720, y=345)

    # ENTER AGE

    Label(f1, text='AGE :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=100, y=320)
    en2 = Entry(f1, width=20, bg='white')
    en2.place(x=215, y=325)

    def check_age():

        if int(en2.get()) < 0:
            messagebox.showerror('Error', 'Incorrect age')

        else:
            messagebox.showinfo('Valid', 'Continue.')

    Button(f1, text='Check', fg='black', bg='white', font=('times new roman', 10, 'bold'),
           bd=3, width=5, command=check_age).place(x=460, y=320)

    # ENTER PHONE NO.

    Label(f1, text='Phone No :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=100, y=370)
    en3 = Entry(f1, width=30, bg='white')
    en3.place(x=215, y=375)

    def check_phone():

        y = cursor.execute("SELECT Phone FROM Sign_in_info")
        p = y.fetchall()
        ep = int(en3.get())
        n1 = 0

        for i in p:
            if n1 == 0:
                if ep == i[0]:
                    messagebox.showerror('Error', 'User already exists.')
                    signin()

            else:
                messagebox.showinfo('Done!', 'Valid Phone no.')

        n1 += 1

    Button(f1, text='Check', fg='black', bg='white', font=('times new roman', 10, 'bold'),
           bd=3, width=5, command=check_phone).place(x=460, y=370)

    # ENTER EMAIL-ID

    Label(f1, text='Email Id :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=590, y=395)
    en8 = Entry(f1, width=40, bg='white')
    en8.place(x=720, y=395)

    # ENTER ACC NO.

    Label(f1, text='Account No :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=590, y=440)
    en9 = Entry(f1, width=30, bg='white')
    en9.place(x=720, y=440)

    # ENTER BALANCE AMOUNT

    Label(f1, text='Balance Amount :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=100, y=440)
    en4 = Entry(f1, width=40, bg='white')
    en4.place(x=255, y=445)

    # ENTER PIN NO.

    Label(f1, text='Enter PIN :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=100, y=510)
    en5 = Entry(f1, width=20, bg='white')
    en5.place(x=225, y=510)

    def check_pin():

        if len(en5.get()) == 4:
            messagebox.showinfo('Done', 'Valid Pin')

        else:
            messagebox.showerror('Error.', 'Pin should have 4 digits.')
        signin()

    Button(f1, text='Check', fg='black', bg='white', font=('times new roman', 10, 'bold'),
           bd=3, width=5, command=check_pin).place(x=460, y=510)

    # ENTER PIN CONFIRMATION

    Label(f1, text='Confirm PIN :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=590, y=500)
    en6 = Entry(f1, width=20, bg='white')
    en6.place(x=720, y=505)

    def check():
        if en1.get() == "" or en2.get() == "":
            messagebox.showinfo('Error.', 'Name and Age field can not be empty !')
        elif en3.get() == "" or en4.get() == "":
            messagebox.showinfo('Error.', 'Phone no and Balance field can not be empty !')
        elif en5.get() == "" or en6.get() == "":
            messagebox.showinfo('Error.', 'Enter PIN and Confirm PIN field can not be empty !')
        elif en5.get() != en6.get():
            messagebox.showinfo('Error.', 'Incorrect PIN number')
        else:
            messagebox.showinfo('Sign in Completed.', 'Registration successful !')

    # CONNECTING TO SQLITE DATABASE

    def database():

        details = [(en1.get(), en7.get(), int(en2.get()), int(en3.get()), en8.get(),
                    int(en9.get()), int(en4.get()), int(en5.get()))]  # tuple format
        # print(details)

        cursor.execute('create table if not exists Sign_in_info (First_name text, Last_name text, '
                       'Age int, Phone int, Email text, Acc_No int, Balance int, Pin int )')
        # create table (student_info)

        cursor.executemany('insert into Sign_in_info values (?,?,?,?,?,?,?,?)', details)

    # SUBMIT BUTTON FOR SIGN IN PAGE

    b_s = Button(f1, text='SUBMIT', fg='black', bg='yellow', font=('times new roman', 15, 'bold'),
                 bd=3, width=10, command=check)
    b_s.place(x=380, y=620)

    # SIGN IN BUTTON FOR SIGN IN PAGE

    b_1 = Button(f1, text='SIGN IN', fg='black', bg='yellow', font=('times new roman', 15, 'bold'),
                 bd=3, width=10, command=database)
    b_1.place(x=680, y=620)


# HOME PAGE

def home_page():
    rt = Toplevel(root)
    rt.title('HOME PAGE')
    rt.geometry('1280x1080')

    frame = Frame(rt, bg='grey', height=1080, width=1200)
    frame.place(x=40, y=10)

    Label(frame, text='PUNJAB NATIONAL BANK (PNB)', fg='white', bg='grey',
          font=('times new roman', 30, 'bold')).place(x=320, y=50)

    Label(frame, text='Welcome', fg='white', bg='grey',
          font=('times new roman', 30, 'bold')).place(x=520, y=100)

    # TRANSACTION DETAILS

    Label(frame, text='SELECT TRANSACTION', fg='white', bg='grey',
          font=('times new roman', 25, 'bold')).place(x=410, y=240)

    # DEPOSIT BUTTON

    bt = Button(frame, text='DEPOSIT', fg='black', bg='yellow', font=('times new roman', 15, 'bold'),
                bd=3, width=20, command=deposit)
    bt.place(x=150, y=350)

    # CASH WITHDRAWAL BUTTON

    bt_1 = Button(frame, text='CASH WITHDRAWAL', fg='black', bg='yellow', font=('times new roman', 15, 'bold'),
                  bd=3, width=20, command=withdrawal)
    bt_1.place(x=800, y=350)

    # BALANCE INQUIRY BUTTON

    bt_2 = Button(frame, text='BALANCE INQUIRY', fg='black', bg='yellow', font=('times new roman', 15, 'bold'),
                  bd=3, width=20, command=balance)
    bt_2.place(x=150, y=440)

    # PIN CHANGE BUTTON

    bt_3 = Button(frame, text='PIN CHANGE', fg='black', bg='yellow', font=('times new roman', 15, 'bold'),
                  bd=3, width=20, command=pin)
    bt_3.place(x=800, y=440)


def home():
    # CHECK WHETHER INPUT PHONE NO. AND PIN NO. EXIST IN DATABASE

    y = cursor.execute("SELECT Phone FROM Sign_in_info")
    num = 0
    for i in y:

        if num == 0:
            if int(entry1.get()) == i[0]:

                x = cursor.execute("SELECT Pin FROM Sign_in_info where Phone = '%d' " % int(entry1.get()))

                for j in x:

                    if int(entry2.get()) == j[0]:
                        messagebox.showinfo('Success', 'Successfully login')

                        home_page()
                        num += 1

    else:

        if int(entry1.get()) != i[0]:
            messagebox.showerror('Error.', 'Login failed.')

# PIN CHANGE


pin1 = StringVar()


def pin():
    r_p = Toplevel(root)
    r_p.geometry('1280x1080')
    r_p.title('PIN CHANGE')

    frame_1 = Frame(r_p, bg='grey', height=420, width=720)
    frame_1.place(x=280, y=100)

    Label(frame_1, text='PUNJAB NATIONAL BANK (PNB)', fg='white', bg='grey',
          font=('times new roman', 20, 'bold')).place(x=150, y=50)

    Label(frame_1, text='PIN CHANGE', fg='white', bg='grey',
          font=('times new roman', 20, 'bold')).place(x=300, y=100)

    # ENTER EXISTING PASSWORD

    Label(frame_1, text='ENTER PIN :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=50, y=200)

    e_p1 = Entry(frame_1, width=40, bg='white')
    e_p1.place(x=190, y=205)

    # ENTER NEW PASSWORD

    Label(frame_1, text='ENTER NEW PASSWORD :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=50, y=250)

    e_p2 = Entry(frame_1, width=40, bg='white')
    e_p2.place(x=330, y=255)

    # CONFIRM NEW PASSWORD

    Label(frame_1, text='CONFIRM PASSWORD :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=50, y=300)

    e1 = Entry(frame_1, textvariable=pin1, width=40, bg='white')
    e1.place(x=330, y=300)

    def msg1():
        messagebox.showinfo('PIN changed.', 'Successful !')

        cursor.execute('update Sign_in_info set Pin = (?)  where Phone = (?)', (int(e1.get()), int(entry1.get())))

        conn.commit()
        conn.close()
#
    # NEW PASSWORD SUBMIT BUTTON

    bt_4 = Button(frame_1, text='SUBMIT', fg='black', bg='yellow', font=('times new roman', 15, 'bold'), bd=3,
                  width=10, command=msg1)
    bt_4.place(x=300, y=350)


# BALANCE INQUIRY

def balance():
    r_2 = Toplevel(root)
    r_2.geometry('1280x1080')
    r_2.title('BALANCE INQUIRY')

    f_1 = Frame(r_2, bg='grey', height=420, width=720)
    f_1.place(x=280, y=100)

    Label(f_1, text='PUNJAB NATIONAL BANK (PNB)', fg='white', bg='grey',
          font=('times new roman', 20, 'bold')).place(x=150, y=50)

    Label(f_1, text='Welcome', fg='yellow', bg='grey',
          font=('times new roman', 20, 'bold')).place(x=300, y=100)

    Label(f_1, text='CURRENT BALANCE :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=90, y=200)

# DISPLAY BALANCE AMOUNT

    balance_amount = StringVar()

    x = cursor.execute("SELECT Balance FROM Sign_in_info where Phone = '%d' " % int(entry1.get()))
    q = x.fetchall()

    for j in q:

        balance_amount.set(j[0])

        Label(f_1, textvariable=balance_amount, fg='black', bg='white',
              font=('times new roman', 15, 'bold'), width=20).place(x=260, y=250)

    bt_4 = Button(f_1, text='BACK', fg='black', bg='yellow', font=('times new roman', 15, 'bold'), bd=3,
                  width=10, command=home_page)
    bt_4.place(x=300, y=350)


# CASH WITHDRAWAL

def withdrawal():
    r_c = Toplevel(root)
    r_c.geometry('1280x1080')
    r_c.title('CASH WITHDRAWAL')

    f_c = Frame(r_c, bg='grey', height=420, width=720)
    f_c.place(x=280, y=100)

    Label(f_c, text='PUNJAB NATIONAL BANK (PNB)', fg='white', bg='grey',
          font=('times new roman', 20, 'bold')).place(x=150, y=50)

    Label(f_c, text='Welcome', fg='yellow', bg='grey',
          font=('times new roman', 20, 'bold')).place(x=300, y=100)

    Label(f_c, text='ENTER AMOUNT :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=90, y=200)

    e = Entry(f_c, width=40, bg='white')
    e.place(x=270, y=205)

    def mg():

        x = cursor.execute("SELECT Balance FROM Sign_in_info where Phone = '%d' " % int(entry1.get()))
        q = x.fetchall()

        a = q[0][0] - int(e.get())
        print(a)

        for i in q:

            if int(e.get()) > i[0]:
                messagebox.showerror('Transaction Failed.', 'Insufficient Balance !')

            else:
                l1 = (a, int(entry1.get()))

                cursor.execute("update Sign_in_info set Balance = '%d'  where Phone = '%d'" % l1)

                messagebox.showinfo('Transaction Processing', 'please wait !')

                conn.commit()
                conn.close()

    b_c = Button(f_c, text='OK', fg='yellow', bg='grey', font=('times new roman', 15, 'bold'),
                 bd=3, width=5, command=mg)
    b_c.place(x=300, y=300)


# CASH DEPOSIT

def deposit():
    r_d = Toplevel(root)
    r_d.geometry('1280x1080')
    r_d.title('CASH DEPOSIT')

    f_d = Frame(r_d, bg='grey', height=420, width=720)
    f_d.place(x=280, y=100)

    Label(f_d, text='PUNJAB NATIONAL BANK (PNB)', fg='white', bg='grey',
          font=('times new roman', 20, 'bold')).place(x=150, y=50)

    Label(f_d, text='Welcome', fg='yellow', bg='grey',
          font=('times new roman', 20, 'bold')).place(x=300, y=100)

    Label(f_d, text='ENTER AMOUNT :', fg='white', bg='grey',
          font=('times new roman', 15, 'bold')).place(x=90, y=200)

    ed = Entry(f_d, width=40, bg='white')
    ed.place(x=270, y=205)

    def mg_d():

        x = cursor.execute("SELECT Balance FROM Sign_in_info where Phone = '%d' " % int(entry1.get()))
        q = x.fetchall()

        a = q[0][0] + int(ed.get())

        if int(ed.get()) < 0:
            messagebox.showerror('Error.', 'Enter valid number.')

        else:
            l2 = (a, int(entry1.get()))

            cursor.execute("update Sign_in_info set Balance = '%d'  where Phone = '%d'" % l2)

            messagebox.showinfo('Please wait', 'Processing !')

            conn.commit()
            conn.close()

    b_d = Button(f_d, text='OK', fg='yellow', bg='grey', font=('times new roman', 15, 'bold'),
                 bd=3, width=5, command=mg_d)
    b_d.place(x=300, y=300)


b_home = Button(f, text='SIGN IN ', fg='black', bg='yellow', font=('times new roman', 15, 'bold'),
                bd=3, width=10, command=signin)
b_home.place(x=320, y=500)

b_home1 = Button(f, text='LOGIN ', fg='black', bg='yellow', font=('times new roman', 15, 'bold'),
                 bd=3, width=10, command=home)
b_home1.place(x=680, y=500)

mainloop()
