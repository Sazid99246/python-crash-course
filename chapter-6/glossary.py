glossary = {
    "variable": "Name to store data",
    "list": "Sequence of data of same type",
    "dictonary": "Sequence of data to store key-value pair data types",
    "tuple": "Kind of list whilch is immutable",
    "string": "Data type of multiple characters",
    "function": "Block of code which only runs when it is called",
    "integer":"Positive or negative whole number",
    "operator":"Special symbols that designate that some sort of computation should be performed",
    "expression":"Combination of operators and operands",
    "python":"A programming language"
}

for term, definitionn in glossary.items():
    print(term.title() + "\n\t" + definitionn)