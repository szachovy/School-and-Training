from tkinter import *
import math
from PIL import Image, ImageTk

FIELDS = ('insert radiation of sphere','mark distance between spheres centre')

def calculate(entries):
    r = float(entries['insert radiation of sphere'].get())
    d = float(entries['mark distance between spheres centre'].get())

    new_r = math.sqrt((r * r) - (0.25 * d * d))
    P = math.pi * new_r ** 2

    return result.configure(text = "Circle area: " + str(P))

def makeform(root, FIELDS):
    entries = {}
    for field in FIELDS:
       row = Frame(root)
       lab = Label(row, width=35, text=field+": ", anchor='w')
       ent = Entry(row)
       ent.insert(0,"0")
       row.pack(side=TOP, fill=X, padx=5, pady=5)
       lab.pack(side=LEFT)
       ent.pack(side=RIGHT, expand=YES, fill=X)
       entries[field] = ent
    return entries


if __name__ == '__main__':

    root = Tk()
    root.title('Circle area calculator')

    ents = makeform(root, FIELDS)

    root.bind('<Return>', (lambda event, ents: fetch(ents)))

    result = Label(root)
    result.pack(pady=10)

    b1 = Button(root, text='Calculate area',
        command=(lambda e=ents: calculate(e)))
    b1.pack(side=LEFT, padx=5, pady=5)

    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)

    img = ImageTk.PhotoImage(Image.open("circle.png"))

    imageadd = Label(root, image=img)
    imageadd.pack(side=BOTTOM, fill="both", expand="yes", padx=10, pady=10)

    root.mainloop()