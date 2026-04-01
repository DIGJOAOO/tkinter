import tkinter as tk

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 770
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 106

root = tk.Tk()
root.title("f11")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)

field_img = tk.PhotoImage(file="jugadores/noestoyorgullosodeesto/cancha.png") 

player_paths = [
    "jugadores/noestoyorgullosodeesto/sage.jfif",  
    "jugadores/noestoyorgullosodeesto/yoru.jfif",   
    "jugadores/noestoyorgullosodeesto/kayo.jfif",  
    "jugadores/noestoyorgullosodeesto/brim.jfif", 
    "jugadores/noestoyorgullosodeesto/skye.jfif",  
    "jugadores/noestoyorgullosodeesto/vaper.jfif",  
    "jugadores/noestoyorgullosodeesto/teoj.jfif",  
    "jugadores/noestoyorgullosodeesto/fe.jfif",  
    "jugadores/noestoyorgullosodeesto/veto.jfif",  
    "jugadores/noestoyorgullosodeesto/chamber.jfif",  
    "jugadores/noestoyorgullosodeesto/vaso.jfif" 
]

player_images = [tk.PhotoImage(file=path) for path in player_paths]

field_label = tk.Label(root, image=field_img)
field_label.place(x=0, y=0, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)


positions = [
    (250, 650),  
    (100, 500), (220, 500), (340, 500), (460, 500),  
    (150, 350), (300, 350), (450, 350),  
    (150, 200), (300, 150), (450, 200) 
]

players = []

drag_data = {"widget": None, "x": 0, "y": 0}


def on_press(event):
    drag_data["widget"] = event.widget
    drag_data["x"] = event.x
    drag_data["y"] = event.y


def on_drag(event):
    widget = drag_data["widget"]
    if widget:
        x = widget.winfo_x() + event.x - drag_data["x"]
        y = widget.winfo_y() + event.y - drag_data["y"]
        widget.place(x=x, y=y)


def on_release(event):
    widget = drag_data["widget"]
    if not widget:
        return

    x1, y1 = widget.winfo_x(), widget.winfo_y()

    for other in players:
        if other == widget:
            continue

        x2, y2 = other.winfo_x(), other.winfo_y()

        if abs(x1 - x2) < PLAYER_WIDTH and abs(y1 - y2) < PLAYER_HEIGHT:
            # intercambio
            widget.place(x=x2, y=y2)
            other.place(x=x1, y=y1)
            break

    drag_data["widget"] = None

for i in range(11):
    lbl = tk.Label(root, image=player_images[i], bd=0)
    x, y = positions[i]
    lbl.place(x=x, y=y)

    lbl.bind("<ButtonPress-1>", on_press)
    lbl.bind("<B1-Motion>", on_drag)
    lbl.bind("<ButtonRelease-1>", on_release)

    players.append(lbl)

root.mainloop()