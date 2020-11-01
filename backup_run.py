import os
import shutil
import numpy

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
        inputManager = InputManager()
        self.input_paths = inputManager.get_paths()

        outputManager = OutputManager()
        self.output_paths = outputManager.get_paths()
    
    def get_new_folders(self, input_folder, output_folder):
        folder_input = get_cleaned_folder_paths(input_folder)
        folder_output = get_cleaned_folder_paths(output_folder)

        new_folders = numpy.setdiff1d(folder_input, folder_output)

        if len(new_folders) <= 0:
            return None
        
        new_folder_paths = []
        print("\nNew folders")
        for fol in new_folders:
            print("New folder - {}".format(fol))
            new_folder_paths.append("{}{}".format(input_folder, fol))
        
        return new_folder_paths

        

    def get_new_files(self, input_folder, output_folder):
        files_input = get_cleaned_file_paths(input_folder)
        files_output = get_cleaned_file_paths(output_folder)

        new_files = numpy.setdiff1d(files_input, files_output)

        if len(new_files) <= 0:
            return None
        
        new_files_paths = []
        print("\nNew files")
        for fil in new_files:
            print("New file - {}".format(fil))
            new_files_paths.append("{}{}".format(input_folder, fil))
        
        return new_files_paths
    
    def get_modified_folders(self, input_folder, output_folder):
        # dive into folder
        x = 3
    
    def get_modified_files(self, input_folder, output_folder):
        # copy file
        x = 3
    
    def remove_deleted_folders(self, input_folder, output_folder):
        folder_input = get_cleaned_folder_paths(input_folder)
        folder_output = get_cleaned_folder_paths(output_folder)

        # print('\nInput')
        # for fol in folder_input:
        #     print(fol)
        # print('\nOutput')
        # for fol in folder_output:
        #     print(fol)

        deleted_folders = numpy.setdiff1d(folder_output, folder_input)

        if len(deleted_folders) <= 0:
            return False

        print("\nDeleted")
        for fol in deleted_folders:
            print("Deleted - {}".format(fol))
            shutil.rmtree("{}{}".format(output_folder, fol))

        return True

    def remove_deleted_files(self, input_folder, output_folder):
        files_input = get_cleaned_file_paths(input_folder)
        files_output = get_cleaned_file_paths(output_folder)

        # print('\nInput')
        # for fil in files_input:
        #     print(fil)
        # print('\nOutput')
        # for fil in files_output:
        #     print(fil)

        deleted_files = numpy.setdiff1d(files_output, files_input)

        if len(deleted_files) <= 0:
            return False

        print("\nDeleted")
        for fil in deleted_files:
            print("Deleted - {}".format(fil))
            os.remove("{}{}".format(output_folder, fil))

        return True
    
    def run(self):
        path = "D:\\Program Files\\World of Warcraft\\_retail_\\Interface\\addons"
        ipt = "C:\\Users\\Povel Galfvensjö\\Desktop\\test_folder\\input\\"
        opt = "C:\\Users\\Povel Galfvensjö\\Desktop\\test_folder\\output\\"
        print(self.get_new_files(ipt, opt))
        print(self.get_new_folders(ipt, opt))

        # list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]
        # list_files_with_paths = [f.path for f in os.scandir(path) if f.is_file()]

        # for p in list_subfolders_with_paths:
        #     stat = os.stat(p)
        #     mod_date = datetime.datetime.fromtimestamp(stat.st_mtime)
        #     print(mod_date)
        
        # for paths in output_paths:



if __name__ == '__main__':
    scr = Backup()
    scr.run()