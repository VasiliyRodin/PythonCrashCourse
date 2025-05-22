from collections import OrderedDict

glossary = OrderedDict()
glossary = {
    "integer" : "a full number",
    "float" : "a number with decible point",
    "variable" : "something that can change",
    "algorith" : "a set of steps a program takes",
    "array" : "a list of items",
    "dictionary" : "a key value pair store"
}
glossary["key1"] = "value1"
glossary["key2"] = "value2"

for term, definition in glossary.items():
    print("Term: " + term + " means: " + definition + "\n")