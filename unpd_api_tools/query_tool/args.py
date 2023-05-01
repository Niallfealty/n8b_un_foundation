""" Arg parser for cli args
"""

from argparse import ArgumentParser

parser = ArgumentParser("""
        Cli tool for downloading UNPD WPP data from api.
""")

#parser.add_argument()
#parser.add_subparser()

if __name__ == "__main__":
    args = parser.parse_args()

    print(f"args = {args}")
