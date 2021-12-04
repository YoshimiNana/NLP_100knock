def cipher(str):
    change = [chr(219-ord(s)) if s.islower() else s for s in str]
    return "".join(change)

str = "There must be a beginning of any great matter"
code = cipher(str)
print("暗号化:", code)
print("復号化:", cipher(code))
