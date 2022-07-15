def word_frequency(freq):
    dictionary = {}
    for j in freq:
        if j in dictionary.keys():
            dictionary[j] = dictionary[j] + 1
        else:
            dictionary[j] = 1
    print(len(dictionary.keys()))
    for j in dictionary:
        print(dictionary[j], end=" ")


num = int(input())
lst = []
for i in range(num):
    lst.append(input())
word_frequency(lst)