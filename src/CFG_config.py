import token

def isTerminal(listTerminal, string):
    return string in listTerminal

def isNonTerminal(string):
    return not isTerminal(string)

def listTerminalGenerator():
    listTerminal = []

    for (reg, code) in token.tokenData:
        listTerminal.append(code)

    return listTerminal

def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    line = file.readline()
    while line != "":
        head, *tail = line.replace("\n", "").split(" -> ")

        if(len(tail) != 0):
            body = tail[0]
            if head not in cfg.keys():
                cfg[head] = [body.split(" ")]
            else:
                cfg[head].append(body.split(" "))

        line = file.readline()

    file.close()

    print(cfg)
    
    return cfg
