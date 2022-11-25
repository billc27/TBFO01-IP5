def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    baris = file.readline()
    while baris != "":
        if (baris.startswith('##')):    # ignore comments
            pass
        else:
            # head, body = baris.replace("\n", "").split(" -> ")
            head, *tail = baris.replace("\n", "").split(" -> ")

            if(len(tail) != 0):
                body = tail[0]
                if head not in cfg.keys():
                    cfg[head] = [body.split(" ")]
                else:
                    cfg[head].append(body.split(" "))

        baris = file.readline()

    file.close()
    print(cfg)
    # return cfg

def is_terminal(string):
    list_of_terminal = [
        "LCB",
        "LSB",
        "LRB",
        "RCB",
        "RSB",
        "RRB",
        "ADD",
        "SUB",
        "MUL",
        "DIV",
        "POW",
        "MOD",
        "EQ",
        "ADDEQ",
        "SUBEQ",
        "MULEQ",
        "DIVEQ",
        "POWEQ",
        "MODEQ",
        "E",
        "EE",
        "NE",
        "NEE",
        "L",
        "LE",
        "G",
        "GE",
        "QUESTION",
        "AND",
        "OR",
        "ANDBIT",
        "ORBIT",
        "XORBIT",
        "SAL",
        "SAR",
        "SHR",
        "BREAK",
        "CONTINUE",
        "RETURN",
        "SEMICOLON",
        "COLON",
    ]
    return string in list_of_terminal

def is_variables(string):
    return not is_terminal(string)

read_grammar("CFG.txt")