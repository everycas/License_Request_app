import uuid
from tkinter import *
from random import randint
from tkinter import messagebox
import pyperclip

COLOR = "#F5F5DC"


def n():
    
    """ Generate and return random number from defined range """
    
    return str(randint(1111, 999999))


def uid_rnum():

    """ Generate request code from uuid node.
    The mask is: n1 - uid3 - uid1 - n2 - uid2 - n3 """

    # Get uid num string
    uid = str(uuid.getnode())
    
    # Reverse uid
    num = uid[::-1]
    
    # Pick control nums from uid
    x1 = num[:4]
    x2 = num[4:9]
    x3 = num[9:]
    
    # Redy request code / rnum
    return f"{n()}-{x3}-{x1}-{n()}-{x2}-{n()}"
    

##############################################
# GUI / Интерфейс программы  -----------------
##############################################

root = Tk()
root.title('LicRequest v1.0')
root.config(padx=5, pady=5)
root.maxsize(width=400, height=250)
root.resizable(False, False)

label = Label(text="Request: ", width=7)
label.grid(column=0, row=0, sticky=NW)

entry = Entry(width=40, relief="sunken")
entry.insert(0, uid_rnum())
entry.config(state='readonly', readonlybackground=COLOR)
entry.grid(column=1, row=0, padx=3, pady=3)

pyperclip.copy(entry.get())
messagebox.showinfo(title="Copy to clipboard", message='License request number copied to clipboard.')
root.destroy()
