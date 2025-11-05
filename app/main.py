
"""A simple shell implementation with exit command support."""

import sys
from typing import NoReturn


def main() -> NoReturn:
    """
    Main REPL loop for the shell.
    
    Continuously reads commands from user input and executes them.
    The shell terminates when the 'exit' command is received.
    """
    # Define the builtin commands
    builtins = {"exit", "echo", "type"}

    while True:
        try:
            # Display prompt
            sys.stdout.write("$ ")
            
            # Wait for user input
            command: str = input().strip()
            
            # Skip empty commands
            if not command:
                continue
            
            # Split command into parts
            parts: list[str] = command.split()
            command_name: str = parts[0]

            # Handle exit command
            if command_name == "exit":
                sys.exit(0)
            
            # Handle echo command
            elif command_name == "echo":
                # Join all arguments with spaces
                text_to_echo: str = " ".join(parts[1:])
                print(text_to_echo)
            
            # Handle type command
            elif command_name == "type":
                if len(parts) < 2:
                    print("type: missing argument")
                    continue
                
                command_to_check: str = parts[1]
                
                if command_to_check in builtins:
                    print(f"{command_to_check} is a shell builtin")
                else:
                    print(f"{command_to_check}: not found")
            
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