strong_word = ""
total = 0

while True:
    word = input()
    if word == "End of words":
        break
    sum_ascii = 0

    for i in range(len(word)):
        sum_ascii += ord(word[i])

    if word[0] in "aeiouyAEIOUY":
        sum_ascii *= len(word)
    else:
        sum_ascii /= len(word)

    if sum_ascii > total:
        strong_word = word
        total = sum_ascii
        
print(f"The most powerful word is {strong_word} - {int(total)}")