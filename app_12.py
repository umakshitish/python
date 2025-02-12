# set

# a = [1, 2, 3, 2, 2, 3, 4, 5, 6, 7, 8, 9]

# print(type(a))

# b = set(a)
# print(b)

set1 = {"a", "b", "c", 1}
set2 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
set6 = {4, 9, 11}

# set3 = set1.union(set2) #alternatively
# set3 = set2|set4
# print(set3)


# set1.update(set2)
# print(set1)
# set5 = set2.intersection(set4)
# set5 = set2.intersection(set4, set6) # Alternatively

# set5= set2 & set6

# set2.intersection_update(set4)
# print(set2)

#intersection

set5 = set2.difference(set4) #alternatively

# set5 = set2 - set4  #{1, 2}

# set2.difference_update(set4)  #{1, 2}

#symmetric difference

# set5= set2.symmetric_difference(set4)

# set5 = set2.isdisjoint(set4) # False

#subset

# set5 = set2.issubset(set4) #False

set5 = set2.issuperset(set4)
print(set5) 