#!/usr/bin/env python3

names = [ "Anna Smith", 
          "John Anderson", 
          "Cliff Bates",
          "Jeffrey Sinclair",
          "Michael Garibaldi",
          "Susan Ivanova",
          "John Sheridan",
          "Delenn",
          "Kosh",
          "G'Kar",
          "Valen",
          "Zathras"
        ]

def by_last(full_name):
    # split on whitespace and use final element as lastname
    last_name = full_name.split()[-1]
    return (last_name, full_name) # note return of tuple

# sort using helper function to extract sorting key
sorted_names1 = sorted(names, key=by_last)
print("Sort using function reference:")
print("\n".join(sorted_names1))

# alternate way to specify a key function with a lambda
sorted_names2 = sorted(names, key=lambda full: (full.split()[-1], full))
print("\nSort using lambda:")
print("\n".join(sorted_names2))
