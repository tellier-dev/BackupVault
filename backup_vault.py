import sys
from input_manager import InputManager
from output_manager import OutputManager


def documentation():
    print("\ninput add {path}")
    print("-- Add a path to the input directory")
    print("-- Path to folder (without braces) e.g C:/Users/Pictures")

    print("\noutput add {path}")
    print("-- Add a path to the output directory")
    print("-- Path to folder (without braces) e.g C:/Users/Pictures")

    print("\ninput list")
    print("-- List current input directories")

    print("\noutput list")
    print("-- List current output directories")

    print("\ninput remove {path}")
    print("-- Remove path from input directories")
    print("-- Path as listed in list dirs, without braces")

    print("\noutput remove {path}")
    print("-- Remove path from output directories")
    print("-- Path as listed in list dirs, without braces")

    print("\ninput clear")
    print("-- Clear all input directories")

    print("\noutput clear")
    print("-- Clear all output directories")


if __name__ == '__main__':
    print("\nBackupVault - automate your backups!")
    if not (sys.platform.startswith("win") or sys.platform.startswith("cygwin")):
        print("Error: BackupVault only supports Windows OS")

    inputManager = InputManager()
    outputManager = OutputManager()

    print("\nexit\n-- To exit")
    print("\nhelp\n-- For command documentation")

    while True:
        print("\nEnter command: ", end='')
        command = input().strip()

        if command == "exit":
            break

        if command == "help":
            documentation()
        elif command.startswith("input add"):
            inputManager.add_path(command[9:].strip())
        elif command.startswith("output add"):
            outputManager.add_path(command[10:].strip())
        elif command.startswith("input remove"):
            inputManager.remove_path(command[12:].strip())
        elif command.startswith("output remove"):
            outputManager.remove_path(command[13:].strip())
        elif command.startswith("input clear"):
            inputManager.clear()
        elif command.startswith("output clear"):
            outputManager.clear()
        elif command.startswith("input list"):
            inputManager.list()
        elif command.startswith("output list"):
            outputManager.list()