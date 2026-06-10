import tkinter as tk

root = tk.Tk()
root.title("Перевод из см в метры")
root.geometry("400x250")
root.resizable(False, False)

def calculate_meters():
    try:
        L = int(entry_cm.get())
        A = L // 100
        lbl_result.config(text=f"В метрах = {A}", fg="green")
    except ValueError:
        lbl_result.config(text="Введите число правильно!", fg="red")

lbl_task1 = tk.Label(root, text="Дано расстояние L в сантиметрах.", font=("Arial", 10, "italic"))
lbl_task1.pack(pady=(10, 0))

lbl_task2 = tk.Label(root, text="Найти количество полных метров в нем.", font=("Arial", 10, "italic"))
lbl_task2.pack(pady=(0, 10))

lbl_input = tk.Label(root, text="Введите число в см:", font=("Arial", 11))
lbl_input.pack(pady=5)

entry_cm = tk.Entry(root, font=("Arial", 11), justify="center")
entry_cm.pack(pady=5)
entry_cm.focus()

btn_calc = tk.Button(
    root, 
    text="Рассчитать", 
    font=("Arial", 10, "bold"), 
    command=calculate_meters,
    bg="#e1e1e1"
)
btn_calc.pack(pady=10)

lbl_result = tk.Label(root, text="", font=("Arial", 11, "bold"))
lbl_result.pack(pady=10)

root.mainloop()
