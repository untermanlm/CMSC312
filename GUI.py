import tkinter as tk

root = tk.Tk()
e = tk.Entry(root)
e.pack()

def callback(*args):
    msg = e.get()
    if ('LOAD' in msg):
        try:
            fileName = msg[5:]
            f = open(fileName, 'r')
            print(f.readlines())
        except OSError:
            print("Not a valid file")
    elif ('SETPROC' in msg):
        try:
            numProcesses = int(msg[8:])
            print(f'Initializing {numProcesses} processes.')
        except ValueError:
            print('Invalid number of processes.')
    elif (msg == 'STATS'):
        print('Printing stats!')
    elif('SUSPEND' in msg):
        try:
            numCycles = int(msg[8:])
            print(f'Suspending processes after {numCycles} cycles.')
        except ValueError:
            print('Invalid number of cycles.')


    else:
        print(-1)

e.bind("<Return>",callback)
root.mainloop()