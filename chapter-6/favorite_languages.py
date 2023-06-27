# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# friends = ['phil', 'sarah', 'erin', 'john']

# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("Hi, " + name.title() + 
#               ", I see your favorite language is " + 
#               favorite_languages[name].title() + ".")
#     if name not in friends:
#         print("Hi, " + name.title() + 
#               ", you are invited to choose your favorite language")

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())





favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel']
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are: ")
        for language in languages:
            print("\t" + language.title())
    elif len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is " + languages[0].title() + ".")
    else:
        print("\n" + name.title() + "has no favorite language.")