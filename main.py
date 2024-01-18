def menu():
    print("Добро пожаловать в (название проекта)!")
    print("Для начала введите - START")
    print("Для выхода введите - EXIT")

while True:
    menu()
    vhod = input()
    if vhod == "START":
        pass
    elif vhod == "EXIT":
        break