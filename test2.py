import tkinter as tk

def on_mouse_down(event):
    c.start = event.x, event.y
    c.oval = c.create_oval(*c.start, *c.start)
def on_mouse_up(event):
    c.oval = None
def on_mouse_move(event):
    if c.oval:
        c.coords(c.oval, *c.start, event.x, event.y)

tk.Label(text="Click and drag below:").pack()
c = tk.Canvas()
c.oval = None
c.pack()
c.bind('<Button>', on_mouse_down)
c.bind('<ButtonRelease>', on_mouse_up)
c.bind('<Motion>', on_mouse_move)

c.mainloop()