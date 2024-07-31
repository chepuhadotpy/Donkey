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

# Настройка изображения машинки
car = tk.PhotoImage(file=r'resources\sprites\car.png')
car_label = tk.Label(window)
car_label.image = car
car_label['image'] = car_label.image
car_y = 280
car_label.place(x=250, y=car_y)
car_label.config(bg='#555555')

car_y_initial = 280

# Функция для передвижения машинки
def move_car(event):
    if car_y == 100:
        return
    else:
        if event.keysym == 'Right':
            car_label.place(x=380)
        elif event.keysym == 'Left':
            car_label.place(x=250)
        winsound.PlaySound(r'resources\sounds\move_car.wav', 1)


window.bind('<KeyPress-Right>', move_car)
window.bind('<KeyPress-Left>', move_car)

# Перезапуск игры
def restart_game():
    global car_y, car_y_initial

    car_y = car_y_initial

    car_label.place(x=250)

    donkey_loses.place(x=1000, y=1000)

    driver_wins_label.place(x=1000, y=1000)

    if car_count['text'] == 10:
        car_count['text'] = int(car_count['text']) * 0
        donkey_count['text'] = int(donkey_count['text']) * 0


# Настройка изображения Donkey
donkey = tk.PhotoImage(file=r'resources\sprites\donkey.png')
donkey_label = tk.Label(window)
donkey_label.image = donkey
donkey_label['image'] = donkey_label.image
donkey_x = 365
donkey_y = -40
donkey_label.place(x=donkey_x, y=donkey_y)
donkey_label.config(bg='#555555')

donkey_y_initial = -1340

# Перезапуск игры в случае, если ослик победил
def restart_game_2():
    global car_y, car_y_initial, donkey_y, donkey_y_initial

    car_y = car_y_initial
    car_label.place(x=250, y=car_y)

    donkey_y = donkey_y_initial

# Функция скрытия меток
def driver_loses_f():
    driver_loses.place(x=1000, y=1000)


# Прячу картинку с текстом о победе ослика
def donkey_wins_f():
    donkey_wins_label.place(x=1000, y=1000)


# Перезапуск игры в случае, если ослик победил со счетом, равным десяти
def restart_game_3():
    global car_y, car_y_initial, donkey_y, donkey_y_initial

    car_y = car_y_initial
    car_label.place(x=250, y=car_y)

    donkey_y = donkey_y_initial

    if donkey_count['text'] == 10:
        donkey_count['text'] = int(donkey_count['text']) * 0
        car_count['text'] = int(car_count['text']) * 0


# Функция для проверки столкновений
def check_collision():
    car_x = car_label.winfo_rootx()
    car_y = car_label.winfo_rooty()

    donkey_x = donkey_label.winfo_rootx()
    donkey_y = donkey_label.winfo_rooty()

    # Условие, если Осел победит
    if car_x >= donkey_x and car_x <= donkey_x + donkey.width() and \
            car_y >= donkey_y and car_y <= donkey_y + donkey.height():
        donkey_points_count()

        winsound.PlaySound(r'resources\sounds\image_collision.wav', 1)

        if donkey_count['text'] < 10:
            driver_loses.place(x=26, y=140)

            restart_game_2()

            window.after(2500, driver_loses_f)
        else:
            donkey_wins_label.place(x=498, y=225)

            restart_game_3()

            window.after(2500, donkey_wins_f)


is_moving = False

# Функция передвижения ослика
def move_donkey():
    global is_moving, donkey_y, car_y

    # Выход в случае, если функция уже работает
    if is_moving:
        return

    # Установить флажок, если функция только начала работу
    is_moving = True

    donkey_y += 50
    donkey_label.place(y=donkey_y)

    # Проверка столкновения
    window.after(1000, check_collision)

    # Условие, если осел достигнет определенной игрек-координаты
    if donkey_y == 360:
        donkey_x = 365 if randint(1, 2) == 1 else 230

        donkey_y = -40
        donkey_label.place(x=donkey_x, y=donkey_y)

        car_y -= 20
        car_label.place(y=car_y)

        # Действия, если водитель победил
        if car_y == 100:
            driver_points_count()

            donkey_x = 1000
            donkey_label.place(x=donkey_x)

            if car_count['text'] < 10:
                donkey_loses.place(x=500, y=140)

                window.after(2500, move_donkey)
                window.after(2500, restart_game)
            else:
                driver_wins_label.place(x=498, y=225)

                window.after(2500, move_donkey)
                window.after(2500, restart_game)
        else:
                window.after(110, move_donkey)

    else:
        window.after(110, move_donkey)

    # Убираю флажок в конце работы функции
    is_moving = False


# Создаю ярлык для дороги
road_label = tk.Label(window)

road_label.place(x=308, y=5)

# Анимирую дорогу
def change_road():
    if car_y == 100:
        return
    else:
        current_time = (int(time.time() * 20) % 3) + 1
        road = tk.PhotoImage(file=r'resources\sprites\doroga_{}.png'.format(current_time))
        road_label.image = road
        road_label['image'] = road_label.image
        road_label.config(bg='#555555')
        window.after(10, change_road)


move_donkey()
change_road()
window.mainloop()