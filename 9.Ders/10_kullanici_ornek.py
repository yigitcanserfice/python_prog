import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_614=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_614["font"] = ft
        GLabel_614["fg"] = "#333333"
        GLabel_614["justify"] = "center"
        GLabel_614["text"] = "Kullanıcı Girişi :"
        GLabel_614.place(x=70,y=60,width=213,height=30)

        GLineEdit_957=tk.Entry(root)
        GLineEdit_957["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_957["font"] = ft
        GLineEdit_957["fg"] = "#333333"
        GLineEdit_957["justify"] = "center"
        GLineEdit_957["text"] = "Entry"
        GLineEdit_957.place(x=160,y=100,width=127,height=30)

        GLabel_387=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_387["font"] = ft
        GLabel_387["fg"] = "#333333"
        GLabel_387["justify"] = "center"
        GLabel_387["text"] = "Kıllanıcı Adı  :"
        GLabel_387.place(x=60,y=100,width=93,height=30)

        GButton_921=tk.Button(root)
        GButton_921["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_921["font"] = ft
        GButton_921["fg"] = "#000000"
        GButton_921["justify"] = "center"
        GButton_921["text"] = "Giriş"
        GButton_921.place(x=170,y=240,width=88,height=30)
        GButton_921["command"] = self.GButton_921_command

        GLabel_539=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_539["font"] = ft
        GLabel_539["fg"] = "#333333"
        GLabel_539["justify"] = "center"
        GLabel_539["text"] = "Şifre :"
        GLabel_539.place(x=60,y=150,width=70,height=25)

        GLineEdit_546=tk.Entry(root)
        GLineEdit_546["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_546["font"] = ft
        GLineEdit_546["fg"] = "#333333"
        GLineEdit_546["justify"] = "center"
        GLineEdit_546["text"] = "Entry1"
        GLineEdit_546.place(x=160,y=150,width=128,height=30)
        GLineEdit_546["show"] = "*"

    def GButton_921_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
