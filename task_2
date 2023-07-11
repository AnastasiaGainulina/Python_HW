names = ['fierst', 'second', 'thierd']
wages = [10, 20, 50]
percentages = ['10.25%', '10.25%', '10.25%']


def wage_generator(names: list[str], wages: list[int], percentages: list[str]) -> dict[str: float]:
    return {name: wage / 100 * percent
        for name, wage, percent in zip(names, wages, (float(i[:-1]) for i in percentages))}.items()


print(*(wage_generator(names, wages, percentages)))
