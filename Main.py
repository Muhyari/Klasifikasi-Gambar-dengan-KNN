from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox
import numpy as np
import model_ai

def quit(exit):
    msg = messagebox.askquestion(title="Exit program",message="Exit?")
    if msg == 'yes':
        root.destroy()
    else:
        return True

root = Tk()

model = model_ai.image_model()

update_text = StringVar()

image = Image.new(mode="1", size=(500,500), color=0)
image_new = ImageTk.PhotoImage(image=image)
label = Label(root, image=image_new)
label.pack()

label_text_image = Label(root, textvariable=update_text, font=("Arial",20))

image_draw = ImageDraw.Draw(image)

final_point = (0, 0)
def start_image_draw(event):
    global image, image_new, final_point
    this_point = (event.x, event.y)
    image_draw.line([this_point, final_point], width=25, fill=255)
    final_point = this_point
    image_new = ImageTk.PhotoImage(image)
    label['image'] = image_new
    label.pack()
    image_resize = image.resize((28,28))
    image_predict = np.array(image_resize)
    image_predict = image_predict.flatten()
    result_image = model.predict([image_predict])
    if result_image[0] == 0:
        update_text.set("LINGKARAN")
    elif result_image[0] == 4:
        update_text.set("KOTAK")
    elif result_image[0] == 3:
        update_text.set("SEGITIGA")
    elif result_image[0] == 1:
        update_text.set("SATU")
    
label_text_image.pack()
def start_draw_layer(event):
    global final_point
    final_point = (event.x, event.y)

def delete_draw_layer(event):
    global image, image_new, image_draw
    image = Image.new(mode="1", size=(500,500), color=0)
    image_new = ImageTk.PhotoImage(image)
    image_draw = ImageDraw.Draw(image)
    label["image"] = image_new
    label.pack()
    
label_tersimpan = Label(root, textvariable=update_text, font=("Arial",20))
   
satu = 0
kotak = 0 
lingkaran = 0
segitiga = 0
def save_image(event):
    global kotak, segitiga, lingkaran, satu
    image_resize = image.resize((28,28))
    if event.char == "k":
        image_resize.save(f"Klasifikasi Gambar/foto/kotak/{kotak}.png")
        kotak += 1
        update_text.set("Gambar Kotak Tersimpan")
    elif event.char == "l":
        image_resize.save(f"Klasifikasi Gambar/foto/lingkaran/{lingkaran}.png")
        lingkaran += 1
        update_text.set("Gambar lingkaran Tersimpan")
    elif event.char == "s":
        image_resize.save(f"Klasifikasi Gambar/foto/segitiga/{segitiga}.png")
        segitiga += 1
        update_text.set("Gambar segitiga Tersimpan")
    elif event.char == "1":
        image_resize.save(f"Klasifikasi Gambar/foto/satu/{satu}.png")
        satu += 1
        update_text.set("Gambar satu Tersimpan")
    elif event.char == "i":
        messagebox.showinfo(title="Info Tombol", message=
                            """
Tombol:
K untuk menyimpan gambar kotak
S untuk menyimpan gambar segitiga
L untuk menyimpan gambar lingkaran
1 untuk menyimpan gambar satu
I untuk melihat info Tombol
                            """)
        

root.bind("<Escape>", lambda exit: quit(exit))
root.bind("<B1-Motion>", start_image_draw)
root.bind("<ButtonPress-1>", start_draw_layer)
root.bind("<ButtonPress-3>", delete_draw_layer)
root.bind("<Key>", save_image)
root.mainloop()