import sys

def print_arguments():
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name
    plural_s = 's' if num_args != 1 else ''
    colon_or_dot = ':' if num_args > 0 else '.'

    print(f" argument{plural_s}: {num_args}{colon_or_dot}")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments()
