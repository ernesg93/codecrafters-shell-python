
"""A simple shell implementation with exit command support."""

import sys
from typing import NoReturn


def main() -> NoReturn:
    """
    Main REPL loop for the shell.
    
    Continuously reads commands from user input and executes them.
    The shell terminates when the 'exit' command is received.
    """
    while True:
        try:
            # Display prompt
            sys.stdout.write("$ ")
            
            # Wait for user input
            command: str = input().strip()
            
            # Skip empty commands
            if not command:
                continue

            # Handle exit command
            if command == "exit" or command == "exit 0":
                sys.exit(0)
            else:
                # Print the "<command>: command not found" message
                print(f"{command}: command not found")
                
        except EOFError:
            # Handle Ctrl+D - exit gracefully
            print()  # Ensure clean line break
            sys.exit(0)
        except KeyboardInterrupt:
            # Handle Ctrl+C - clear line and continue
            print()  # Move to new line
            continue


if __name__ == "__main__":
    main()