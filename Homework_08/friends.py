from person import Person

my_friends = [Person('Nicolas', 75, 'M'),
              Person('Dan', 21, 'M'),
              Person('Maria', 41,'F'),
              Person('Bred', 29, 'M'),
              Person('Katrin', 36, 'F')]

for friends in my_friends:
    friends.print_person_info()

print()

def get_oldest_person(oldest_friends):
    the_oldest_friend = max(oldest_friends, key=lambda my_friends: my_friends.age)
    return the_oldest_friend

def filter_male_person(friends):
    male_friends = filter(lambda person: person.gender == 'M', friends)
    return list(male_friends)

old_friend = get_oldest_person(my_friends)
male_person = filter_male_person(my_friends)

print('Самый старый друг:  ')
old_friend.print_person_info()
print()
print('Друзья мужского пола:  ')
for friend in male_person:
    friend.print_person_info()

