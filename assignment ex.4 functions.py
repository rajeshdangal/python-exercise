def my_split(sentence, separator):
    result = []
    word = ""
    for char in sentence:
        if char == separator:
            result.append(word)
            word = ""
        else:
            word += char
    result.append(word)
    return result

def my_join(lst, separator):
    result = ""
    for i in range(len(lst)):
        result += lst[i]
        if i < len(lst) - 1:
            result += separator
    return result


sentence = input("Please enter sentence: ")
split_sentence = my_split(sentence, " ")
joined_sentence = my_join(split_sentence, ",")

print(joined_sentence)
for item in split_sentence:
    print(item)
