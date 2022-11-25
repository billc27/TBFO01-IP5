from argparse import ArgumentParser
from tokenisasi import create_token
from CFG_config import read_grammar
from CFGtoCNF import convert_CFG_to_CNF
from CYK import CYK_validation

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("nama_file", type=str, help="Nama File...")

    args = argument_parser.parse_args()

    if CYK_validation(convert_CFG_to_CNF(read_grammar("CFG.txt")), create_token(args.nama_file)):
        print("ACCEPTED")
    else:
        print("SYNTAX ERROR")