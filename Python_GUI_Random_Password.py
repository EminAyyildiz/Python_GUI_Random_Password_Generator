import tkinter as tk
import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):

    letters = string.ascii_letters
    if include_digits:
        letters += string.digits
    if include_special_chars:
        letters += string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

def generate():

    password = generate_password(length_slider.get(), digits_var.get(), special_chars_var.get())
    result_box.delete("1.0", "end")
    result_box.insert("end", password)
def delete():
    result_box.delete("1.0", "end")


window = tk.Tk()
window.title("***Random password Generator***Written by Emin Ayyıldız")

length_label = tk.Label(window, text="Password Length :",font=('times new roman', 20))
length_label.pack()
length_slider = tk.Scale(window, from_=0, to=32, orient=tk.HORIZONTAL)
length_slider.pack()

digits_var = tk.BooleanVar()
digits_checkbutton = tk.Checkbutton(window, text="Include Number", variable=digits_var, onvalue=True, offvalue=False)
digits_checkbutton.pack()
special_chars_var = tk.BooleanVar()
special_chars_checkbutton = tk.Checkbutton(window, text="Include Special Characters", variable=special_chars_var, onvalue=True, offvalue=False)
special_chars_checkbutton.pack()


generate_button = tk.Button(window, text="GENERATE", command=generate)
generate_button.pack()

delete_button = tk.Button(window, text="DELETE", command=delete)
delete_button.pack()


result_box = tk.Text(window, height=3,background='orange',font=('times new roman', 15,"bold"),fg='black')
result_box.pack()


window.mainloop()
