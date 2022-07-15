def greater_minimum_helper(lst, x) -> str:
    for i in lst:
        if i > x:
            return i
    return x


def greater_minimum(word: str):
    for j in reversed(range(len(word))):
        seq = "".join(sorted(word[j:]))
        if greater_minimum_helper(seq, word[j]) != word[j]:
            x = greater_minimum_helper(seq, word[j])
            seq = seq.replace(x, "", 1)
            new_word = word[:j]
            new_word += x
            new_word += seq
            return new_word
    return "no answer"


t = input()
lst = []
for i in range(int(t)):
    lst.append(input())
ans = []
for i in range(int(t)):
    ans.append(greater_minimum(lst[i]))
for i in ans:
    print(i)