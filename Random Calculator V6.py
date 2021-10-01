from tkinter import*
import tkinter.messagebox 

class calculator:

    def __init__(self,root):
        self.root = root
        self.root.title = ("Addition")
        self.root.geometry("1200+600+0+0")
        frame1 = Frame(self.rooot)
        frame1.gride()
        
        frame2 = Frame(self.rooot)
        frame2.gride(row=0,column=0)
        
        frame3 = Frame(frame1)
        frame3.gride(row=1,column=0)

        FirstNum = StringVar()
        SecondNum = StringVar()

        self.lb1FirstNum = Label(frame1,text='Enter First Number')
        self.lb1FirstNum.grid(row=0, comlumn=0)
        self.txtFirstNum = Entry(frame1,textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, comlumn=1)

        self.lb1SecondNum = Label(frame1,text='Enter Second Number')
        self.lb1SecondNum.grid(row=0, comlumn=0)
        self.txtSecondNum = Entry(frame1,textvariable=SecondNum)
        self.txtSecondNum.grid(row=0, comlumn=1)
        
if __name__ =='__main__':
    root=Tk()
    application = calculator(root)
    root.mainloop()
    