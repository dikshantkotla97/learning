dict={
    "fast":"quick manner",
    "dikshant":"ok",
    "marks":[1,2,3,],
    "nested dict":{"game":"player"},
    1:2
    }
print(dict["marks"])
print(dict["nested dict"]["game"])
print(list(dict.keys()))
print(dict.keys())
print(dict.values())
print(dict.items())
dict.update({"abc":"xyz","dikshant":"amaze"})
print(dict)
print(dict.get("dikshant")) #returns none if not present in dictionary
print(dict["dikshant"]) #throws error if not present


