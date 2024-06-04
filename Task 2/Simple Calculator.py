import tkinter as tk
def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))
def clear():
    input_text.set("")
def evaluate():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except Exception as e:
        input_text.set("Error")
root = tk.Tk()
root.title("Calculator")
root.geometry("550x500")
root.config(bg="#333")
input_text = tk.StringVar()
input_frame = tk.Frame(root, width=312, height=50, bd=0, bg="#333")
input_frame.pack(side=tk.TOP, pady=10)
input_field = tk.Entry(input_frame, font=('Helvetica', 18), textvariable=input_text, width=39, bg="#222", fg="#FFF", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0, ipady=10)
buttons_frame = tk.Frame(root, width=312, height=272.5, bg="#333")
buttons_frame.pack()
button_texts = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]
for i, row in enumerate(button_texts):
    for j, text in enumerate(row):
        if text == 'C':
            btn = tk.Button(buttons_frame, text=text, width=10, height=3, bg="#FF6347", fg="white", font=("Helvetica", 14), command=clear)
        elif text == '=':
            btn = tk.Button(buttons_frame, text=text, width=10, height=3, bg="#32CD32", fg="white", font=("Helvetica", 14), command=evaluate)
        else:
            btn = tk.Button(buttons_frame, text=text, width=10, height=3, bg="#4CAF50", fg="white", font=("Helvetica", 14), command=lambda x=text: button_click(x))
        btn.grid(row=i, column=j, padx=5, pady=5)
root.mainloop()
