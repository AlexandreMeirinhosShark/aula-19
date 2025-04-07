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
img_bragc = ImageTk.PhotoImage(Image.open(os.path.join(c_path, "images", "Posta-Mirandesa.webp")).resize((70, 70)))

markr = mapw.set_marker(41.8060, -6.7567, text="Bragança", icon=img_bragc)

mapw.set_zoom(7)
mapw.pack()
root.mainloop()
