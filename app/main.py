import sys


def main():
    sys.stdout.write("$ ")

    # Wait for user input
    command = input()

    # Prints the "<command>: command not found" message
    print(f"{command}: command not found")


if __name__ == "__main__":
    main()
