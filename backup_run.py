import os
import shutil
import numpy
import datetime
from directory import Directory
from distutils import dir_util

from input_manager import InputManager
from output_manager import OutputManager

def get_cleaned_folder_paths(parent):
    paths = [f.path for f in os.scandir(parent) if f.is_dir()]
    cleaned = []
    for path in paths:
        cleaned.append(path[len(parent):])
    return cleaned

def get_cleaned_file_paths(parent):
    paths = [f.path for f in os.scandir(parent) if f.is_file()]
    cleaned = []
    for path in paths:
        cleaned.append(path[len(parent):])
    return cleaned


class Backup:
    def __init__(self):
        self.inputManager = InputManager()
        self.outputManager = OutputManager()

        self.created_backup = False
        self.terminal = False
    
    def load_dirs(self):
        self.input_dirs = self.inputManager.getPaths()
        self.output_dirs = self.outputManager.getPaths()
    
    def terminal_print(self, text):
        if self.terminal:
            print(text)
    
    def move_new_folders(self, input_folder, output_folder):
        folder_input = get_cleaned_folder_paths(input_folder)
        folder_output = get_cleaned_folder_paths(output_folder)

        new_folders = numpy.setdiff1d(folder_input, folder_output)

        if len(new_folders) <= 0:
            return None
        
        self.created_backup = True
        
        # tuple (full_path, folder_name)

        new_folder_paths = []
        for fol in new_folders:
            new_folder_paths.append(("{}{}".format(input_folder, fol), fol))
        
        for fol in new_folder_paths:
            self.terminal_print("Moving {}...".format(fol[0]))
            shutil.copytree(fol[0], output_folder + fol[1])      

    def move_new_files(self, input_folder, output_folder):
        files_input = get_cleaned_file_paths(input_folder)
        files_output = get_cleaned_file_paths(output_folder)

        new_files = numpy.setdiff1d(files_input, files_output)

        if len(new_files) <= 0:
            return None
        
        self.created_backup = True
        
        new_files_paths = []
        for fil in new_files:
            new_files_paths.append("{}{}".format(input_folder, fil))

        for fil in new_files_paths:
            self.terminal_print("Moving {}...".format(fil))
            shutil.copy2(fil, output_folder)

    def get_modified_folders(self, input_folder, output_folder):
        folder_input = [f.path for f in os.scandir(input_folder) if f.is_dir()]
        folder_output = [f.path for f in os.scandir(output_folder) if f.is_dir()]

        # stat tuple - (folderName, modifiedTime)

        input_stats = []
        for p in folder_input:
            stat = (p[len(input_folder):], os.stat(p).st_mtime)
            input_stats.append(stat)

        output_stats = []
        for p in folder_output:
            stat = (p[len(output_folder):], os.stat(p).st_mtime)
            output_stats.append(stat)
        
        modified_folders = []
        unmodified_folders = []
        for in_stat in input_stats:
            out_stat = next((x for x in output_stats if x[0] == in_stat[0]), None)

            if out_stat is None:
                self.terminal_print('ERR - Could not find matching folder: {}'.format(in_stat[0]))
                continue
            
            if in_stat[1] > out_stat[1]:
                modified_folders.append(("{}{}\\".format(input_folder, in_stat[0]), "{}{}\\".format(output_folder, out_stat[0])))
            else:
                unmodified_folders.append(("{}{}\\".format(input_folder, in_stat[0]), "{}{}\\".format(output_folder, out_stat[0])))
        
        return (modified_folders, unmodified_folders)
        
    
    def move_modified_files(self, input_folder, output_folder):
        files_input = [f.path for f in os.scandir(input_folder) if f.is_file()]
        files_output = [f.path for f in os.scandir(output_folder) if f.is_file()]

        # stat tuple - (fileName, modifiedTime)

        input_stats = []
        for p in files_input:
            stat = (p[len(input_folder):], os.stat(p).st_mtime)
            input_stats.append(stat)

        output_stats = []
        for p in files_output:
            stat = (p[len(output_folder):], os.stat(p).st_mtime)
            output_stats.append(stat)
        
        modified_files = []
        for in_stat in input_stats:
            out_stat = next((x for x in output_stats if x[0] == in_stat[0]), None)

            if out_stat is None:
                self.terminal_print('ERR - Could not find matching file: {}'.format(in_stat[0]))
                continue
            
            if in_stat[1] > out_stat[1]:
                modified_files.append("{}{}".format(input_folder, in_stat[0]))
        
        if len(modified_files) <= 0:
            return

        self.created_backup = True

        for fil in modified_files:
            self.terminal_print("Moving {}...".format(fil))
            shutil.copy2(fil, output_folder)
    
    def remove_deleted_folders(self, input_folder, output_folder, delete):
        folder_input = get_cleaned_folder_paths(input_folder)
        folder_output = get_cleaned_folder_paths(output_folder)

        deleted_folders = numpy.setdiff1d(folder_output, folder_input)

        if len(deleted_folders) <= 0:
            return False if delete else None

        folders_for_removal = []
        for fol in deleted_folders:
            folders_for_removal.append("{}{}".format(output_folder, fol))

        if not delete:
            return folders_for_removal

        if len(folders_for_removal) <= 0:
            return
        
        self.created_backup = True

        for fol in folders_for_removal:
            self.terminal_print("Removing {}...".format(fol))
            shutil.rmtree(fol)

    def remove_deleted_files(self, input_folder, output_folder, delete):
        files_input = get_cleaned_file_paths(input_folder)
        files_output = get_cleaned_file_paths(output_folder)

        deleted_files = numpy.setdiff1d(files_output, files_input)

        if len(deleted_files) <= 0:
            return False if delete else None

        files_for_removal = []
        for fil in deleted_files:
            files_for_removal.append("{}{}".format(output_folder, fil))

        if not delete:
            return files_for_removal
        
        if len(files_for_removal) <= 0:
            return
        
        self.created_backup = True
        
        for fil in files_for_removal:
            self.terminal_print("Removing {}...".format(fil))
            os.remove(fil)
    
    def print_path_list(self, tag, path_list):
        if path_list is None or len(path_list) <= 0:
            return

        for path in path_list:
            self.terminal_print("{}: {}".format(tag, path))
    
    def parse_folders(self, in_folder, out_folder):
        if not os.path.exists(out_folder):
            os.mkdir(out_folder)
        self.remove_deleted_files(in_folder, out_folder, True)
        self.remove_deleted_folders(in_folder, out_folder, True)
        
        self.move_new_files(in_folder, out_folder)
        self.move_new_folders(in_folder, out_folder)
        self.move_modified_files(in_folder, out_folder)

        folders = self.get_modified_folders(in_folder, out_folder)

        if (len(folders) <= 0):
            return
        
        # NTFS file systems have a lazy update feature, so folder modified date does not reflect the latest changes in subdirectories
        # FAT file systems don't support update features for folders at all, meaning folders never reflect changes in subdirectories

        # Dive into modified folders
        for modified in folders[0]:
            self.parse_folders(modified[0], modified[1])
        # Dive into unmodified folders
        for unmodified in folders[1]:
            self.parse_folders(unmodified[0], unmodified[1])

    
    def run(self, terminal = False):
        self.load_dirs()
        if terminal:
            self.terminal = True
        for out_dir in self.output_dirs:
            for in_dir in self.input_dirs:
                out_dir_with_name = "{}\\{}".format(out_dir.path, self.inputManager.getNameFromRootPath(in_dir))
                self.terminal_print("\nFrom src: {}".format(in_dir.path))
                self.terminal_print("To dest: {}".format(out_dir.path))
                self.parse_folders(in_dir.path, out_dir_with_name)
        
        if self.created_backup is not True:
            self.terminal_print("\nNo changes detected")
        else:
            self.terminal_print("\nBackup successful")
            self.created_backup = False
        
        self.terminal = False


if __name__ == '__main__':
    scr = Backup()
    scr.run()