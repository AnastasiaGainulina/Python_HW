# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.


def ten_popular(text: str) -> list[str]:
    delete = ".,!?;:-[]{}()="
    for i in delete:
        text = text.replace(i, "")
    text = text.lower()
    return sorted(set(text.split()), key=lambda x: text.count(x))[-10:]
text = 'Программирование — это алгоритм, процесс, искусство написания кода. ' \
       'Код пишется для создания программ, при этом разработчики используют разные языки ' \
       'программирования. Каждый язык отличается друг от друга, например, поддерживает разные ' \
       'парадигмы. В свою очередь, изначально правильно выбранный язык может оптимизировать ' \
       'роцесс создания программы, сделать его более продуманным и быстрым. Раньше программирование ' \
       'осуществлялось на машинном коде, но сейчас такой подход практически не используется. ' \
       'Таким образом, программист пишет исходный код, тестируют его и занимается отладкой ' \
       'компьютерной программы.'
print(ten_popular(text))
