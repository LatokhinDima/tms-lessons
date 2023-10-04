def get_most_frequent_word(txt: str) -> str:
    count = {}
    for i in txt.split():
        count[i] = count.get(i, 0) + 1

    return max(count, key=count.get)


print(get_most_frequent_word("hello this is a string with words and spaces and big big woooooooooord and and and"))
