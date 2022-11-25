def CYK_validation(CNF, string_input):
    string = string_input.split(' ')
    str_len = len(string)
    CYK_table = [[set([]) for j in range(str_len)] for i in range(str_len)]

    for j in range(str_len):
        for head, body in CNF.items():
            for pro_rule in body:
                if len(pro_rule) == 1 and pro_rule[0] == string[j]:
                    CYK_table[j][j].add(head)
        for i in range(j, -1, -1):
            for k in range(i, j):
                for head, body in CNF.items():
                    for pro_rule in body:
                        if len(pro_rule) == 2 and pro_rule[0] in CYK_table[i][k] and pro_rule[1] in CYK_table[k + 1][j]:
                            CYK_table[i][j].add(head)

    # Validation
    if 'S' in CYK_table[0][str_len-1]:
        return True
    else:
        return False