from tkinter import *
import random
import math
root=Tk()
root.attributes('-alpha',0.3)
g=Canvas(bg='gray89',width=1000,height=500)
g.pack()
pocet=0
pole=[]
lines=[]
def round_down(num, divisor):
    return num - (num%divisor)

for i in range(50):
    for j in range(100):
        g.create_rectangle(j*10,i*10,10+j*10,10+i*10,outline='gray70')
def klik(sur):
    global pocet,x1,x2,x3,y1,y2,y3,a,b,c,pole,lines
    pocet+=1
    if pocet==1:
        x1=round_down(sur.x,10)+5
        y1=round_down(sur.y,10)+5
        b=g.create_line(0,y1,1000,y1,width=2,fill='tomato')
        c=g.create_line(x1,0,x1,500,width=2,fill='tomato')
        a=g.create_rectangle(round_down(sur.x,10),round_down(sur.y,10),round_down(sur.x,10)+10,round_down(sur.y,10)+10,fill='red')

                
    if pocet==2:
        x2=round_down(sur.x,10)+5
        y2=round_down(sur.y,10)+5
        lines.append(g.create_line(x1,y1,x2,y2,fill='red',width='2'))
        pole.append([x1//5,100-y1//5,x2//5,100-y2//5])
        g.delete(a,b,c)
        pocet=0
def delete(sur):
    if len(pole)!=0 and len(lines)!=0:
        g.delete(lines[-1])
        lines.pop()
        pole.pop()
def translate(sur):
    
    for i in range(len(pole)):
        print(f'\qbezier{pole[i][0],pole[i][1]}{(pole[i][0]+pole[i][2])//2,(pole[i][1]+pole[i][3])//2}{pole[i][2],pole[i][3]}')
g.bind('<Button-1>',klik)
g.bind('<Button-3>',delete)
g.bind('<Button-2>',translate)
root.mainloop()
