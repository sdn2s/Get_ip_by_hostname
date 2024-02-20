import socket
import tkinter as tk
from tkinter import messagebox

# Глобальная переменная для хранения введенного URL
entry = None

# Функция для проверки валидности URL
def is_valid_url(url):
    try:
 # Попытка установки соединения с указанным URL с использованием socket.create_connection
        socket.create_connection((url, 80), timeout=2)
        return True
    except OSError:
        return False

# Функция для получения IP-адреса по хостнейму
def get_ip_by_hostname():
    # Получаем введенный URL из текстового поля
    hostname = entry.get()

    # Проверяем валидность введенного URL
    if is_valid_url(hostname):
        try:
            # Пытаемся получить IP-адрес по введенному хостнейму
            ip_address = socket.gethostbyname(hostname)
            # Выводим результат в окне сообщения
            result_text = 'Hostname: {}\nIP address: {}'.format(hostname, ip_address)
            messagebox.showinfo("Result", result_text)
        except socket.gaierror as error:
            # Обрабатываем ошибку, связанную с неверным хостнеймом
            messagebox.showerror("Error", 'Invalid Hostname - {}'.format(error))
        except Exception as error:
            # Обрабатываем общие ошибки, которые могут возникнуть при работе с сетью
            messagebox.showerror("Error", 'Error - {}'.format(error))
    else:
        # В случае невалидного URL выводим сообщение об ошибке
        messagebox.showerror("Error", 'Invalid URL')

# Основная функция программы
def main():
    global entry  # Делаем entry глобальной переменной
    # Создаем главное окно
    root = tk.Tk()
    root.title("IP Address Finder")

    # Создаем и размещаем элементы интерфейса
    label = tk.Label(root, text="Enter website address(URL):")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    button = tk.Button(root, text="Get IP Address", command=get_ip_by_hostname)
    button.pack(pady=10)

    # Запускаем главный цикл событий
    root.mainloop()

# Вызываем основную функцию
if __name__ == '__main__':
    main()
