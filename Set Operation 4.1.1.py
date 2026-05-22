set_a = set(map(int, input("Set A: ").split()))
set_b = set(map(int, input("Set B: ").split()))

union_set = set_a.union(set_b)

intersection_set = set_a.intersection(set_b)

difference_set = set_a.difference(set_b)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
