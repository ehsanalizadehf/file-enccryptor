import os
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
from tkinter import filedialog
from PIL import ImageTk,Image
import sqlite3
import mmap



# con=sqlite3.connect('prj.db')
# con.execute('''CREATE TABLE USER
#          (ID INT PRIMARY KEY     NOT NULL,
#          heights   INT PRIMARY KEY   NOT NULL,);''')
# cur=con.cursor()
# conn.close()
def get_height():
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    return height
    fd1=open('userinput.txt',"w")
    fd1.write(get_height())

def get_weight():
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight
    fd2 = open('userinput.txt', "w")
    fd1.write(get_weight())



def calculate_bmi(a="", button_exit=None):   # "a" is there because the bind function gives an argument to the function....
    print(a)
    '''
      This function calculates the result
    '''
    global flag_pass
    flag_pass=0
    try:
        height = get_height()
        weight = get_weight()
        # with open("userinput.txt", "r") as file1:
        #     f_list = [float(i) for line in file1 for i in line.split(',') if i.strip()]
        #     T = f_list[0:5]
        #     if T==height + weight:
        #        flag_pass=1
        if height==185 and weight==93:
            flag_pass=1
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)


try:
    import pyAesCrypt
except:
    msg.showerror("Status","pyAesCrypt not found \n install using \"pip install pyAesCrypt\" ")
    quit()

def decrypt():
    if(filepath.get()==""):
        msg.showerror("File Status","File Name cannot be empty!!")
    else:
        if(os.path.exists(filepath.get())):
            filepathwaes=filepath.get().split(".aes")[0]
            try:
                pyAesCrypt.decryptFile(filepath.get(),filepathwaes,password.get(),int(buffersize.get()))
                if(delfile.get()=="yes"):
                    os.remove(filepath.get())
                else:
                    pass
                msg.showinfo("File Status","File Decrypted Successfully!!")
                password.set("")
                filepath.set("")
            except ValueError as e:
                msg.showerror("File Status",e)
            except:
                msg.showerror("File Status","an error occured!!")
        else:
            msg.showerror("File Status","File does not exists!!")
    
    
    
def encrypt():
    if(filepath.get()==""):
        msg.showerror("File Status","File Name cannot be empty!!")
    else:
        if(os.path.exists(filepath.get())):
            filepathaes=filepath.get()+".aes"
            try:
                pyAesCrypt.encryptFile(filepath.get(),filepathaes,password.get(),int(buffersize.get()))
                if(delfile.get()=="yes"):
                    os.remove(filepath.get())
                else:
                    pass
                msg.showinfo("File Status","File Encrypted Successfully!!")
                password.set("")
                filepath.set("")
            except:
                msg.showerror("File Status","an error occured!!")
        else:
            msg.showerror("File Status","File does not Exists!!")
    
def browsefile():    
    filepath.set(filedialog.askopenfilename(title="Select File",filetypes=(("all files","*.*"),)))
        
def about():
    global r4
    r4=Toplevel(root)
    r4.title("About this")
    r4.resizable(False,False)
    r4.iconbitmap("lock.ico")
    mf4=ttk.Frame(r4,padding='3 3 12 12')
    mf4.pack(fill="both",expand="yes")
    mf4.rowconfigure(0,weight=1)
    mf4.columnconfigure(0,weight=1)
    l=ttk.Label(mf4,background="#19284B")
    l.pack(fill="both",expand="yes")
    ttk.Label(l,text="Created By: Ehsan alizadeh Fallah",foreground="white",background="#19284B",font=("Arial Black",16)).grid(row=2,column=0,columnspan=2)
    img=ImageTk.PhotoImage(Image.open("lock.ico"))
    imglbl=ttk.Label(l,background="#19284B",image=img)
    imglbl.photo=img
    imglbl.grid(row=4,column=0,rowspan=3)
    ttk.Label(l,text="File Encrypter",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=4,column=1)
    ttk.Separator(l,orient="horizontal").grid(row=6,column=0,columnspan=3,sticky="ew")
    ttk.Label(l,text="Email : e.alizadeh07@umail.umz.ac.ir",foreground="white",background="#19284B",font=("Calibri",14)).grid(row=7,column=1)


    for child in l.winfo_children():
        child.grid_configure(pady=10)

def features():
    r5=Toplevel(root)
    r5.title("What's New")
    r5.resizable(False,False)
    r5.iconbitmap("lock.ico")
    mf5=ttk.Frame(r5,padding='3 3 12 12')
    mf5.pack(fill="both",expand="yes")
    mf5.rowconfigure(0,weight=1)
    mf5.columnconfigure(0,weight=1)
    l=ttk.Label(mf5,background="#19284B")
    l.pack(fill="both",expand="yes")
    ttk.Label(l,text="File Encrypter",foreground="white",background="#19284B",font=("Arial black",16)).grid(row=2,column=0)
    ttk.Separator(l,orient="horizontal").grid(row=3,column=0,columnspan=5,sticky="ew")
    ttk.Label(l,text="1. Encrypt and Decrypt Files",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=5,column=0)
    ttk.Label(l,text="2. Support all File types (*.*) ",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=6,column=0)
    ttk.Label(l,text="3. Encrypt Files Using AES256-CBC Algorithm",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=7,column=0)
    ttk.Label(l,text="4. Use of Password to Encypt or Decrypt Files",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=8,column=0)
    ttk.Label(l,text="5. Set Buffer size of 64Kb to Encrypt/Decrypt \nVery Large Files in 64Kb(default) Chunks\n to not Overload the Memory.",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=9,column=0)
if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("400x400")
    TOP.configure(background="#307678")
    TOP.title("BMI Calculator")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="#307678", anchor="center", text="             BMI Calculator", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter Weight (in kg):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter Height (in cm):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=121)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=121)
    BUTTON = Button(bg="#2187e7", bd=10, text="BMI", padx=30, pady=10, command=calculate_bmi,
                    font=("Helvetica", 15, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    # creates a Tk() object

    TOP.mainloop()
root=Tk()
root.title("File Encrypter ")
root.iconbitmap("lock.ico")
root.resizable(False,False)

mainframe=ttk.Frame(root,padding='3 3 12 12')
mainframe.pack(fill="both",expand="yes")
mainframe.rowconfigure(0,weight=1)
mainframe.columnconfigure(0,weight=1)

l=ttk.Label(mainframe,background="#19284B")
l.pack(fill='both',expand='yes')

filepath=StringVar()
buffersize=StringVar()
password=StringVar()
delfile=StringVar()

buffersize.set(int(64*1024))
password.set("12345")

ttk.Label(l,text="File path: ",background="#19284B",foreground="white").grid(row=2,column=2)
e=ttk.Entry(l,textvariable=filepath,width=40)
e.grid(row=2,column=3)
e.focus()
ttk.Button(l,text="Browse",command=browsefile).grid(row=4,column=3)
ttk.Label(l,text="Buffer Size: ",background="#19284B",foreground="white").grid(row=6,column=2)
ttk.Entry(l,textvariable=buffersize).grid(row=6,column=3,sticky='w')
ttk.Label(l,text="Password",background="#19284B",foreground="white").grid(row=8,column=2)
ttk.Entry(l,textvariable=password).grid(row=8,column=3,sticky='w')
ttk.Label(l,text="Delete File after Encrypt/Decrypt",background="#19284B",foreground="white").grid(row=10,column=3,sticky='w')
ttk.Checkbutton(l,variable=delfile,onvalue="yes",offvalue="no",).grid(row=10,column=2)
ttk.Button(l,text="Decrypt",command=decrypt).grid(row=12,column=3)
ttk.Button(l,text="About",command=about).grid(row=14,column=3)
ttk.Button(l,text="Encrypt",command=encrypt).grid(row=12,column=2)
ttk.Button(l,text="Features",command=features).grid(row=14,column=2)

for child in l.winfo_children():
    child.grid_configure(padx=10,pady=10)
if flag_pass==1:
    root.mainloop()
