def remove_vowels(let):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda x: x not in vowels, let))


letters = input('Enter letters (use space):  ').lower().split()

print(remove_vowels(letters))
