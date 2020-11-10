from pathlib import Path
from directory import Directory
import json

def dataAsJson(data):
    if data is None:
        data = []
    json_data = {}
    json_data['directories'] = data
    return json_data


class OutputManager:
    def __init__(self):
        self.__file_path = "output.json"
        doc = Path(self.__file_path)
        if not doc.is_file():
            with open(self.__file_path, 'w') as out:
                data = {}
                data['directories'] = []
                json.dump(data, out, indent=4)

    def addPath(self, path):
        new_data = Directory(path=path)
        data = self.getPaths()
        data.append(new_data)
        self.writeDirectoriesToJson(data)
        print('Path added')

    def removePath(self, path):
        removed = False
        data = self.getPaths()
        for directory in data:
            if directory['path'] == path:
                data.remove(directory)
                removed = True

        if not removed:
            print("> Could not find path <")
            return

        self.writeDirectoriesToJson(data)
        print('Path has been removed')

    def clear(self):
        self.writeDirectoriesToJson(None)
        print('Output directories have been removed')

    def list(self):
        dirs = self.getPaths()
        if len(dirs) <= 0:
            print('No directories exist')
            return 
        for directory in dirs:
            print("Path: {}".format(directory.path))

    def getPaths(self):
        dirs = []
        with open(self.__file_path, 'r') as json_file:
            data = json.load(json_file)
            if data['directories'] is not None and len(data['directories']) > 0:
                for data_dir in data['directories']:
                    directory = Directory(dictionary=data_dir)
                    dirs.append(directory)
        return dirs

    def hasPaths(self):
        paths = self.getPaths()
        return paths is not None and len(paths) > 0
    
    def writeDirectoriesToJson(self, directories):
        data = []
        for directory in directories:
            data.append(directory.asJson())
        with open(self.__file_path, 'w') as out:
            json_data = dataAsJson(data)
            json.dump(json_data, out, indent=4)
