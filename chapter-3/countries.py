countries = ["bangladesh", "india", "USA", "england", "indonesia", "soudi arabia"]
# 1. print the list
print(countries)

# 2. Accessing element of the list and use string methods to the elemnts
print(countries[0].title())
print(countries[1].title())
print(countries[2].title())
print(countries[3].title())
print(countries[4].title())
print(countries[5].title())

# 3. Using the elements to print a sentence
print("I live in " + countries[0].title() + ".")
print("I visited " + countries[1].title() + " last year.")
print("I went to " + countries[2].title() + " to parsute my degree 3 years ago.")
print("I went to " + countries[3].title() + " for a labwork 2 years ago.")
print("I visited " + countries[4].title() + " 4 years ago")
print("I will go to do Hazz " + countries[5].title() + " next year.")

# 4. changing element in a list
countries[1] = "uganda"
print(countries)

# 5. appending element in a list
countries.append("india")
print(countries)

# 6. Inserting element to a definite position in a list
countries.insert(2, "austrelia")
print(countries)

# 7. Removing an element from a list by del method
del countries[0]
print(countries)

# 8. Removing an element from a list by pop() method at any position and retrieve it
deleted_country = countries.pop(2)
print(deleted_country)
print(countries)

# 9. Removing an item from list by value
countries.remove('indonesia')
print(countries)

# 10. Sorting elements in alphabetical order
countries.sort()
print(countries)

# 11. Sorting elemnts in alphabetical order reversely
countries.sort(reverse = True)
print(countries)

# 12. We can also sort by sorted() function
sorted_countries = sorted(countries)
print(sorted_countries)

# 13. Printing a list in reverse order
countries.reverse()
print(countries)

# 14. Finding length of a list
print(len(countries))