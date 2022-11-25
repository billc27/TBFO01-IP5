import re
import token

def comparer(text, tokenData):
    pos = 0
    regexs = []
    tokens = []
    lengthText = len(text)

    for x in tokenData:
        pattern, code = x
        regex = re.compile(pattern)
        regexs.append((regex, code))

    while(pos < lengthText):
        if text[pos] == " ":
            pos += 1

        for regex in regexs:
            reg, code = regex
            isMatch = reg.match(text, pos)

            if isMatch:
                if code:
                    tokens.append(code)
                break
        
        if isMatch:
            pos = isMatch.end(0)
        else:
            print(text[pos])
            print("Error")
            break

    return tokens

def tokenGenerator(tesFile):
    file = open(tesFile)
    char = file.read()
    file.close()

    print(char)

    tokens = " ".join(comparer(char,token.tokenData))

    if len(tokens) != 0:
        tokens += ' '
    tokens += 'EOF'
    print(tokens)


    return tokens