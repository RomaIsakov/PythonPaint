# Камент

from tkinter import*
import colorsys
#from PIL import ImageGrab

color1 = "#000000"
color2 = "#ffffff"

w = 320
h = 240



def MotionEvent(event, t):
    if t == 1:
        global color1
        c = color1
    else:
        global color2
        c = color2
    create_circle(event.x, event.y, var.get(), tfill = c)
    

def create_circle(x, y, d, tfill = None):
    r = d // 2
    if tfill == None:
        canvas.create_oval(x - r, y - r, x + r, y + r, outline = '')
    else:
        canvas.create_oval(x - r, y - r, x + r, y + r, fill = tfill, outline = '')

def buttonCClick():
    canvas.delete("all")


def ButtonColorGet(background, t):
    if t == 1:
        global color1
        color1 = background
        buttonCurrentColor1["background"] = background
    else:
        global color2
        color2 = background
        buttonCurrentColor2["background"] = background


root = Tk()
root.geometry("880x680+600+300")

canvas = Canvas(root, background = '#ffffff', relief = FLAT)
canvas.bind("<B1-Motion>", lambda e: MotionEvent(e, 1))
canvas.bind("<B3-Motion>", lambda e: MotionEvent(e, 3))
canvas.bind("<ButtonRelease-1>", lambda e: MotionEvent(e, 1))
canvas.bind("<ButtonRelease-3>", lambda e: MotionEvent(e, 3))
canvas.place(x = 0, y = 42, width = 500, height = 420)

buttonC = Button(root, text = "î÷èñòèòü", command = buttonCClick)
buttonC.place(x = 0, y = 0, width = 80, height = 41)

var = IntVar()
var.set(30)
scale = Scale(root,from_=1, to=84, length=300, orient=HORIZONTAL, resolution=1, variable = var)
scale.place(x = 100, y = 0)

buttonCurrentColor1 = Button(root, text = "1", background = color1)
buttonCurrentColor1.place(x = 420, y = 0, width = 41, height = 41)

buttonCurrentColor2 = Button(root, text = "2", background = color2)
buttonCurrentColor2.place(x = 461, y = 0, width = 41, height = 41)


n = 16
m = 8

listH = [i/(n+1)     for i in range(1, n+1)]
listV = [i/(m+1)*255 for i in range(1, m+1)]   

num = 0
frame0 = Frame(root)
frame0.place(x = 501, y = 44)
for i in range(n):
    for j in range(m):
        
        col = colorsys.hsv_to_rgb(listH[i], 1.0, listV[j])
        bcolor = '#%02x%02x%02x' % (round(col[0]), round(col[1]), round(col[2]))
        if num == 0:
            bcolor = "#ffffff"
        elif num == 120:
            bcolor = "#000000"
        b = Button(frame0, width = 2, height = 1, text = str(num), background = bcolor)#text = "(" + str(i) + " " + str(j) + ")"
        b.bind("<ButtonRelease-1>", lambda e, bColor=b["background"]: ButtonColorGet(bColor, 1))
        b.bind("<ButtonRelease-3>", lambda e, bColor=b["background"]: ButtonColorGet(bColor, 3))
        

        b.grid(row = i, column = j)
        num = num + 1
#x = 0
#y = 42
#x1 = 500
#y1 = 482
#ImageGrab.grab().crop((x,y,x1,y1)).save('C:\\Users')
root.mainloop()
