import customtkinter as ctk

from core.crosshair import Crosshair

class BaseTab(ctk.CTkFrame):
    def __init__(self, master, data_manager, on_update, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.data_manager = data_manager
        self.on_update = on_update
        self.initialize_last_crosshair()
        
    def initialize_last_crosshair(self):
        last_crosshair = Crosshair.load_from_json(self.data_manager.get_last_crosshair_path())

        self.last_width = last_crosshair.width
        self.last_length = last_crosshair.length
        self.last_gap = last_crosshair.gap

        dot = last_crosshair.get_dot()
        self.last_is_dot = dot.is_it_dot()

        if dot.dot_size is not None:
            self.last_dot_size = dot.dot_size