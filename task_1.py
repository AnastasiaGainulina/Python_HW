# Решить задачи, которые не успели решить на семинаре:
# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# * Какие вещи взяли все три друга

# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует

# * Для решения используйте операции с множествами.
# * *Код должен расширяться
# на любое большее количество друзей.

dict_friends_things = {'Kenny': ('whater', 'snackes', 'bbq coals'), \
                       'Oleg': ('snackes', 'bbq meat', 'beer'),\
                        'Peter': ('bbq vegetables', 'soda', 'tent')}

# * Какие вещи взяли все три друга
def list_friends_things(dict_list):
    list_thing = []
    for thing in dict_list.values():
        list_thing += thing
    return list_thing


# Какие вещи уникальны, есть только у одного друга
# и имя того, у кого данная вещь отсутствует
count = 0
for i in list_friends_things(dict_friends_things):
    for j in list_friends_things(dict_friends_things):
        if j == i:
            count += 1

def dict_unique_thing (dict_list):
    name_not_thing = []
    new_dict = {}
    count = 0
    for key, value in dict_friends_things.items():
        name_not_thing.append(key)
        new_dict[key] = []
        for j in value:
            for k in list_friends_things(dict_friends_things):
                if k == j:
                    count += 1
            if count == 1:
                new_dict[key] += [j]
            if count > 1:
                name_not_thing.remove(key)
            count = 0
    print("отсутствуют дубли", name_not_thing)
    return new_dict

print(f'Вещи которые взяли все {list_friends_things(dict_friends_things)}')
print(f'Уникальные вещи которые взял каждый {dict_unique_thing(dict_friends_things)}')

