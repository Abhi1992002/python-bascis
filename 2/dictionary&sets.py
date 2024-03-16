## Dictionaries -> key-value pair, unordered, mutable, don't allow duplicate keys

# basics
dict = {
    "name" : "Abhimanyu",
    "age" : 1024,
    "marks" : [100,100,96,10,20],
    1000000 : "million",
    "language" : {
       "python" : True,
       "js"     : True,
       "C#"     : False
    }
}

print(dict["age"])           # output -> 1024, if key not exist -> Error
print(dict[1000000])         # output -> million
new_dict = {}                # empty dictionary

# mutable 
dict["age"] = 1096                # allowed
new_dict["first"] = "abhimanyu"   # allowed

# some important method
print(dict.keys())                # return all keys
                                  # output -> dict_keys(['name', 'age', 'marks', 1000000, 'language'])

print(list(dict.keys()))          # output -> ['name', 'age', 'marks', 1000000, 'language']

dict.values()                     # return all values
print(dict.items())               # return all (key , value) pair as tuples
                                  # output -> dict_items([('name', 'Abhimanyu'), ('age', 1096), ('marks', [100, 100, 96, 10, 20]), (1000000, 'million'), ('language', {'python': True, 'js': True, 'C#': False})])

dict.get("name")                  # output -> "abhimanyu", if key not exist -> return Null
dict.update({"color":"red"})      # add {"color":"red"} inside dict

# --------------------------------------------------------------------------------------------------------------------------------------------

## Sets -> mutable but its elements are immutable and all elements are unique

# basic 
old_set = {1,2,3,4}                   # can only add immutable values (can't add list , dict , set)
new_set = {1,2,2,3}                   # ignore duplicate element
print(new_set)                        # output -> {1, 2, 3}
 
print(type(old_set))                  # output -> <class 'set'>
empty_set = set()                     # empty set

# some important methods
old_set.add(5)                        # add an element
old_set.remove(5)                     # remove an element, Error if doesn't exist
old_set.clear()                       # emptied the set
old_set.pop()                         # remove random element from old_set
old_set.union(new_set)                # combine both set & return new
old_set.intersection(new_set)         # return common elements and return new