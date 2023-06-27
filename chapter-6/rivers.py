rivers = {
    'nile':'africa',
    'amazon':'brazil',
    'yangtze':'China'
    }
print("Here are the rivers mentioned in the dictionary above:")
for river in rivers.keys():
    print(river.title())

print("\nHere are the countries mentioned in the dictionary above:")
for country in rivers.values():
    print(country.title())