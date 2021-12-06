str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

import re
str = re.sub("[\.,]", "", str)
split = str.split()

num_alphabet = [len(i) for i in split]
print(num_alphabet)
