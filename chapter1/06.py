def ngram(str, n):
    ngram = []
    for i in range(len(str) - n + 1):
        ngram.append(str[i:i+n])
    return ngram

str1 = "paraparaparadise"
str2 = "paragraph"
X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合:", X - Y)
print("Xにseが含まれる:", "se" in X)
print("Yにseが含まれる:", "se" in Y)
