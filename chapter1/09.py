import random
str = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

shuffle = []
for str in str.split():
    if len(str) > 4:
        str = str[0] + "".join(random.sample(str[1:-1], len(str) - 2)) + str[-1]
    shuffle.append(str)

print(" ".join(shuffle))
