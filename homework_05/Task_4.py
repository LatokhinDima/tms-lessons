def get_longest_word(txt: str) -> str:
    return max(txt.split(), key=len)

print(get_longest_word("hello this is a string with words and spaces and big big woooooooooord"))
