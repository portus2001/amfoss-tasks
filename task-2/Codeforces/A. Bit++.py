n = int(input())
lst = []
for i in range(n):
    c = input()
    lst.append(c)
print(lst.count("X++")+lst.count("++X")-lst.count("X--")-lst.count("--X"))
