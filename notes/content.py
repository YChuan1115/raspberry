from tkinter import *
class App:
        def __init__(self,master):
            master.geometry("300x200");
            fm = Frame(master);
            Button(fm, text="Top").pack(side=TOP,expand=YES);
            Button(fm, text="Center").pack(side=TOP,expand=YES);
            Button(fm, text="Bottom").pack(side=TOP,expand=YES);
            fm.pack(fill=BOTH,expand=YES);
root = Tk();
root.option_add("*font",("verdana",12,"bold"));
root.title("Pack - Example 4");
display = App(root)
root.mainloop();
