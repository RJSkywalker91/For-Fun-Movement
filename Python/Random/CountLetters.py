import sys
alphaCounter = {
    'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0,
    'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0,
    'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0,
    'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0,
    'q' : 0, 'r' : 0, 's' : 0, 't' : 0,
    'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0,
    'y' : 0, 'z' : 0
}
numberCounter = {
    0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0,
    5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0
}
punctuationCounter = {
    '`' : 0, '~' : 0, '!' : 0, '@' : 0, '#' : 0, '$' : 0, '%' : 0, '^' : 0,
    '&' : 0, '*' : 0, '(' : 0, ')' : 0, '-' : 0, '_' : 0, '=' : 0, '+' : 0,
    '[' : 0, ']' : 0, '{' : 0, '}' : 0, ';' : 0, ':' : 0, '"' : 0, ',' : 0,
    '<' : 0, '.' : 0, '>' : 0, '/' : 0, '?' : 0, '\'' : 0
}
words = 0

fileName = sys.argv[1]
if(not fileName or fileName == ""):
    print("No file name supplied. Wah wah")
    exit

with open(fileName, "r") as f:
    while True:
        char = f.read(1).lower()
        if not char:
            break
        if char in alphaCounter:
            alphaCounter[char] += 1
        elif char in numberCounter:
            numberCounter[char] += 1
        elif char in punctuationCounter:
            punctuationCounter[char] += 1    
        if char == " ":
            words += 1

sortedAlphaDict = dict(sorted(alphaCounter.items(), key=lambda item: item[1]))
sortedNumberDict = dict(sorted(numberCounter.items(), key=lambda item: item[1]))
sortedPunctDict = dict(sorted(punctuationCounter.items(), key=lambda item: item[1]))
print("\n")
print("All letters: %s\n" % sortedAlphaDict)
print("All numbers: %s\n" % sortedNumberDict)
print("All punctuation: %s\n" % sortedPunctDict)
print("Total words: %s" % words)