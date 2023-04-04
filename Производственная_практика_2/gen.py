import os
import shutil
import json


for get_user in users:
    print("Обработка файла \033[1m" + get_user + "\033[0m")
    shutil.copy2("main.tex", "work.tex")
    os.rename("work.tex", "Отчет " + get_user+".tex")

    print("Запись метаданных в файл " + "name.tex")
    f = open("name.tex", 'w+')
    print("Получение доступа к файлу")
    f.write(get_user)
    print("Запись метаданных в файл: " + str(get_user))
    f.close()
    print("Закрытие файла")

    for i in range(4):
        os.system('pdflatex -file-line-error "Отчет {}.tex"'.format(get_user))
    os.rename("Отчет " + get_user+".tex", "work.tex")

print ("\a\033[7m   Выполнение завершено!\033[0m")