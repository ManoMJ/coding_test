def solution(word):
    vowel='AEIOU'
    vowels = {char : i for i, char in enumerate(vowel)}
    total = 0
    w = [1+5+25+125+625, 1+5+25+125, 1+5+25, 1+5, 1]
    pos = 0
    for c in word:
        print("total", total)
        total += vowels[c] * w[pos]  + 1
        pos+=1
    return total