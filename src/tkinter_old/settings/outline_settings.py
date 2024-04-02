import tkinter as tk

class OutlineSettings:
    def __init__(self, tab):
        self.tab = tab
    
    def create_outline_settings(self):
        self.dot_label = tk.Label(self, text="Outline")
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