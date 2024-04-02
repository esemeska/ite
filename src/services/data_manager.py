from core.crosshair import Crosshair
from core.dot import Dot


class DataManager:
    def __init__(self):
        self.default_crosshair_path = 'src/data/default_crosshair.json'
        self.last_crosshair_path = 'src/data/last_crosshair.json'
        

    def get_last_crosshair_path(self) -> str:
        return self.last_crosshair_path
    
    def get_default_crosshair_path(self) -> str:
        return self.default_crosshair_path

    def create_default_crosshair(self):
        default_crosshair = Crosshair(1, 8, 10, Dot(True, 1, None))
        default_crosshair.save_to_json(self.default_crosshair_path)