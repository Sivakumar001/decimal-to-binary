from tkinter import *
# module for graphical interface
from tkinter import messagebox

# a single function to convert decimal to binary


def converter(Event=None):
    # making state so user cannot write on result
    result.config(state='normal')
    result.delete(CURRENT, END)  # to delete past occurences
    try:
        int(decimal.get())  # exception cases for alphabets
    except Exception:
        # message box is used inorder to display errors in new error screen
        messagebox.showerror('invalid!', message='enter only numbers')
        decimal.delete(0, END)
    else:
        quo = int(decimal.get())  # getting the decimal
        lis = []  # making a list to store values
        while True:
            rem = quo % 2
            quo = quo // 2
            lis.append(rem)
            if quo == 0:
                break
        sam = ''  # converting to string inorder to display values
        for i in range(len(lis) - 1, -1, -1):
            sam = sam + str(lis[i])
            if i % 4 == 0:
                sam = sam + ' '
        result.insert(INSERT, sam)  # displaying values in text box
        result.config(state='disable')


# graphical interface object
root = Tk()
root.title('decimal to binary')
root.geometry('400x400')
root.resizable(False, False)
root.config(bg='grey')
# setting title and words here
Label(root, text='decimal to binary converter',
      font='timesnewroman 14 bold', bg='grey').place(x=60, y=0)
Label(root, text='enter a number:', font='verdana 10', bg='grey').place(x=70, y=100)
Label(root, text='the result is:', font='verdana 10', bg='grey').place(x=40, y=200)
# setting buttons entry and result values in here
decimal = Entry(root)
but = Button(root, text='find', command=converter)
result = Text(root, width=25, height=1, state='disable')
# a simple bind event to run when enter is pressed
root.bind('<Return>', converter)
# finally placing in correct places
decimal.place(x=190, y=100)
but.place(x=210, y=150)
result.place(x=130, y=200)

root.mainloop()
