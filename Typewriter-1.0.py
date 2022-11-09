#!/usr/bin/python3.8
# Import tkinter widgets

from tkinter import Tk, Menu, scrolledtext, Label, Button, END, messagebox, simpledialog, Canvas
from tkinter.filedialog import asksaveasfilename, askopenfilename
print('Typewriter 1.0')
# the root window
root = Tk()
root.title('Typewriter 1.0')

root.resizable(False, False)
root.geometry('500x440')


# The Text widget
text = scrolledtext.ScrolledText(root, height=30,font='TkFixedFont',bg='aliceblue', fg='black', bd=10, insertbackground='black', relief='flat', wrap='word')
text.pack()

# funs
def close():
    Close = messagebox.askyesno('Close?', 'Do you want to close the writer?')
    if Close == True:
        root.destroy()

def  clear():
    question = messagebox.askyesno('Clear?', 'Do you want to delete the text that you have written?')
    if question == True:
        text.delete('1.0', END)
        



    
def save():
    filepath = asksaveasfilename(
    defaultextension = ".txt",
    filetypes = [("Text Files", "*.txt*"), ("All Files", "*.*")])

    if not filepath:
        return

    with open(filepath, 'w') as output_file:
        txt = text.get('1.0', END)
        output_file.write(txt)
    print('File saved as ' + filepath)

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text.delete(1.0, END)
    with open(filepath, "r") as input_file:
        tex = input_file.read()
        text.insert(END, tex)
    print('Opened file ' + filepath)
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar)
def about():
    about_window = Tk()
    about_window.resizable(False, False)
    about_window.geometry('200x200')
    about_window.title('About')
    about_window.update()
    c = Canvas(about_window, width=200, height=150, bg='Gray')
    c.create_text(5, 5, anchor='w', fill='Black', font='TkFixedFont 10 bold', text='Typewriter')
    c.create_text(5, 30,anchor='w', fill='Black', font='TkFixedFont 8', text='Version: 1.0 \nMade by: The Wild Coder')
    c.pack()
    butt = Button(about_window, command=about_window.destroy, text='Close')
    butt.pack()
    root.update()
file_menu.add_command(label='Exit', command=close)
file_menu.add_command(label='Save', command=save)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Clear', command=clear)
menubar.add_cascade(label='File', menu=file_menu)
help_menu = Menu(menubar)
help_menu.add_command(label='About', command=about)
menubar.add_cascade(label='Help', menu=help_menu)
root.update()


root.mainloop()
# End
