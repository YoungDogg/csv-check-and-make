import tkinter as tk
from tkinter import filedialog

def select_folder():
    root.directory = filedialog.askdirectory()
    print(f"Selected Folder: {root.directory}")
    # You can add your processing function call here

root = tk.Tk()
root.title("Folder Selection")
root.geometry("400x200")

select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=20)

root.mainloop()

#something
