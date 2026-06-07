#https://uicookies.com/wp-content/uploads/2019/05/Reg-Form-v5.jpg
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Event Registration Form")
root.geometry("600x650")
root.configure(bg="#2d3748")

# Заголовок формы
title_label = tk.Label(
    root, text="EVENT REGISTRATION FORM", font=("Arial", 16, "bold"),
    bg="#1a202c", fg="white", pady=15
)
title_label.pack(fill="x")

# Главный контейнер для полей
form_frame = tk.Frame(root, bg="white", padx=40, pady=30)
form_frame.pack(fill="both", expand=True, padx=40, pady=20)

# Настройка колонок сетки
form_frame.columnconfigure(0, weight=1)
form_frame.columnconfigure(1, weight=2)
form_frame.columnconfigure(2, weight=2)

# Блок: Name
tk.Label(form_frame, text="Name", font=("Arial", 11, "bold"), bg="white", anchor="w").grid(row=0, column=0, sticky="w", pady=(10, 0))
entry_first_name = tk.Entry(form_frame, bg="#e2e8f0", bd=0, highlightthickness=1, highlightbackground="#cbd5e1")
entry_first_name.grid(row=0, column=1, padx=5, sticky="ew", pady=(10, 0))
entry_last_name = tk.Entry(form_frame, bg="#e2e8f0", bd=0, highlightthickness=1, highlightbackground="#cbd5e1")
entry_last_name.grid(row=0, column=2, padx=5, sticky="ew", pady=(10, 0))

tk.Label(form_frame, text="First Name", font=("Arial", 8), bg="white", fg="gray").grid(row=1, column=1, sticky="nw", padx=5)
tk.Label(form_frame, text="Last Name", font=("Arial", 8), bg="white", fg="gray").grid(row=1, column=2, sticky="nw", padx=5)

# Блок: Company
tk.Label(form_frame, text="Company", font=("Arial", 11, "bold"), bg="white", anchor="w").grid(row=2, column=0, sticky="w", pady=(15, 10))
entry_company = tk.Entry(form_frame, bg="#e2e8f0", bd=0, highlightthickness=1, highlightbackground="#cbd5e1")
entry_company.grid(row=2, column=1, columnspan=2, padx=5, sticky="ew", pady=(15, 10))

# Блок: Email
tk.Label(form_frame, text="Email", font=("Arial", 11, "bold"), bg="white", anchor="w").grid(row=3, column=0, sticky="w", pady=10)
entry_email = tk.Entry(form_frame, bg="#e2e8f0", bd=0, highlightthickness=1, highlightbackground="#cbd5e1")
entry_email.grid(row=3, column=1, columnspan=2, padx=5, sticky="ew", pady=10)

# Блок: Phone
tk.Label(form_frame, text="Phone", font=("Arial", 11, "bold"), bg="white", anchor="w").grid(row=4, column=0, sticky="w", pady=(10, 0))
entry_area_code = tk.Entry(form_frame, bg="#e2e8f0", bd=0, highlightthickness=1, highlightbackground="#cbd5e1")
entry_area_code.grid(row=4, column=1, padx=5, sticky="ew", pady=(10, 0))
entry_phone_num = tk.Entry(form_frame, bg="#e2e8f0", bd=0, highlightthickness=1, highlightbackground="#cbd5e1")
entry_phone_num.grid(row=4, column=2, padx=5, sticky="ew", pady=(10, 0))

tk.Label(form_frame, text="Area Code", font=("Arial", 8), bg="white", fg="gray").grid(row=5, column=1, sticky="nw", padx=5)
tk.Label(form_frame, text="Phone Number", font=("Arial", 8), bg="white", fg="gray").grid(row=5, column=2, sticky="nw", padx=5)

# Блок: Subject
tk.Label(form_frame, text="Subject", font=("Arial", 11, "bold"), bg="white", anchor="w").grid(row=6, column=0, sticky="w", pady=15)
combo_subject = ttk.Combobox(form_frame, values=["Option 1", "Option 2", "Option 3"], state="readonly")
combo_subject.set("Choose option")
combo_subject.grid(row=6, column=1, columnspan=2, padx=5, sticky="ew", pady=15)

# Блок: Radio buttons
tk.Label(form_frame, text="Are you an existing customer?", font=("Arial", 11, "bold"), bg="white").grid(row=7, column=0, columnspan=3, sticky="w", pady=(15, 5))

radio_var = tk.StringVar(value="Yes")
rb_yes = tk.Radiobutton(form_frame, text="Yes", variable=radio_var, value="Yes", bg="white", activebackground="white", fg="#48bb78")
rb_yes.grid(row=8, column=0, sticky="w", padx=5)
rb_no = tk.Radiobutton(form_frame, text="No", variable=radio_var, value="No", bg="white", activebackground="white", fg="gray")
rb_no.grid(row=8, column=1, sticky="w", padx=5)

# Кнопка: Register
btn_register = tk.Button(form_frame, text="REGISTER", bg="#ff4d5a", fg="white", font=("Arial", 10, "bold"), bd=0, height=2, width=15)
btn_register.grid(row=9, column=0, columnspan=2, sticky="w", pady=(30, 0), padx=5)

root.mainloop()
