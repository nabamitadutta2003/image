import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg *.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        img = img.resize((400, 300))
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk  
root = tk.Tk()
root.title("Simple Image Viewer")
btn = tk.Button(root, text="Open Image", command=open_image, font=("Arial", 14))
btn.pack(pady=10)
label = tk.Label(root)
label.pack()
root.mainloop()