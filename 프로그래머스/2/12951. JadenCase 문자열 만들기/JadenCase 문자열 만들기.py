def solution(s):
    # split the string by spaces, and process each word to fit the JadenCase format
    words = s.split(' ')
    
    # process each word to be in JadenCase
    for i in range(len(words)):
        word = words[i]
        if len(word) > 0:
            # if the first character is alphabet, capitalize the first letter and lowercase the rest
            words[i] = word[0].upper() + word[1:].lower()
    
    # join the words back into a single string
    return ' '.join(words)
