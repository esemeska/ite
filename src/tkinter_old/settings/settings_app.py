import tkinter as tk
from tkinter import ttk

from apps.settings.dot_tab import DotTab
from apps.settings.main_tab import MainTab

class SettingsApp(tk.Toplevel):
    def __init__(self, data_manager, on_update):
        super().__init__()
        self.title("Settings")
        self.attributes("-topmost", True)
        self.geometry("400x300")

        self.data_manager = data_manager
        self.on_update = on_update

        self.tab_control = ttk.Notebook(self)
        self.initialize_tabs()

    def initialize_tabs(self):
        self.tab_main = MainTab(self.tab_control, self.data_manager, self.on_update)
        self.tab_dot = DotTab(self.tab_control, self.data_manager, self.on_update)

        self.tab_control.add(self.tab_main, text="Main")
        self.tab_control.add(self.tab_dot, text="Dot")
        self.tab_control.pack(expand=1, fill='both')
