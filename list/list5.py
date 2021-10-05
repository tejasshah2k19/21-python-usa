list = [11,22,33,44,55]

print(list)
list.append(66)
print(list)


list.remove(55)
print(list)

#total number of elements / data in a list
print(len(list))

#count how many times 33 appear
count33 = list.count(33)
print("33 present ",count33," times")


# reverse list
list.reverse()
print(list)


