filename = input("Название файла: ")
with open (filename, "r", encoding="utf-8") as file:
    txt = file.readlines()
    print("Количество строк: ", len(txt))