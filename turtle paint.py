import tkinter as tk
import turtle
from tkinter import Tk, Frame, Menu
from tkinter import messagebox


root = tk.Tk()
root.iconbitmap("E:\\turtle.ico")
root.state('zoomed')
root.title("Turtle Paint")
root.configure(bg="#ff6600")

#creating canvas
canvas = tk.Canvas(root,height=root.winfo_screenheight(),width=800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) 

draw = turtle.RawTurtle(canvas)

#FUNCTIONS

def forward():
	draw.forward(int(e.get()))



def backward():
	draw.backward(int(e1.get()))



def right():
	draw.right(int(e2.get()))


def left():
	draw.lt(int(e3.get()))


def penupfd():
	draw.penup()
	draw.fd(int(e4.get()))
	draw.pendown()


def penupbd():
	draw.penup()
	draw.bk(int(e5.get()))
	draw.pendown()

def undo():
	draw.undo()


def home():
	draw.home()

def speed():
	draw.speed(int(e6.get()))

def clear():
	draw.clear()

def shape():
	draw.shape(e7.get())

def square():
	draw.fd(100)
	draw.lt(90)
	draw.fd(100)
	draw.lt(90)
	draw.fd(100)
	draw.lt(90)
	draw.fd(100)

def drawcircle():
	draw.circle(80)


def triangle():
	draw.bk(100)
	draw.lt(60)
	draw.fd(100)
	draw.right(120)
	draw.fd(100)

def pentagon():
	draw.fd(100)
	draw.lt(72)
	draw.fd(100)
	draw.lt(72)
	draw.fd(100)
	draw.lt(72)
	draw.fd(100)
	draw.lt(72)
	draw.fd(100)
def hexagon():
	draw.fd(100)
	draw.lt(60)
	draw.fd(100)
	draw.lt(60)
	draw.fd(100)
	draw.lt(60)
	draw.fd(100)
	draw.lt(60)
	draw.fd(100)
	draw.lt(60)
	draw.fd(100)

def octagon():
	draw.fd(100)
	draw.lt(45)
	draw.fd(100)
	draw.lt(45)
	draw.fd(100)
	draw.lt(45)
	draw.fd(100)
	draw.lt(45)
	draw.fd(100)
	draw.lt(45)
	draw.fd(100)
	draw.lt(45)
	draw.fd(100)
	draw.lt(45)
	draw.fd(100)



def hide():
	draw.hideturtle()

def show():
	draw.showturtle()
def save():
	import tkinter as tk
	root1=Tk()
	def o():
		ts = draw.getscreen()
		ts.getcanvas().postscript(file=entry1.get())
		
	lbl=tk.Label(root1,text="add the extension '.eps' with your file name")
	lbl.grid(padx=2, pady=2, row=1, column=0, sticky='nw')
	btna=tk.Button(root1,text="save",command=o)
	btna.grid(padx=2, pady=2, row=3, column=0, sticky='news')
	entry1=tk.Entry(root1)
	entry1.grid(padx=2, pady=2, row=2, column=0, sticky='news')
	root1.mainloop()

#entry boxes
e=tk.Entry(root)#fd entry box
e.grid(padx=2, pady=2, row=1, column=11, sticky='nw')

e1=tk.Entry(root)#bd entry box
e1.grid(padx=2, pady=2, row=2, column=11, sticky='nw')

e2=tk.Entry(root)#turn right entry box
e2.grid(padx=2, pady=2, row=3, column=11, sticky='nw')


e3=tk.Entry(root)#turn left entry box
e3.grid(padx=2, pady=2, row=4, column=11, sticky='nw')

e4=tk.Entry(root)#penup fd entry box
e4.grid(padx=2, pady=2, row=5, column=11, sticky='nw')

e5=tk.Entry(root)#penup bd entry box
e5.grid(padx=2, pady=2, row=6, column=11, sticky='nw')


e6=tk.Entry(root)#penup bd entry box
e6.grid(padx=2, pady=2, row=7, column=11, sticky='nw')

e7=tk.Entry(root)#penup bd entry box
e7.grid(padx=2, pady=2, row=8, column=11, sticky='nw')



#BUTTONS


btn=tk.Button(root,text="forward",bg="black",fg="white",command=forward)
btn.grid(padx=2, pady=1, row=1, column=11)


btn1=tk.Button(root,text="backward",bg="black",fg="white",command=backward)
btn1.grid(padx=2, pady=1, row=2, column=11)


btn2=tk.Button(root,text="turn right",bg="black",fg="white",command=right)
btn2.grid(padx=2, pady=1, row=3, column=11)


btn3=tk.Button(root,text="turn left",bg="black",fg="white",command=left)
btn3.grid(padx=2, pady=1, row=4, column=11)


btn4=tk.Button(root,text="penup forward",bg="black",fg="white",command=penupfd)
btn4.grid(padx=2, pady=1, row=5, column=11)

btn5=tk.Button(root,text="penup backward",bg="black",fg="white",command=penupbd)
btn5.grid(padx=2, pady=1, row=6, column=11)

btn6=tk.Button(root,text="speed",bg="black",fg="white",command=speed)
btn6.grid(padx=2, pady=1, row=7, column=11)

btn7=tk.Button(root,text="change shape",bg="black",fg="white",command=shape)
btn7.grid(padx=2, pady=1, row=8, column=11)


#menubar



  
# create a toplevel menu  

menubar = Menu(root)  
tools = Menu(menubar, tearoff=0)  
tools.add_command(label="undo",command=undo)  
tools.add_command(label="home",command=home)  
tools.add_command(label="clear",command=clear)  
tools.add_command(label="Hide",command=hide)
tools.add_command(label="show",command=show)

tools.add_command(label="save",command=save)
tools.add_command(label="Close")  
  
tools.add_separator()  
  
tools.add_command(label="Exit", command=root.quit)  
  
menubar.add_cascade(label="Tools", menu=tools)  
edit = Menu(menubar, tearoff=0)  

  
edit.add_separator()  
  
edit.add_command(label="Square",command=square)  
edit.add_command(label="Circle",command=drawcircle)  
edit.add_command(label="Triangle",command=triangle)  
edit.add_command(label="Pentagon",command=pentagon)  
edit.add_command(label="Hexagon",command=hexagon)  
edit.add_command(label="Octagon",command=octagon)  

  
menubar.add_cascade(label="Draw", menu=edit)  

root.config(menu=menubar)  


  
root.mainloop()  
