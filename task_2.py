# Напишите однострочный генератор словаря, который принимает на вход 
# три списка одинаковой длины: имена str, ставка int, премия str 
# с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой 
# премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии




names = ['fierst', 'second', 'thierd']
wages = [10, 20, 50]
percentages = ['10.25%', '10.25%', '10.25%']


def wage_generator(names: list[str], wages: list[int], percentages: list[str]) -> dict[str: float]:
    return {name: wage / 100 * percent
        for name, wage, percent in zip(names, wages, (float(i[:-1]) for i in percentages))}.items()


print(*(wage_generator(names, wages, percentages)))
