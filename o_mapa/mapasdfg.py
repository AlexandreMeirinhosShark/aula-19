import tkinter as tk
import tkintermapview as mapper
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Portugal")
root.geometry("900x700")

frame = tk.LabelFrame(root)
frame.pack(pady=20)
mapw = mapper.TkinterMapView(frame, width=800, height=600, corner_radius=0)

mapw.set_position(39.81222, -7.99138)

c_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
img_bragc = ImageTk.PhotoImage(Image.open(os.path.join(c_path, "images", "braganamem.jpg")).resize((70, 70)))
img_lisb = ImageTk.PhotoImage(Image.open(os.path.join(c_path, "images", "lisboamem.jpg")).resize((70, 70)))
img_porto = ImageTk.PhotoImage(Image.open(os.path.join(c_path, "images", "portomem.jpg")).resize((70, 50)))
img_combr = ImageTk.PhotoImage(Image.open(os.path.join(c_path, "images", "coimbmem.webp")).resize((60, 70)))

markr1 = mapw.set_marker(41.8060, -6.7567, text="Bragança", icon=img_bragc)
markr2 = mapw.set_marker(38.7195, -9.13125, text="Lisboa", icon=img_lisb)
markr3 = mapw.set_marker(41.150000, -8.617000, text="Porto", icon=img_porto)
markr4 = mapw.set_marker(40.267000, -8.400000, text="Coimbra", icon=img_combr)

mapw.set_zoom(7)
mapw.pack()
root.mainloop()
