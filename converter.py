#Created by Swapnil
#Reach at swapnilhbk123@gmail.com

import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def convert_to_jpeg(input_files, format):
    output_folder = "your_path_output"
    for input_file in input_files:
        try:
            im = Image.open(input_file)
            output_file = os.path.join(output_folder, os.path.basename(input_file).replace(f'.{format}', '.jpeg'))
            im.save(output_file, 'jpeg')
            status_label.config(text=f"Conversion successful. Image saved as {output_file}")
        except Exception as e:
            status_label.config(text=f"Error converting image {input_file}: {e}")

def select_files(format):
    files = filedialog.askopenfilenames(title=f"Select .{format} files", filetypes=((f"{format.upper()} files", f"*.{format}"), ("All files", "*.*")))
    if files:
        convert_to_jpeg(files, format)

# Create the main window
root = tk.Tk()
root.title("Image Format Converter")
root.geometry("640x480")
root.configure(bg="#f0f0f0")

# Heading label
heading_label = tk.Label(root, text="Image Format Converter", font=("Segoe UI", 16, "bold"), bg="#f0f0f0")
heading_label.pack(pady=10)

# Button styles
button_style = {"font": ("Segoe UI", 12), "bg": "#0078D7", "fg": "white", "activebackground": "#005a9e", "padx": 15, "pady": 5, "bd": 2}

# Create buttons to select files for conversion
webp_button = tk.Button(root, text="Convert WebP to JPEG", command=lambda: select_files("webp"), **button_style)
webp_button.pack(pady=10)

heic_button = tk.Button(root, text="Convert HEIC to JPEG", command=lambda: select_files("heic"), **button_style)
heic_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="", font=("Segoe UI", 10), bg="#f0f0f0")
status_label.pack(pady=10)

# Run the main event loop
root.mainloop()
