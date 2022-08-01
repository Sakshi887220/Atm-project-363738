'''
In this lecture we will make a interface same as that of an ATM. For the puropse we will use SQLite database. You will also learn about the hex color codes and we will be place geometry manager and we have place many buttons here and there.

We will use classes to make the interface. For every different screen we will make a frame and keep on adding thing in that frame.

First we have to create a database and a tabel in that database. Then we need to add an account in that table.

Now we will build our interface. That takes care of all the operation on the database.

'''
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

Courier = ('Courier',17,'bold')
class Atm:
   
        # Creating the login screen(2 buttons , 2 entry boxes and 2 labels)
        

        # Login button calls validate method of the same class.
        

        # placing all the buttons and entry boxes in the frame.
        
    # Taking all the details of a account in list.
    def fetch(self):
        

    def validate(self):
        
    # Creating the menu frame
    def menu(self):
        # There are total 7 buttons and commands associated with each of the button.
        self.frame = Frame(self.main,bg='#2193b0',width=650 ,height=600)
        main.geometry('800x600')
        self.user_info = Button(self.frame,text='Account Info',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.account_details)
        self.balance_enquiry = Button(self.frame,text='Balance Enquiry',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.check)
        self.deposit = Button(self.frame,text='Deposit',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.deposit)
        self.withdraw = Button(self.frame,text='Withdrawal',bg='#1f1c2c',fg='white',font=('Courier',10,'bold'),command=self.withdraw)

        self.last = Button(self.frame,text='Last Transaction',bg='#1f1c2c',fg='white',font=('Courier',8,'bold'),command=self.history)
        self.changePin = Button(self.frame,text='Change Pin',bg='#1f1c2c',fg='white',font=('Courier',8,'bold'),command=self.change)

        self.quit = Button(self.frame, text='Quit', bg='#1f1c2c', fg='white', font=('Courier', 10, 'bold'),command=self.main.destroy)

        # PLacing all the buttons and the frames.
        self.user_info.place(x=0,y=0,width=200,height=50)
        self.balance_enquiry.place(x=0,y=450,width=200,height=50)
        self.deposit.place(x=450,y=0,width=200,height=50)
        self.withdraw.place(x=450,y=450,width=200,height=50)
        self.last.place(x=0,y=240,width=130,height=50)
        self.changePin.place(x=530, y=240, width=130, height=50)
        self.quit.place(x=270,y=470,width=100,height=30)
        self.frame.pack()

    # Making all the commands associated with menu window
    def account_details(self):
        # Removing previous options
        self.entries()
        # there is an option for changing the pin and it require to make entry boxes and other stuff. If we call any other option first we have to get rid of changepin option for that we need to remove the button made by change pin option.
        self.remove_change_pin()

        # Fetching the data
        

    def check(self):
        # Removing previous options
        
        # Fetching the data
        
    def deposit(self):
        # Creating the interface for deposit
        

        

    def deposit_trans(self):
        # If field remains empty a error message must pop up
       
       

    def write_deposit(self):
        # Print the information of amount deposited on the menu window and save a text file about the same.
        

    # Withdraw is also same as deposit. Note that we have not taken in to account that what is the current amount in the acoount user can take any amount if withdraw is more than current. Balance will become negative.
    def withdraw(self):
        
    def with_trans(self):
        


    def last_with(self):
       

    # This function changes the PIN of the user.
    def change(self):
        # Making the interface and adding the required fields.
        self.entries()
        self.label = Label(self.frame,text='Change PIN',font=('Courier', 10, 'bold'))
        self.old = Entry(self.frame, bg='#FFFFFF', highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.new = Entry(self.frame, bg='#FFFFFF', highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.confirm = Entry(self.frame, bg='#FFFFFF', highlightcolor="#50A8B0", highlightthickness=2, highlightbackground="white")
        self.submit2 = Button(self.frame, text='Change', bg='#1f1c2c', fg='white', font=('Courier', 10, 'bold'),command = self.change_req)

        self.old.insert(0, 'Old password')
        self.new.insert(0, 'New password')
        self.confirm.insert(0, 'Confirm password')
        # Placing all the widgets in the menu frame
        self.label.place(x=180, y=180, width=300, height=100)
        self.old.place(x=230, y=300, width=180, height=20)
        self.new.place(x=230, y=330, width=180, height=20)
        self.confirm.place(x=230, y=360, width=180, height=20)
        self.submit2.place(x=230, y=390, width=180, height=20)

    def change_req(self):
        # If any one is empty return a error message
        # First condition whether the field is empty or not
        if(self.old.get()=='Old password' or self.new.get()=='New password' or self.confirm.get()=='Confirm password'):
            messagebox._show('Failed','Kindly fill all the details')
        else:
            self.fetch()
            self.details = self.conn.execute('Select name, password, acc_no, type, balance from atm where acc_no = ?',(self.ac,))
            for i in self.details:
                p = i[1]
            #Second condition if old password matches with current password
            if self.old.get() == p :

                # Third condition if new and confirmed are same or not
                if self.new.get() == self.confirm.get():
                    self.label = Label(self.frame,text='Updated Pin',font=('Courier', 10, 'bold'))
                    self.label.place(x=180, y=180, width=300, height=100)
                    self.conn.execute('Update atm set password = ? where acc_no=?', (self.new.get(), self.ac))
                    self.conn.commit()
                    self.remove_change_pin()
                    messagebox._show('Restart','Re-open your id')
                    main.destroy()
                else:
                    self.label = Label(self.frame,text='New Pin and Confirmed pin are \n different please enter the same PIN',font=('Courier', 10, 'bold'))
                    self.label.place(x=180, y=180, width=300, height=100)
            else:
                self.label = Label(self.frame,text='Older PIN does not match try again!!',font=('Courier', 10, 'bold'))
                self.label.place(x=180, y=180, width=300, height=100)                
    # Print the last transaction
    def history(self):
        

# Create the main window
main = Tk()
main.title('Bank')
window_height = 500
window_width = 900
# Return the number of pixels of the width of the screen of this widget in pixel.
screen_width = main.winfo_screenwidth()
# Return the number of pixels of the height of the screen of this widget in pixel.
screen_height = main.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
main.resizable(width=False, height=False)
# connecting to the database  
connection = sqlite3.connect("atm.db") 
  
# cursor  
crsr = connection.cursor() 
  
# SQL command to create a table in the database 
sql_command = """CREATE TABLE IF NOT EXISTS atm  (  
name text, 
password text, 
acc_no INTEGER PRIMARY KEY, 
type text, 
balance INTEGER);"""
  
# execute the statement 
crsr.execute(sql_command) 
  
# SQL command to insert the data in the table 
#sql_command = """INSERT INTO atm VALUES ("Arpit Bansal", "arpit123", 1298,"Savings", 23452);"""
crsr.execute(sql_command) 
  
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close() 
# Creating our ATM object
interface = Atm(main)
main.mainloop()
