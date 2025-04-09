import tkinter as tk

# Constants
WIDTH, HEIGHT = 400, 400
SPEED = 8

posx = 0
posy = 0
# Initial setup
root = tk.Tk()
root.title("Move the Square")
# Create the square
x, y = WIDTH // 2, HEIGHT // 2
root.geometry("10x100+0+0")

# Movement tracking
keys_pressed = {"Left": False, "Right": False, "Up": False, "Down": False}


def update_position():
    global posx, posy
    dx = dy = 0
    if keys_pressed["Left"]:
        dx -= SPEED
    if keys_pressed["Right"]:
        dx += SPEED
    if keys_pressed["Up"]:
        dy -= SPEED
    if keys_pressed["Down"]:
        dy += SPEED
    posx += dx
    posy += dy
    root.geometry(f"200x200+{posx}+{posy}")
    root.after(16, update_position)  # ~60 FPS


def key_press(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = True


def key_release(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = False


# Bind key events
root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

# Start the loop
update_position()
root.mainloop()
