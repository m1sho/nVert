from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import PIL.ImageOps
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import PIL


metadata_Erase = False

root = tk.Tk()
root.title('NVert')
root.resizable(False, False)
root.geometry('300x150')


def select_files():
    metadata_Erase = True
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')

    )

    filenames = fd.askopenfilename(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Image Inverted:',
        message=filenames

    )


    if metadata_Erase == True:
        image_file = Image.open(filenames)
        image_file.load()
        image_data = np.asarray(image_file, dtype=np.uint8)

        inverted_image = PIL.ImageOps.invert(image_file)

        inverted_image.save("inverted copy.jpg")



# open button
open_button = ttk.Button(
    root,
    text='Select Photos to Invert',
    command=select_files




)





open_button.pack(expand=True)

root.mainloop()

