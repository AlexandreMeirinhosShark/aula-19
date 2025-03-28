import tkinter as tk
import tkintermapview as mapper

root = tk.Tk()
root.title("Portugal")
root.geometry("900x700")

frame = tk.LabelFrame(root)
frame.pack(pady=20)
mapw = mapper.TkinterMapView(frame, width=800, height=600, corner_radius=0)

mapw.set_position(39.81222, -7.99138)

markr = mapw.set_marker(41.8060, -6.7567, text="Bragança")

mapw.set_zoom(7)
mapw.pack()
root.mainloop()
