
def avg(ranks):
    assert len(ranks) != 0, 'Список ranks не должен быть пустым'
    return round(sum(ranks)/len(ranks))

ranks = [5, 6, 3]
print("Среднее значение:", avg(ranks))
