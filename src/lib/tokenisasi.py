import re
import sys

tokenData = [
    (r'[ \t]+',                 None),
    (r'\/\/[^\n]*',                None),
    (r'\/\*[^*/]*\*\/',                None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # Number and String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "NUM"),
    (r'[\+\-]?[1-9][0-9]+',     "NUM"),
    (r'[\+\-]?[0-9]',           "NUM"),

    # Delimiter
    (r'\n',                     "NEWLINE"),
    (r'\(',                     "KLKI"), 
    (r'\)',                     "KLKA"),
    (r'\[',                     "KSKI"), 
    (r'\]',                     "KSKA"),
    (r'\{',                     "KKKI"),
    (r'\}',                     "KKKA"),
    (r'\;',                     "TITIKKOMA"), 
    (r'\:',                     "TITIKDUA"),

    # Operator
    (r'\*\*=',                   "POWAS"),
    (r'\*\*',                    "POW"),
    (r'\*=',                    "MULAS"),
    (r'/=',                     "DIVAS"),
    (r'\+=',                    "SUMAS"),
    (r'\++',                    "SUMAS NUM"),
    (r'\-=',                     "SUBAS"),
    (r'\%=',                     "MODAS"),
    (r'\=>',                    "ARROW"),
    (r'\+',                     "ADD"),
    (r'\-',                     "SUB"),
    (r'\*',                     "MUL"),
    (r'/',                      "DIV"),
    (r'%',                      "MOD"),
    (r'<=',                     "LEQ"),
    (r'<',                      "L"),
    (r'>=',                     "GEQ"),
    (r'>',                      "G"),
    (r'!=',                     "NEQ"),
    (r'\==',                    "ISEQ"),
    (r'\=(?!\=)',               "EQ"),

    # Keyword
    (r'\bformat\b',             "FORMAT"),
    (r'\b&&\b',                "AND"),
    (r'\b\|\|\b',                 "OR"),
    (r'\b!\b',                "NOT"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bfalse\b',              "FALSE"),
    (r'\bfrue\b',               "TRUE"),
    (r'\bNone\b',               "NONE"),
    (r'\bin\b',                 "IN"),
    (r'\bclass\b',              "CLASS"),
    (r'\breturn\b',             "RETURN"),
    (r'\bimport\b',             "IMPORT"),
    (r'\braise\b',              "RAISE"),
    (r'\bwith\b',               "WITH"),
    (r'\bas\b',                 "AS"),
    (r'\bvar\b',                "TYPE"),
    (r'\blet\b',                "TYPE"),
    (r'\bconst\b',              "TYPE"),
    (r'\bfuntion\b',            "FUNCTION"),
    (r'\,',                     "COMMA"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "NAME"),
    (r'\w+[.]\w+',              "KARTITIK"),
    (r'\.',                     "TITIK"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
]

# teks ke token
newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lexer(teks, token_exp):
    pos = 0 # posisi karakter pada seluruh potongan teks (absolut)
    cur = 1 # posisi karakter relatif terhadap baris tempat dia berada
    line = 1 # posisi baris saat ini
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in token_exp:
            pattern, tag = t
            # if line == 1:
            #     if pattern == newA:
            #         pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
            #     elif pattern == newB:
            #         pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not match:
            print("ILLEGAL CHARACTER")
            print("SYNTAX ERROR")
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1
    return tokens

def create_token(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    print(char)

    tokens = lexer(char,tokenData)

    return " ".join(tokens)

x = create_token('C:/Users/HP/Documents/Koding/TBFO01-IP5/src/lib/test.txt')
print(x)