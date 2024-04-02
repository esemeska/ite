import tkinter as tk
from tkinter import ttk
from apps.settings.base_tab import BaseTab

class DotTab(BaseTab):
    def __init__(self, master, data_manager, on_update, *args, **kwargs):
        super().__init__(master, data_manager, on_update, *args, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.create_dot_settings()

    def create_dot_settings(self):
        self.dot_label = tk.Label(self, text="Dot")
        self.dot_label.grid(row=3, column=0, pady=4, padx=4)

        self.show_dot_settings = tk.BooleanVar(value=self.last_is_dot)

        self.dot_button = tk.Checkbutton(self, text="Include", takefocus=0, variable=self.show_dot_settings, command=self.update_dot)
        self.dot_button.grid(row=3, column=1, pady=4, padx=4)

        self.dot_size_scale = tk.Scale(self, from_=1, to=20, orient=tk.HORIZONTAL, length=200, command=self.update_dot_size)
        self.dot_settings = [tk.Label(self, text="Size"),
                          self.dot_size_scale,
                          tk.Label(self, text="Color"),
                          tk.Label(self, text="Green")]
        
        self.show_dot_settings.trace_add('write', self.toogle_dot_settings)
        if self.show_dot_settings.get():
            self.toogle_dot_settings()

    def update_dot(self):
        if self.on_update:
            self.on_update('is_dot', self.show_dot_settings.get())
        

    def toogle_dot_settings(self, *args):
        if self.show_dot_settings.get():
            i = 0
            j = 0
            for element in self.dot_settings:
                element.grid(row=4+j, column=i, pady=4, padx=4)
                i += 1
                if i == 2:
                    i = 0
                    j += 1
        
            self.dot_size_scale.set(self.last_dot_size)
        else:
            for element in self.dot_settings:
                element.grid_remove()
        
    def update_dot_size(self, value):
        if self.on_update:
            self.on_update('dot_size', value)
            self.last_dot_size = value