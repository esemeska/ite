from core.crosshair import Crosshair


class CrosshairManager:
    def __init__(self, data_manager, screen_size) -> None:
        self.data_manager = data_manager
        self.screen_size = screen_size
        self.default_crosshair = None
        self.last_crosshair = None
        self.load_crosshair()

    def load_crosshair(self):
        self.data_manager.create_default_crosshair()
        self.default_crosshair = Crosshair.load_from_json(self.data_manager.get_default_crosshair_path())

        last_crosshair = Crosshair.load_from_json(self.data_manager.get_last_crosshair_path())
        if last_crosshair is None:
            self.last_crosshair = self.default_crosshair
        else:
            self.last_crosshair = last_crosshair

    def get_data_manager(self):
        return self.data_manager
    
    def update_screen_size(self, new_screen_size):
        self.screen_size = new_screen_size

    def get_screen_size(self):
        return self.screen_size