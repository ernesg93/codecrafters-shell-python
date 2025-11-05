
"""A simple shell implementation with exit, echo and type command support."""

import sys
import os
import stat
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
                
                # Check if it's a builtin first
                if command_to_check in builtins:
                    print(f"{command_to_check} is a shell builtin")
                
                # If not builtin, search in PATH
                else:
                    found_executable: bool = False
                    
                    # Get PATH from environment, default to empty string
                    path_dirs: str = os.environ.get("PATH", "")
                    
                    # Split PATH using OS-agnostic separator
                    directories: list[str] = path_dirs.split(os.pathsep) if path_dirs else []
                    
                    for directory in directories:
                        # Skip empty directories
                        if not directory:
                            continue
                            
                        # Construct full path to potential executable
                        full_path: str = os.path.join(directory, command_to_check)
                        
                        # Check if file exists and is executable
                        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                            print(f"{command_to_check} is {full_path}")
                            found_executable = True
                            break
                    
                    # If no executable found
                    if not found_executable:
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