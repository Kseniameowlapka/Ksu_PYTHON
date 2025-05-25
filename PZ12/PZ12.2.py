#Составить генератор (yield), который выводит из строки только буквы.

def letter_generator(s):
    i = 0
    while i < len(s):
        if s[i].isalpha():
            yield s[i]
        i += 1

gen = letter_generator("H3ll0, W0rld!")
print("".join(gen))