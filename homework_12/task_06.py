def generate_words(txt):
    word = txt.split()
    count = 0
    while count < len(word):
        yield word[count]
        count += 1


for i in generate_words("мама мыла раму"):
    print(i)

assert ['mom', 'was', 'washing', 'the', 'frame'] == [i for i in generate_words('mom was washing the frame')]
assert ['easy', 'peasy', 'lemon', 'squeezy'] == [i for i in generate_words('easy peasy lemon squeezy')]
assert ['мама', 'мыла', 'окно'] != [i for i in generate_words('mom was washing the frame')]
assert ['easy', 'peasy', 'lemon', 'squeezy'] != [i for i in generate_words('easy_peasy_lemon_squeezy')]
