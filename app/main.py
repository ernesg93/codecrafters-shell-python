import sys


def main():
    while True:
        sys.stdout.write("$ ")
        # Wait for user input
        command = input().strip()
        
        if not command:
            continue

        if command == "exit":
            sys.exit(0)
        else:
            # Prints the "<command>: command not found" message
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()

