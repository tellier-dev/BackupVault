from pathlib import Path
import json

def inputAsJson(path):
    return {'path': path}

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
        new_data = inputAsJson(path)
        data = self.getPaths()
        data.append(new_data)
        self.writeDataToJson(data)
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

        self.writeDataToJson(data)
        print('Path has been removed')

    def clear(self):
        self.writeDataToJson(None)
        print('Output directories have been removed')

    def list(self):
        dirs = self.getPaths()
        if len(dirs) <= 0:
            print('No directories exist')
            return 
        for directory in dirs:
            print("Path: {}".format(directory['path']))

    def getPaths(self):
        dirs = []
        with open(self.__file_path, 'r') as json_file:
            data = json.load(json_file)
            if data['directories'] is not None and len(data['directories']) > 0:
                dirs = data['directories']
        return dirs

    def hasPaths(self):
        paths = self.getPaths()
        return paths is not None and len(paths) > 0
    
    def writeDataToJson(self, data):
        with open(self.__file_path, 'w') as out:
            json_data = dataAsJson(data)
            json.dump(json_data, out, indent=4)