from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    file_path = askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    text_area.delete(1.0, END)
    with open(file_path, "r") as file:
        text_area.insert(END, file.read())
    window.title(f"{file_path} - Text Editor")

def save_file():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    with open(file_path, "w") as file:
        file.write(text_area.get(1.0, END))
    window.title(f"{file_path} - Text Editor")

window = Tk()
window.title("Text Editor")

text_area = Text(window, font=("Helvetica", 12))
text_area.pack(expand=True, fill=BOTH)

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)
window.mainloop()

