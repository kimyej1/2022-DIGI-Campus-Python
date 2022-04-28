# 09String.py

# text = input("Insert Message in English : ")
# print(text.upper(), end = "")
# print(text.lower(), end = "\tAAA")
# print(text.capitalize())

# for c in text:
#     print(c)


# 대문자로 입력된 것은 소문자로, 소문자는 대문자로 출력하기
# Hello World --> hELLO wORLD

text = input("Insert Message in English : ")

for c in text:
    if c.isupper():
        print(c.lower(), end="")
    elif c.islower():
        print(c.upper(), end="")
    else:
        print(c, end="")

print("\n")
'''
for c in text:
    if c.isupper():
        d = c.lower()
        text = text.replace(c,d)
    elif c.islower():
        d = c.upper()
        text = text.replace(c,d)
    else:
        pass
print(text)
'''
rText = str()
for c in text:
    if c.isupper():
        rText += c.lower()
    elif c.islower():
        rText += c.upper()
    else:
        rText += c
print(rText)

print("text = ", text)
print("swap = ", text.swapcase())

print("-" * 80)

# text를 역순으로 출력하시오.
# rText에 역순을 저장한 후, rText를 출력하시오.
# range(10, -1, -1)
# range(1, 10, 1)

rText = str()
for c in range(len(text)-1, -1, -1):
    rText = rText + text[c]
print(rText)
print(text[::-1])