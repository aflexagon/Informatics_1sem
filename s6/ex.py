from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = str(inp.get()) 
        result.set(eval(value))
        ttk.Label(text=f'{result}')
    except ValueError:
        pass
root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

inp = StringVar()
inp_entry = ttk.Entry(mainframe, width=10, textvariable=inp)
inp_entry.grid(column=2, row=1, sticky=(W, E))
result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Number").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="result").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

inp_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()
