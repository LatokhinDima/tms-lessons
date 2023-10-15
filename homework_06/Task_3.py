def remove_vowels(let):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    return list(filter(lambda x: x not in vowels, let))


letters = input('Enter letters (use space):  ').split()

print(remove_vowels(letters))
