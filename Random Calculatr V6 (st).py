import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk , Image

root=tk.Tk()
root.title("Calculator")
root.geometry('400x300')
root.resizable(False,False)

#BACKGROUND((
#button image

#icon
path7 = r'C:\\Users\\HOME\\Downloads\\New folder\\Random\\Jupyter\\calculator.png'
bg7 = ImageTk.PhotoImage(Image.open(path7))
root.iconphoto(True, bg7 )
#canvas
can = tk.Canvas(root,width=300,height=400)
can.pack(fill="both",expand=True)
#image part
can.create_image(0,0, image = bg , anchor = "nw")
#))

#1st title
can.create_text(200, 17 ,fill="black", text="Calculator Selector", font=("Ink Free",20))

#entry box for selector
e = tk.Entry(root,width=50)

e.config(font=("Ink Free",10))
e.bind("<Return>")
e.pack()
b1_window = can.create_window(30,55 , anchor="nw", window=e)




#BUTTON((

#what makes the cals come
def come_cals():
    if e.get() == "T":#Triangle area cal
        
        t = tk.Toplevel()
        t.title("TRIANGLE AREA")
        t.geometry("400x300")
        t.config(bg="light blue")
        t.resizable(False,False)
        t.overrideredirect(True)
        
        
        #1st Label
        tl = tk.Label(t,text="TRIANGLE AREA")
        tl.config(font=("Ink Free",20))
        tl.config(bg="light blue")
        tl.pack()

        tlll = tk.Label(t,text= "Base:")
        tlll.config(font=("Ink Free",12))
        tlll.config(bg="light blue")
        tlll.pack()
        #entry box
        te = tk.Entry(t,width=50)
        te.config(font=("Ink Free",10))
        te.pack()
        

        #label
        tll = tk.Label(t,text= "Hight:")
        tll.config(font=("Ink Free",12))
        tll.config(bg="light blue")
        tll.pack()
        
        tte = tk.Entry(t,width=50)
        tte.config(font=("Ink Free",10))
        tte.pack()
        

        #The solving parts() 
        def answering():
            B = int(te.get())
            H = int(tte.get())
            T = (B*H)/2
            AQ =  "Answer",round(T,3)
            Al = tk.Label(t,text=  AQ)
            Al.config(font=("Ink Free",15))
            Al.config(bg="light blue")
            Al.pack()
        
        def Error():
            try:
                int(te.get())
                int(tte.get())
            except:
                messagebox.showerror('Error', 'Something went wrong!',icon='error')
        #)
        #button that solves
        
        tb = tk.Button(t,image = bg1)
        tb.config(bg="white")
        tb.config(command=lambda:[Error(),answering()])
        tb.pack()

        def cringe():
            t.destroy()
        
        tb2 =tk.Button(t,text="Close")
        tb2.config(font=("Ink Free",12))
        tb2.config(bg="white")
        tb2.config(command=cringe)
        tb2.pack(side=tk.LEFT)


     #triangle prism
    elif e.get() == "TP":
        tp = tk.Toplevel()
        tp.title("TRIANGLE AREA")
        tp.geometry("400x300")
        tp.config(bg="light blue")
        tp.resizable(False,False)
        tp.overrideredirect(True)
        #title
        tpt = tk.Label(tp,text="TRIANGLE PRISM AREA")
        tpt.config(font=("Ink Free",20))
        tpt.config(bg="light blue")
        tpt.pack()
        #label
        tpl = tk.Label(tp,text="Base")
        tpl.config(font=("Ink Free",12))
        tpl.config(bg="light blue")
        tpl.pack()
        #entry box base
        tpe = tk.Entry(tp,width=50)
        tpe.config(font=("Ink Free",10))
        tpe.pack()
        # 2label
        tpl2 = tk.Label(tp,text="Hight")
        tpl2.config(font=("Ink Free",12))
        tpl2.config(bg="light blue")
        tpl2.pack()
        #entry box hight
        tpe1 = tk.Entry(tp,width=50)
        tpe1.config(font=("Ink Free",10))
        tpe1.pack()
        #3label
        tpl3 = tk.Label(tp,text="Width")
        tpl3.config(font=("Ink Free",12))
        tpl3.config(bg="light blue")
        tpl3.pack()
        #entry box width
        tpe2 = tk.Entry(tp,width=50)
        tpe2.config(font=("Ink Free",10))
        tpe2.pack()
        #button
        def Error3():
            try:
                int(tpe.get())
                int(tpe1.get())
                int(tpe2.get())
            except:
                messagebox.showerror('Error', 'Something went wrong!',icon='error')
        def answering1():
            B2 = int(tpe.get())
            H2 = int(tpe1.get())
            W2 = int(tpe2.get())
            
            T2 = (B2*H2*W2)/2
            AQ2 =  "Answer",round(T2,3)
            Al2 = tk.Label(tp,text=  AQ2)
            Al2.config(font=("Ink Free",15))
            Al2.config(bg="light blue")
            Al2.pack()
        tpb = tk.Button(tp,image=bg1)
        tpb.config(bg="white")
        tpb.config(command=lambda:[Error3(),answering1()])
        tpb.pack()
        
        def cringe():
            tp.destroy()
        
        tpb =tk.Button(tp,text="Close")
        tpb.config(font=("Ink Free",12))
        tpb.config(bg="white")
        tpb.config(command=cringe)
        tpb.pack(side=tk.LEFT)
    elif e.get() == "SA":
        sa = tk.Toplevel()
        sa.title("RECTANGLE/SQUARE AREA")
        sa.geometry("400x300")
        sa.config(bg="light blue")
        sa.resizable(False,False)
        sa.overrideredirect(True)
        #label
        sal= tk.Label(sa,text="RECTANGLE/SQUARE AREA")
        sal.config(font=("Ink Free",20))
        sal.config(bg="light blue")
        sal.pack()
        #label2
        sal2= tk.Label(sa,text="Base")
        sal2.config(font=("Ink Free",15))
        sal2.config(bg="light blue")
        sal2.pack()
        #entry
        sae = tk.Entry(sa,width=50)
        sae.config(font=("Ink Free",10))
        sae.pack()
        #label3
        sal3= tk.Label(sa,text="Hight")
        sal3.config(font=("Ink Free",15))
        sal3.config(bg="light blue")
        sal3.pack()
        #entry2
        sae2 = tk.Entry(sa,width=50)
        sae2.config(font=("Ink Free",10))
        sae2.pack()
        #Button(
        def answering2():
            B = int(sae.get())
            H = int(sae2.get())
            
            T = (B*H)
            AQ =  "Answer",round(T,3)
            Al = tk.Label(sa,text=  AQ)
            Al.config(font=("Ink Free",15))
            Al.config(bg="light blue")
            Al.pack()

        def Error4():
            try:
                int(sae.get())
                int(sae2.get())
            except:
                messagebox.showerror('Error', 'Something went wrong!',icon='error')
        #button
        sab =tk.Button(sa,image= bg1,bg="white")
        sab.config(command=lambda:[Error4(),answering2()])
        sab.pack()
        #)
        def cringe():
            sa.destroy()

        sab =tk.Button(sa,text="Close")
        sab.config(font=("Ink Free",12))
        sab.config(bg="white")
        sab.config(command=cringe)
        sab.pack(side=tk.LEFT)
        
    elif e.get() == "RP":
        rp = tk.Toplevel()
        rp.title("RECTANGLER/CUBE PRISM")
        rp.geometry("400x300")
        rp.config(bg="light blue")
        rp.resizable(False,False)
        rp.overrideredirect(True)
        #label
        rpl2= tk.Label(rp,text="RECTANGLER/CUBE PRISM")
        rpl2.config(font=("Ink Free",20))
        rpl2.config(bg="light blue")
        rpl2.pack()
        #label2
        rpl2= tk.Label(rp,text="Base")
        rpl2.config(font=("Ink Free",12))
        rpl2.config(bg="light blue")
        rpl2.pack()
        #entry
        rpe = tk.Entry(rp,width=50)
        rpe.config(font=("Ink Free",10))
        rpe.pack()
        #label3
        rpl3= tk.Label(rp,text="Hight")
        rpl3.config(font=("Ink Free",12))
        rpl3.config(bg="light blue")
        rpl3.pack()
        #entry2
        rpe2 = tk.Entry(rp,width=50)
        rpe2.config(font=("Ink Free",10))
        rpe2.pack()
        
        rpl4= tk.Label(rp,text="Width")
        rpl4.config(font=("Ink Free",12))
        rpl4.config(bg="light blue")
        rpl4.pack()
        
        rpe3 = tk.Entry(rp,width=50)
        rpe3.config(font=("Ink Free",10))
        rpe3.pack()
        def answering2():
            B = int(rpe.get())
            H = int(rpe2.get())
            W = int(rpe3.get())
            
            T = (B*H*W)
            AQ =  "Answer",round(T,3)
            Al = tk.Label(rp,text=  AQ)
            Al.config(font=("Ink Free",15))
            Al.config(bg="light blue")
            Al.pack()

        def Error4():
            try:
                int(rpe.get())
                int(rpe2.get())
                int(rpe3.get())
            except:
                messagebox.showerror('Error', 'Something went wrong!',icon='error')
        #button
        rpb =tk.Button(rp,image= bg1,bg="white")
        rpb.config(command=lambda:[Error4(),answering2()])
        rpb.pack()
        #)

        def cringe():
            rp.destroy()
        
        rpb =tk.Button(rp,text="Close")
        rpb.config(font=("Ink Free",12))
        rpb.config(bg="white")
        rpb.config(command=cringe)
        rpb.pack(side=tk.LEFT)
    elif e.get() == "S":
        s = tk.Toplevel()
        s.title("Sphere Volume")
        s.geometry("400x300")
        s.config(bg="light blue")
        s.resizable(False,False)
        s.overrideredirect(True)
        
        sl=tk.Label(s,text="Sphere Volume")
        sl.config(font=("Ink Free",20))
        sl.config(bg="light blue")
        sl.pack()

        sl2=tk.Label(s,text="Radius")
        sl2.config(font=("Ink Free",15))
        sl2.config(bg="light blue")
        sl2.pack()

        se=tk.Entry(s,width=50)
        se.config(font=("Ink Free",10))
        se.pack()

        def Error4():
            try:
                int(se.get())
            except:
                messagebox.showerror('Error', 'Something went wrong!',icon='error')
        
        def answering2():
            r = int(se.get())
            
            T = (4/3)*3.14*r**3
            AQ =  "Answer",round(T,3)
            Al = tk.Label(s,text=  AQ)
            Al.config(font=("Ink Free",15))
            Al.config(bg="light blue")
            Al.pack()
        
        sb=tk.Button(s,image=bg1)
        sb.config(bg="white")
        sb.config(command=lambda:[Error4(),answering2()])
        sb.pack()

        def cringe():
            s.destroy()
        
        sb =tk.Button(s,text="Close")
        sb.config(font=("Ink Free",12))
        sb.config(bg="white")
        sb.config(command=cringe)
        sb.pack(side=tk.LEFT)
    elif  e.get() == "C":
        
        c = tk.Toplevel()
        c.title("Circunfernce Calculator ")
        c.geometry("400x300")
        c.config(bg="light blue")
        c.resizable(False,False)
        c.overrideredirect(True)

        cl=tk.Label(c,text="Circunfernce Calculator")
        cl.config(font=("Ink Free",20))
        cl.config(bg="light blue")
        cl.pack()

        cl2=tk.Label(c,text="Radius")
        cl2.config(font=("Ink Free",15))
        cl2.config(bg="light blue")
        cl2.pack()

        ce=tk.Entry(c,width=50)
        ce.config(font=("Ink Free",10))
        ce.pack()

        def Error4():
            try:
                int(ce.get())
            except:
                messagebox.showerror('Error', 'Something went wrong!',icon='error')
        
        def answering2():
            r = int(ce.get())
            
            T = 2*3.14*r
            AQ =  "Answer",round(T,3)
            Al = tk.Label(c,text=  AQ)
            Al.config(font=("Ink Free",15))
            Al.config(bg="light blue")
            Al.pack()
        
        cb=tk.Button(c,image=bg1)
        cb.config(bg="white")
        cb.config(command=lambda:[Error4(),answering2()])
        cb.pack()
        
        def cringe():
            c.destroy()
        
        cb =tk.Button(c,text="Close")
        cb.config(font=("Ink Free",12))
        cb.config(bg="white")
        cb.config(command=cringe)
        cb.pack(side=tk.LEFT)
    elif e.get() == "I":
        i = tk.Toplevel()
        i.title("Intrest Calculator")
        i.geometry("400x300")
        i.config(bg="light blue")
        i.resizable(False,False)
        i.overrideredirect(True)
        #label
        il= tk.Label(i,text="Intrest Calculator")
        il.config(font=("Ink Free",20))
        il.config(bg="light blue")
        il.pack()
        #label2
        il2= tk.Label(i,text="Enter The Amount =")
        il2.config(font=("Ink Free",12))
        il2.config(bg="light blue")
        il2.pack()
        #entry
        ie = tk.Entry(i,width=50)
        ie.config(font=("Ink Free",10))
        ie.pack()
        #label3
        il4= tk.Label(i,text="Enter The Rate =")
        il4.config(font=("Ink Free",12))
        il4.config(bg="light blue")
        il4.pack()
        #entry2
        ie2 = tk.Entry(i,width=50)
        ie2.config(font=("Ink Free",10))
        ie2.pack()
        
        il5= tk.Label(i,text="Enter The Amount Of Time/yrs =")
        il5.config(font=("Ink Free",12))
        il5.config(bg="light blue")
        il5.pack()
        
        ie3 = tk.Entry(i,width=50)
        ie3.config(font=("Ink Free",10))
        ie3.pack()
        def answering2():
            p = int(ie.get())
            r = int(ie2.get())
            t = int(ie3.get())
            
            v = p*(r/100)*t
            AQ =  "Answer",round(v,3)
            Al = tk.Label(i,text=  AQ)
            Al.config(font=("Ink Free",15))
            Al.config(bg="light blue")
            Al.pack()
        

        def Error4():
            try:
                int(ie.get())
                int(ie2.get())
                int(ie3.get())
            except:
                messagebox.showerror('Error', 'Something went wrong!',icon='error')
        #button
        ib =tk.Button(i,image= bg1,bg="white")
        ib.config(command=lambda:[Error4(),answering2()])
        ib.pack()
        def cringe():
            i.destroy()
        
        ib =tk.Button(i,text="Close")
        ib.config(font=("Ink Free",12))
        ib.config(bg="white")
        ib.config(command=cringe)
        ib.pack(side=tk.LEFT)

    else:
        def Error2():
                messagebox.showerror('Error', 'Something went wrong!',icon='error')
        Error2()






#buttn img
# Creating a photoimage object to use image
path3 = r'C:\\Users\\HOME\\Downloads\\New folder\\Random\\Jupyter\\yes3.png'
bg1 = ImageTk.PhotoImage(Image.open(path3))
#actual image
b1 = tk.Button(root, text = 'Click Me !', image = bg1,bg='white',activebackground='white',command=come_cals)
b1_window = can.create_window(175,80, anchor="nw", window=b1)
#))

#OPTIONS TO SELECT(
def options():
    op = tk.Toplevel()
    op.config(background="light blue")
    op.title("Options")
    op.geometry('300x400')
    op.resizable(False,False)
    op.overrideredirect(True)
    opl = tk.Label(op, text = 'Type:')
    opl.config(font=("Ink Free",20))
    opl.config(bg='light blue')
    opl.pack()
    #triangle area
    opl2 = tk.Label(op, text = 'T For Triangle Area Calculator')
    opl2.config(font=("Ink Free",15))
    opl2.config(bg='light blue')
    opl2.pack()
    opl2 = tk.Label(op, text = 'TP For Triangle Prism Calculator')
    opl2.config(font=("Ink Free",15))
    opl2.config(bg='light blue')
    opl2.pack()
    opl2 = tk.Label(op, text = 'SA For Rect/Square Area')
    opl2.config(font=("Ink Free",15))
    opl2.config(bg='light blue')
    opl2.pack()
    opl2 = tk.Label(op, text = 'RP For Rectangler Prism')
    opl2.config(font=("Ink Free",15))
    opl2.config(bg='light blue')
    opl2.pack()
    opl2 = tk.Label(op, text = 'S For Sphere Volume')
    opl2.config(font=("Ink Free",15))
    opl2.config(bg='light blue')
    opl2.pack()
    opl2 = tk.Label(op, text = 'C For Cicumference Calcalator')
    opl2.config(font=("Ink Free",15))
    opl2.config(bg='light blue')
    opl2.pack()
    opl2 = tk.Label(op, text = 'I For Interest Calculator')
    opl2.config(font=("Ink Free",15))
    opl2.config(bg='light blue')
    opl2.pack()
    def cringe():
            op.destroy()
        
    opb =tk.Button(op,text="Close")
    opb.config(font=("Ink Free",12))
    opb.config(bg="white")
    opb.config(command=cringe)
    opb.pack(side=tk.LEFT)


b2 = tk.Button(root, text = 'Options',font=("Ink Free",12),bg='white',activebackground='white',command=options)
b1_window = can.create_window(35,250, anchor="nw", window=b2)
#)



































root.mainloop()