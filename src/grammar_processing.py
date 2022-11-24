def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    baris = file.readline()
    while baris != "":
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
        "EQ",
        "ISEQ",
        "KBKI",
        "KBKA",
        "TITIKKOMA",
        "TITIKDUA",
        "ADD",
        "SUB",
        "MUL",
        "DIV",
        "MOD",
        "POW",
        "FLOORDIV",
        "LEQ",
        "L",
        "GEQ",
        "G",
        "NEQ",
        "SUBAS",
        "MULAS",
        "SUMAS",
        "DIVAS",
        "MODAS",
        "POWAS",
        "FLOORDIVAS",
        "AND",
        "OR",
        "NOT",
        "IF",
        "THEN",
        "ELSE",
        "ELIF",
        "WHILE",
        "RANGE",
        "FALSE",
        "TRUE",
        "NONE",
        "BREAK",
        "AS",
        "CLASS",
        "CONTINUE",
        "DEF",
        "FOR",
        "FROM",
        "FORMAT",
        "IMPORT",
        "IN",
        "IS",
        "RETURN",
        "RAISE",
        "PASS",
        "WITH",
        "COMMA",
        "KARTITIK",
        "TITIK",
        "PETIKSATU",
        "PETIKDUA",
        "KSKI",
        "KSKA",
        "KKKI",
        "KKKA",
        "INT",
        "STRING",
        "MULTILINE",
        "ID",
        "NEWLINE",
        "TYPE",
        "ARROW"
    ]
    
    return string in list_of_terminal

def is_variables(string):
    return not is_terminal(string)

read_grammar("newCFG.txt")