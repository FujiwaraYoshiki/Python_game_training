import tkinter

key = ""


def key_down(e):
    global key
    key = e.keysym


def main_proc():
    label["text"] = key
    root.after(100, main_proc)


root = tkinter.Tk()
root.title("Real-time keystrokes")
root.bind("<KeyPress>", key_down)
label = tkinter.Label(font=("Times New Romen", 80))
label.pack()
main_proc()
root.mainloop()
