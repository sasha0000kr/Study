import os
import shutil

users = [
    "Баранова Олега Евгеньевичя",
    "Беляева Глеба Александровича",
    "Бычкова Ильи Павловича",
    "Зяброва Дмитрия Александровича",
    "Иванова Павла Алексеевича",
    "Корнеева Константина Александровича",
    "Коротких Артема Андреевича",
    "Краснова Александра Сергеевича",
    "Курицына Григория Михайловича",
    "Леонова Виктора Владимировича",
    "Лукьянова Никиты Юрьевича",
    "Люмина Сергея Сергеевича",
    "Мишарина Вадима Владимировича",
    "Панина Семёна Александровича",
    "Сафонова Павла Андреевича",
    "Смирнова Олега Васильевича",
    "Сомова Максима Дмитриевича",
    "Стовбы Дмитрия Андреевича",
    "Тагирова Тимура Олеговича",
    "Толкачева Федора Андреевича",
    "Трушина Степана Алексеевича",
    "Тулякова Ярослава Олеговича",
    "Фадеева Антона Витальевича",
    "Цимбалова Даниила Андреевича",
    "Цимбалова Кирилла Андреевича",
    "Черниченко Артема Евгеньевича",
    "Чигриной Марии Алексеевны",
    "Чунина Сергея Андреевича"
]

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