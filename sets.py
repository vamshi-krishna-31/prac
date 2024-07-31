my_set = {1,2,3,4,5,6,7,8,9}
print(my_set)
my_set.add(10)
print(my_set)
my_set.remove(8)
print(my_set)
popped_element = my_set.pop()
print(popped_element, my_set)
my_set.clear()
print(my_set)
set1 = {1,2,3,4,5,6,7,8,9}
set2 = {1,2,3,4,5,6,7,8,9}
union_set = set1.union(set2)
print(union_set)
intersection_set = set1.intersection(set2)
print(intersection_set)
difference_set = set1.difference(set2)
print(difference_set)
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)
update_set = {1,2,3,4,5,6,7,8,9,11}
print(update_set)
update_set.add(8)
print(update_set)
update_set.remove(8)
print(update_set)
subset = {1,2,3}
print(subset)
set1 = {1,2,3,4,5,6,7,8,9}
set1.symmetric_difference_update(set2)
print(set1)
