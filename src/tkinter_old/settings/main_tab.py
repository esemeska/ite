import tkinter as tk
from tkinter import ttk
from apps.settings.base_tab import BaseTab

class MainTab(BaseTab):
    def __init__(self, master, data_manager, on_update, *args, **kwargs):
        super().__init__(master, data_manager, on_update, *args, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.create_width_scale()
        self.create_length_scale()
        self.create_gap_scale()

    def create_width_scale(self):
        self.width_label = tk.Label(self, text="Width")
        self.width_label.grid(row=0, column=0, pady=4, padx=4)
        self.width_scale = tk.Scale(self, from_=0, to=50, orient=tk.HORIZONTAL, length=300, command=self.update_width)
        self.width_scale.grid(row=0, column=1, pady=4, padx = 4)
        self.width_scale.set(self.last_width)
        
    def update_width(self, value):
        if self.on_update:
            self.on_update('width', value)
    
    def create_length_scale(self):
        self.length_label = tk.Label(self, text="Length")
        self.length_label.grid(row=1, column=0, pady=4, padx=4)
        self.length_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, length=300, command=self.update_length)
        self.length_scale.grid(row=1, column=1, pady=4, padx = 4)
        self.length_scale.set(self.last_length)

    def update_length(self, value):
        if self.on_update:
            self.on_update('length', value)
    
    def create_gap_scale(self):
        self.gap_label = tk.Label(self, text="Gap")
        self.gap_label.grid(row=2, column=0, pady=4, padx=4)
        self.gap_scale = tk.Scale(self, from_=0, to=200, orient=tk.HORIZONTAL, length=300, command=self.update_gap)
        self.gap_scale.grid(row=2, column=1, pady=4, padx = 4)
        self.gap_scale.set(self.last_gap)

    def update_gap(self, value):
        if self.on_update:
            self.on_update('gap', value)
