import sys
import os
import datetime

from input_manager import InputManager
from output_manager import OutputManager
from backup_run import Backup


def documentation():
    print("\ninit backup")
    print("-- Creates a new backup")

    print("\ninput add {name} {path}")
    print("-- Add a path to the input directory")
    print("-- Name of the destination directory [NO SPACES] (without braces) e.g 'Pictures'")
    print("   -- If null, input dirs will simply be moved to the output dir with no specified subfolder")
    print("-- Path to folder (without braces) e.g C:/Users/Pictures")

    print("\noutput add {path}")
    print("-- Add and name a path to the output directory")
    print("-- Path to folder (without braces) e.g 'C:/Users/Pictures'")

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
    print("\n#####################################################################")
    print("#                                                                   #")
    print("#               BackupVault - automate your backups!                #")
    print("#                                                                   #")
    print("#####################################################################")

    if not (sys.platform.startswith("win") or sys.platform.startswith("cygwin")):
        print("Error: BackupVault only supports Windows OS")

    inputManager = InputManager()
    outputManager = OutputManager()

    backup = Backup()

    print("\n#   exit\n#   -- To exit")
    print("#\n#   help\n#   -- For command documentation")

    while True:
        print("\nEnter command: ", end='')
        command = input().strip()

        if command == "exit":
            break
        
        if command == "init backup":
            if not inputManager.has_paths() or not outputManager.has_paths():
                print("Missing input and/or output paths")
            else:
                backup.run(True)
        elif command == "help":
            documentation()
        elif command.startswith("input add"):
            name = command[10:10 + command[10:].index(' ')]
            path = command[10 + len(name) + 1:]
            inputManager.add_path(path, name)
        elif command.startswith("output add"):
            outputManager.add_path(command[11:].strip())
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
        else:
            print("Unknown input. Type 'help' for help")
