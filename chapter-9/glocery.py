from collections import OrderedDict

glossary = OrderedDict()

glossary["variable"] = "Name to store data"
glossary["list"] = "Sequence of data of same type"
glossary["dictionary"] = "Sequence of data to store key-value pair data types"
glossary["tuple"] = "Kind of list whilch is immutable"
glossary["string"] = "Data type of multiple characters"
glossary["function"] = "Block of code which only runs when it is called"
glossary["integer"] = "Positive or negative whole number"
glossary["operator"] = "Special symbols that designate that some sort of computation should be performed"
glossary["expression"] = "Combination of operators and operands"
glossary["python"] = "A programming language"

for term, definitionn in glossary.items():
    print(term.title() + "\n\t" + definitionn)