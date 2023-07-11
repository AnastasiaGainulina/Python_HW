# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

link ='C//docspython/3/faq/programming.txt'
*_, name = link.split('/')
_, extension = name.split('.')
print(f'{link}, {name}, {extension}')
