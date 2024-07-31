import tkinter as tk
import time
from random import randint
import winsound

# Создаю объект окна
window = tk.Tk()

# Настраиваю иконку и название окна
window.iconbitmap(r'resources/icon.ico')
window.title('Donkey')


# Задаю размеры окна
window_width = 718
window_height = 418

# Вычисляю координаты окна
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Применяю заранее уточненные данные
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
# Закрепляю размеры окна
window.resizable(False, False)

# Устанавливаю задний фон
window.image = tk.PhotoImage(file=r'resources\sprites\zf.png')
bg = tk.Label(window, image=window.image)
bg.grid(row=0, column=0)
bg.config(bg='#555555')

# Настройка клавиши Escape
def close(event):
    if event.keysym == 'Escape':
        window.destroy()


esc_lbl = tk.Label(window, text='Press Esc to exit', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
esc_lbl.place(x=500, y=345)
window.bind('<KeyPress-Escape>', close)

# Настройка персонажа
donkey_lbl = tk.Label(window, text='Donkey', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
donkey_lbl.place(x=26, y=40)

donkey_count = tk.Label(window, text=0, bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
donkey_count.place(x=26, y=90)

donkey_loses = tk.Label(window, text='Donkey loses!', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
donkey_loses.place(x=1000, y=1000)

# Функция для подсчета очков
def donkey_points_count():
    donkey_count['text'] = int(donkey_count['text']) + 1


donkey_wins = tk.PhotoImage(file=r'resources\sprites\donkey_wins.png')
donkey_wins_label = tk.Label(window)
donkey_wins_label.image = donkey_wins
donkey_wins_label['image'] = donkey_wins_label.image
donkey_wins_label.place(x=1000, y=1000)
donkey_wins_label.config(bg='#555555')

# Настройка машины
car_lbl = tk.Label(window, text='Driver', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
car_lbl.place(x=500, y=40)

car_count = tk.Label(window, text=0, bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
car_count.place(x=500, y=90)

driver_loses = tk.Label(window, text='Driver loses!', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
driver_loses.place(x=1000, y=1000)

# Подсчет очков машины
def driver_points_count():
    car_count['text'] = int(car_count['text']) + 1


driver_wins = tk.PhotoImage(file=r'resources\sprites\driver_wins.png')
driver_wins_label = tk.Label(window)
driver_wins_label.image = driver_wins
driver_wins_label['image'] = driver_wins_label.image
driver_wins_label.place(x=1000, y=1000)
driver_wins_label.config(bg='#555555')
window.mainloop()