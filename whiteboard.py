# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different
# data types.

def solution(new_str):
    new_list = new_str.split()
    output = f'{new_list[0]}'
    for word in new_list:
        if len(word) < len(output):
            output = word
    return len(output)

# by Q
def solution(stuff):
    words= stuff.split()
    my_list= []
    for word in words:
        my_list.append(len(word))
    return min(my_list)

# by Brian
def solution(words):
    return min([len(word) for word in words.split()])
