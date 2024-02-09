text = "abcdefghijklmnop"

for letter in text:
    print(letter)

    i = 0
    while i < len(text):
        print(text[i])
        i +=1

    i = len(text) - 1
    while 1 >= 0:
        print(text[i], end="")
        i -= 1

    print()
    i = 0
    while i < len(text):
        print(text[len(text)], end="")
        i+= 1