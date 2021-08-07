# Nama        : Lim Jia Shiu
# Tingkatan   : 3 RED
# Tahun       : 2021

# import tkinter and other python features from module
import tkinter as tk
from tkinter import*
from tkinter.ttk import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from datetime import datetime
from tkinter import filedialog
import webbrowser
from pathlib import Path
from PIL import Image

def gopath(path: str) -> Path:   #determine correct path for every file
	return  Path("./assets") / Path(path)

# Procedure moreinfo()
def moreinfo():
    window3=tk.Toplevel(window)
    window3.title ("Introduction to Home Loan")#Set the title
    window3.geometry ("640x690")#Set the window size
    window3.maxsize (640,690)
    window3.configure (bg='floral white')
    window3.attributes('-alpha', 0.93)#Set the window background to be a little transparent
    
    title = tk.Label(window3, text = ('Home Loan in Malaysia') , font = ('Milkyroad', 20,"underline"), background="floral white", foreground="midnight blue")
    title.place(x=170, y=10)#Label and place the title
    
    photo6 = tk.PhotoImage (file = gopath("Picture6.png"))#Insert a picture
    lblgambar6 = tk.Label (window3, image= photo6, relief ="flat", borderwidth=2)
    lblgambar6.place (x=440, y=60, width=180, height=180)
    
    T = Text( window3, height = 9, width = 58)#Create a textbox widget
    T.configure(font = ('Bahnschrift Light Condensed',12), selectbackground="yellow",selectforeground="black")
    T.place(x=10,y=65)
    Subtitle1=("Home Loan Types")
    Type_of_home_loan=("\n\nIn Malaysia, there are two types of basic home loans available for interested home owners.")
    Sentences2=("There is the fixed term loan which involves you paying a fixed sum of money each month.")
    Sentences3=("The others one is the flexi-loan, which as the name suggests, offers you the flexibility of reducing your loan interest.")
    Sentences3b=("The customer ties up a Current Account to the loan and the loan amount is deducted as scheduled while additional monies will be used to pay for the principal amount. ")
    
    T.insert(tk.END,Subtitle1+Type_of_home_loan+Sentences2+Sentences3+Sentences3b)
    T.config(state="disabled")#Insert text into the textbox widget
    
    T2 = Text( window3, height = 7, width = 59)
    T2.configure(font = ('Bahnschrift Light Condensed',12), selectbackground="yellow",selectforeground="black")
    T2.place(x=200,y=300)
    
    Subtitle2=("Available Loan Amount")
    Sentences4=("\n\nThe amount that the bank is willing to loan to you varies from bank to bank. ")
    Sentences5a=("Usually the highest amount that bank will offer is 90% of property’s price thus the remaining 10% will have to come out of your own pockets. ")
    Sentences5b=("Seek for the bank that offers you a higher margin if you do not have sufficient cash flow to put up on your house. ")

    
    T2.insert(tk.END,Subtitle2+Sentences4+Sentences5a+Sentences5b)
    T2.config(state="disabled")
    
    photo7 = tk.PhotoImage (file = gopath("Picture7.png"))
    lblgambar7 = tk.Label (window3, image= photo7, relief ="flat", borderwidth=2)
    lblgambar7.place (x=10, y=300, width=180, height=180)
    
    T3 = Text( window3, height = 9, width = 59)
    T3.configure(font = ('Bahnschrift Light Condensed',12), selectbackground="yellow",selectforeground="black")
    T3.place(x=10,y=490)
    
    Subtitle3=("Terms & Conditions")
    Sentences6=("\n\nAlways read carefully over the contract before agreeing to take up the loan.")
    Sentences7=("The two most vital deciding factors when looking for a home loan are the interest rates and lock-in period.")
    Sentences8=("It goes without saying that interest rates are the killer that adds more burdens to loans which is why you should always choose the bank that can offer you the lowest interest rate.")
    Sentences9=("Mortgage loans are no small amount and just a little hike in interest rate could mean a big difference in your monthly repayments.")
    
    T3.insert(tk.END,Subtitle3+Sentences6+Sentences7+Sentences8+Sentences9)
    T3.config(state="disabled")
    
    photo8 = tk.PhotoImage (file = gopath("Picture9.png"))
    lblgambar8 = tk.Label (window3, image= photo8, relief ="flat", borderwidth=2)
    lblgambar8.place (x=450, y=490, width=180, height=180)
    
    window3.mainloop()
    


def usermanual():
    window2=tk.Toplevel(window)#create a window
    window2.title ("User Manual🧾🖨")
    window2.geometry ("630x700")
    window2.maxsize (630,700)
    window2.configure (bg='azure')
    window2.attributes('-alpha', 0.93)
    
    title =tk.Label(window2, text = ('How to Use This System?') , font = ('Milkyroad', 20,"underline"), background="azure", foreground="midnight blue")
    title.place(x=170, y=10)
    
    T = scrolledtext.ScrolledText(window2, wrap=WORD , width = 83, height = 13, font =('Bahnschrift Light Condensed',12), selectbackground="yellow",selectforeground="black")
    T.place (x =10, y= 65)

    Fact=("Welcome to our home loan calculator system!\n\nJust follow the steps below:\n\n")
    Step1=("1.Please enter the Property Asset Value (RM)💰 , Down Payment (%)💸 , Rate (%)💎  and Year📆 in number or float form. If not, system will ask you to refill again.")
    Step2=("\n2.After fill in all the informations, click the '📝 Calculate' button. If you are mistaken when fill in\n the information, feel free to click the '↷ Reset' button to clear all the data.")
    Step3=("\n3.The result will appear in the scrolledtext below.")
    Step4=("\n4.You can also export this result too by clicking the '🧾🖨🖥  Export as txt' button.  The txt file will save into your device at the same folder (location) of your python file.")
    Step5=("\n\nOthers:")
    Step6=("\n·Please note that when this system comes to next user, the result of last user will be cleared!")
    Step7=("\n·Please enter the data correctly to ensure the system work well.")
    Step8=("\n·All right reserved by jiashiuuuuu 2021")
    Step9=("\n\nThank you! Enjoy~")
    formula=("\n\nList of formula used:\nTotal month = year*12\nRate per month = rate/100/12\nMonthlyRepayment = Loan*(Rate per month/(1-((1+Rate per month)**-Total period)))")
    formula2=("\nInterest = Balance*Rate per month\nPrinciple = Monthly Repayment-Interest\nBalance = Balance-Principle")
    T.insert(tk.END, Fact + Step1+Step2+Step3+Step4+Step5+Step6+Step7+Step8+formula+formula2+Step9)
    T.config(state="disabled")
    
    photo11 = tk.PhotoImage (file = gopath("Picture11.png"))
    lblgambar10 = tk.Label (window2, image= photo11, relief ="sunken", anchor="center")
    lblgambar10.place (x=30, y=340, width=540, height=323)
   
    window2.mainloop()
    
def txt():
    import os
    thepath = filedialog.askdirectory(title='choose the place you want to save your txt')
    if os.path.exists(os.path.join(thepath,'Home Loan Receipt.txt')):  #error handling 
      try: 
       os.remove(os.path.join(thepath,'Home Loan Receipt.txt')) #delete the file if the file is exist 
      except: 
       if PermissionError(): 
        messagebox.showerror('File in use','The action cant be completed because the previous version txt is open in another app\n\nClose the file and try again later.') 
       else: 
        messagebox.showerror('Sorry','An unexpected error has occurred and we fail to export txt\nYou may contact jiashiuuu for futher help') 
       return 
    messagebox.showinfo('Done',["Your txt file was exported to "+str(thepath)])
    with open(os.path.join(thepath,'Home Loan Receipt.txt'), 'w') as f:
        receipt.configure(state='normal')
        cur_inp = receipt.get("1.0",END)
        f.write(cur_inp)
        receipt.configure(state='disabled')
        f.close()
        reset()

def cal( Loan, rate, year):
    Rate_per_month = rate/100/12
    Total_period = year*12
    MonthlyRepayment = Loan*(Rate_per_month/(1-((1+Rate_per_month)**-Total_period)))
    Balance = Loan
    Principle = 0.00
    Interest = 0.00
    TotalPrinciple = 0.00
    TotalInterest = 0.00
    Period = 0
    
    receipt.configure(state = 'normal')
    linea = "\n   Monthly Repayment (RM): "+ format(MonthlyRepayment,"0.2f")
    linepre = "\n   "+"Time: ".rjust(20)+current_time.rjust(20)+"\n"
    line1="\n   ======".rjust(5)+"=========".rjust(15)+"=============".rjust(20)+"============".rjust(17)
    line2="\n   Period".rjust(4)+"Principle".rjust(15)+"Interest Rate".rjust(20)+"   Balance  ".rjust(17)
    line3="\n   ======".rjust(4)+"=========".rjust(15)+"=============".rjust(20)+"============".rjust(17)
    
    receipt.insert(INSERT,linepre)
    receipt.insert(INSERT,linea)
    receipt.insert(INSERT,line1)
    receipt.insert(INSERT,line2)
    receipt.insert(INSERT,line3)
    receipt.configure(state = 'disabled')
    
    
    
    while Period < Total_period :
        Period = Period + 1
        Interest = Balance*Rate_per_month
        Principle = MonthlyRepayment-Interest
        Balance = Balance-Principle
        
        if Balance < 0:
            Balance = 0.00
            
        TotalPrinciple = TotalPrinciple + Principle
        TotalInterest = TotalInterest + Interest
        
        receipt.configure(state = 'normal')
        line4 = "\n"+"   "+str(Period).rjust(4)+format(Principle,"0.2f").rjust(15)+format(Interest,"0.2f").rjust(20)+format(Balance,"0.2f").rjust(17)
        receipt.insert(INSERT,line4)
        receipt.configure(state = 'disabled')
        
        
    line5="\n   ======".rjust(4)+"=========".rjust(15)+"=============".rjust(20)
    line6=("\n   Total"+format(TotalPrinciple,"0.2f").rjust(14)+format(TotalInterest,"0.2f").rjust(19))
    line7=("\n   ======".rjust(4)+"=========".rjust(15)+"=============".rjust(20))
    
    receipt.configure(state = 'normal')
    receipt.insert(INSERT,line5)
    receipt.insert(INSERT,line6)
    receipt.insert(INSERT,line7)
    line8=("\n"+"\n Thank you for using this system!"+ "\n 2021 reserved by jiashiuuuu.")
    receipt.insert(INSERT, line8)
    line9=("\n------------------------------------------------------------------"+"\n")
    receipt.insert(INSERT,line9)
    receipt.configure(state = 'disabled')
    
    style = ttk.Style()
    style.configure("SteelBlue1.TLabel",foreground="floral white",background="SteelBlue1",anchor="center",font=("agency fb", 14,'bold'))
    button3 = Button(window, text = "🧾🖨🖥  Export as txt",style="SteelBlue1.TLabel",command= txt)
    button3.config (state = NORMAL ,cursor="hand2")
    button3.place(x= 340, y=600, width= 200, height= 35)
    
    
def reset():
    property_value.delete(0, END)  
    DownPayment.delete(0, END)
    Rate.delete(0, END)
    Year.delete(0, END)
    receipt.configure(state = 'normal')
    receipt.delete('0.0',END)
    receipt.configure(state = 'disabled')

def time(): 
    global current_time
    now = datetime.now()
    current_time = now.strftime("%d %b  %H:%M:%S") #show current time
    clockUI.config(text="🕘 "+ current_time)
    clockUI.after(1000, time) #update data every seconds
    
def get_and_check_var():
    
    receipt.configure(state = 'normal')
    receipt.delete('0.0',END)
    receipt.configure(state = 'disabled')
    
    Loan= property_value.get()
    
    try :
        Loan = float(Loan)
        if Loan <= 0:
            messagebox.showerror('Invalid input',str(Loan)+" wrong data. Loan cannot be in negative!")
            property_value.delete(0, END)  
            return
    except :
        messagebox.showerror('Invalid input',str(Loan)+" wrong data. Please enter your property asset value in number form")
        property_value.delete(0, END) 
    
    
    Down_payment= DownPayment.get()
    
    try :
        Down_payment = float(Down_payment)
        if Down_payment < 0:
            messagebox.showerror('Invalid input',str(Down_payment)+" wrong data. Down payment cannot be in negative!")
            DownPayment.delete(0, END)
        if Down_payment > 100:
            messagebox.showerror('Invalid input',str(Down_payment)+" wrong data. Down payment cannot be over 100% !")
            DownPayment.delete(0, END)
    except :
        messagebox.showerror('Invalid input',str(Down_payment)+" wrong data. Please enter your down payment value in number form")
        DownPayment.delete(0, END)

    
           
            
    rate= Rate.get()
    
    try :
        rate = float(rate)
        if rate <= 0:
            messagebox.showerror('Invalid input',str(rate)+" wrong data. Rate cannot be in negative!")
            Rate.delete(0, END)
            return
    except :
        messagebox.showerror('Invalid input',str(rate)+" wrong data. Please enter your rate value in number form")
        Rate.delete(0, END)
    
    year= Year.get()
    try :
        year = float(year)
        if year <= 0:
            messagebox.showerror('Invalid input',str(year)+" wrong data. Year cannot be in negative!")
            Year.delete(0, END)
        if year > 100:
            messagebox.showerror('Invalid input',str(year)+" wrong data. Year cannot be over 100!")
            Year.delete(0, END)
            return
    except :
        messagebox.showerror('Invalid input',str(year)+" wrong data. Please enter your year value in number form")
        Year.delete(0, END)
        
    



        
    Loan = float(Loan)
    Down_payment = float(Down_payment)
    rate = float(rate)
    year = float(year)
    Loan = Loan*((100 - Down_payment)/100)
    cal (Loan, rate, year)
   
def end_():
    confirm = messagebox.askyesnocancel("Confirmation","Do you sure you want to quit this system?")
    if confirm == True:  
        window.destroy() 

#main program
window=tk.Tk()
window.title ("Home Loan Calculator 🧾🖨🖥⌨ | 2021 by Jiashiuuu")
window.geometry ("800x650")
window.maxsize (800,650)
window.configure (bg='white smoke')
window.attributes('-alpha', 0.9)
window.protocol("WM_DELETE_WINDOW", end_)

photopre =tk.PhotoImage (file= gopath("calculator2.png"))
lblgambarpre = Label (window, image=photopre, relief ="flat", borderwidth=0)
lblgambarpre.place (x=470, y=3, width=50, height=50)

photopre2 =tk.PhotoImage (file = gopath("loan.png"))
lblgambarpre2 = Label (window, image=photopre2, relief ="flat", borderwidth=0)
lblgambarpre2.place (x=30, y=0, width=100, height=110)

photo1 =tk.PhotoImage (file = gopath("Picture5.png"))
lblgambar = Label (window, image=photo1, relief ="flat", borderwidth=0)
lblgambar.place (x=610, y=50, width=160, height=165)

photo2 = tk.PhotoImage (file = gopath("Picture3.png"))
lblgambar2 = Label (window, image=photo2, relief ="flat", borderwidth=2)
lblgambar2.place (x=610, y=250, width=170, height=180)

photo3 = tk.PhotoImage (file = gopath("Picture4.png"))
lblgambar3 = Label (window, image=photo3, relief ="flat", borderwidth=2)
lblgambar3.place (x=610, y=450, width=180, height=180)

clockUI = Label(window, font = ('Bahnschrift Light Condensed', 14), background="white smoke",foreground="midnight blue")
clockUI.place(x=220, y= 50, width = 250, height = 40)
time()

title = Label(window, text = ('Home Loan Calculator') , font = ('Milkyroad', 25,"underline"), background="white smoke", foreground="midnight blue")
title.place(x=130, y=10)

label1 = Label(window, text = ('Property Asset Value (RM) 💰 :'), font = ('Bahnschrift Light Condensed',14),background="white smoke",foreground="midnight blue")
label1.place(x=30, y= 100)

label2 = Label(window, text = ('Down Payment (%) 💸           :'), font =('Bahnschrift Light Condensed',14),background="white smoke",foreground="midnight blue")
label2.place(x=30, y= 140)

label3 = Label(window, text = ('Rate (%) 💎                          :'), font =('Bahnschrift Light Condensed',14),background="white smoke",foreground="midnight blue")
label3.place(x=30, y= 180)

label4 = Label(window, text = ('Year 📆                                :'),font = ('Bahnschrift Light Condensed',14),background="white smoke",foreground="midnight blue")
label4.place(x=30, y= 220)

property_value = Entry(window)
property_value.place(x=230, y=105)

DownPayment = Entry(window)
DownPayment.place(x=230, y=145)

Rate = Entry(window)
Rate.place(x=230, y=185)

Year = Entry(window)
Year.place(x=230, y=225)

style = ttk.Style()
style.configure("CadetBlue3.TLabel",foreground="floral white",background="CadetBlue3",anchor="center",font=("agency fb", 16,'bold'))

button1 = Button(window, text = "📝   Calculate  ", style="CadetBlue3.TLabel",command= get_and_check_var)
button1.config (state = NORMAL ,cursor="hand2")
button1.place(x= 410, y=130, width= 140, height= 35)

style = ttk.Style()
style.configure("orchid2.TLabel",foreground="floral white",background="orchid2",anchor="center",font=("agency fb", 16,'bold'))

button2 = Button(window, text = "↷     Reset  ", style="orchid2.TLabel",command= reset )
button2.config (state = NORMAL ,cursor="hand2")
button2.place(x= 410, y=180, width= 140, height= 35)

receipt = scrolledtext.ScrolledText(window, wrap=WORD , width = 66, height = 18, font =("courier new", 10), selectbackground="CadetBlue1",selectforeground="black")
receipt.config(cursor="arrow")
receipt.place (x =10, y= 280)
receipt.configure(state = 'disabled')

style = ttk.Style()
style.configure("SteelBlue1.TLabel",foreground="floral white",background="SteelBlue1",anchor="center",font=("agency fb", 16,'bold'))

style = ttk.Style()
style.configure("orchid1.TLabel",foreground="floral white",background="khaki3",anchor="center",font=("Arial Rounded MT Bold", 12))
button4 = Button(window, text = "How to use this system?", style="orchid1.TLabel",command= usermanual )
button4.config (state = NORMAL ,cursor="hand2")
button4.place(x= 370, y=80, width= 220, height= 35)

style = ttk.Style()
style.configure("gold.TLabel",foreground="floral white",background="deep sky blue",anchor="center",font=("agency fb", 16,'bold'))
button5 = Button(window, text = "Introduction to home loan", style="gold.TLabel",command= moreinfo )
button5.config (state = NORMAL ,cursor="hand2")
button5.place(x=10, y=600, width= 220, height= 35)

style = Style()
style.configure("btn.TLabel",background="white smoke",anchor="center")

photoh =tk.PhotoImage (file = gopath( "help.png"))
helpUI = Button(window, style="btn.TLabel",image=photoh)
helpUI.place (x=575, y=15)
helpUI.configure (state = NORMAL,cursor="hand2")
helpUI.bind("<Button-1>", lambda e:webbrowser.open_new_tab('https://github.com/jiashiuuuu/Home-Loan-Calculator'))

window.mainloop()

