from core.dot import Dot
from core.descriptors import IntegerValue


class Crosshair:
    width = IntegerValue(0, 50)
    length = IntegerValue(0, 100)
    gap = IntegerValue(0, 200)

    def __init__(self, width: int, length: int, gap: int, dot: Dot):
        self.width = width #0-50
        self.length = length #1-100
        self.gap = gap #0-200
        self.dot = dot

    def get_dot(self) -> Dot:
        return self.dot
    
    def set_dot(self, new_dot):
        self.dot = new_dot

    def __repr__(self) -> str:
        return f"{self.width}-{self.length}-{self.gap}"
    
    @classmethod
    def load_from_json(cls, path_to_file):
        from json import load
        try:
            with open(path_to_file, 'r') as json_file:
                crosshair_data = load(json_file)
            return Crosshair(crosshair_data['width'], crosshair_data['length'], crosshair_data['gap'], Dot.from_json(crosshair_data['dot']))
        except IOError as e:
            print(f"Error when reading a file: {e}")
            return None
    
    def save_to_json(self, path_to_file):
        from os import path, makedirs
        from json import dumps
        
        directory = path.dirname(path_to_file)
        if not path.exists(directory):
            makedirs(directory)

        crosshair_data = {
            "width": self.width,
            "length": self.length,
            "gap": self.gap,
            "dot": self.dot.to_json(),
        }

        json_object = dumps(crosshair_data, indent=3)

        with open(path_to_file, 'w') as json_file:
            json_file.write(json_object)
        


