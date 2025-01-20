s = {1,4,5,3,55,234}
print(type(s))
print(s)

print(len(s))

s.remove(55)

print(s)

s.pop()
print(s)

s.pop()
print(s)

s.clear()
print(s)

s.add(6)
print(s)


# Set Union and Set Intersections

s1 = {1, 23, 221}
s2 = {23, 22, 112}

print(s1.union(s2))
print(s1.intersection(s2))


