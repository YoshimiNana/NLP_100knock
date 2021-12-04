def ngram(str, n):
    ngram = []
    for i in range(len(str) - n + 1):
        ngram.append(str[i:i+n])
    return ngram

str = "I am an NLPer"
print("単語bi-gram:", ngram(str.split(), 2))
print("文字bi-gram:", ngram(str, 2))
