
def map_to_tuples(sequence) -> list:
    return list(map(lambda x: (x.upper(), x.lower()), sequence.split()))


letters = input('Enter letters (use space):  ')

print(map_to_tuples(letters))
