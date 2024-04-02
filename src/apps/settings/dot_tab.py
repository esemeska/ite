from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QCheckBox, QSlider
from PySide6.QtCore import Qt
from apps.settings.base_tab import BaseTab

class DotTab(BaseTab):
    def __init__(self, master, data_manager, on_update, *args, **kwargs):
        super().__init__(master, data_manager, on_update, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.create_widgets()

    def create_widgets(self):
        self.create_dot_settings()

    def create_dot_settings(self):
        layout = self.layout()

        self.dot_label = QLabel("Dot")
        layout.addWidget(self.dot_label)

        self.show_dot_settings = QCheckBox("Include")
        self.show_dot_settings.setChecked(self.last_is_dot)
        self.show_dot_settings.stateChanged.connect(self.update_dot)
        layout.addWidget(self.show_dot_settings)

        self.dot_size_slider = QSlider(Qt.Horizontal)
        self.dot_size_slider.setMinimum(1)
        self.dot_size_slider.setMaximum(20)
        self.dot_size_slider.setValue(self.last_dot_size if self.last_dot_size is not None else 1)
        self.dot_size_slider.valueChanged.connect(self.update_dot_size)

        self.dot_size_label = QLabel("Size")

        self.dot_color_label = QLabel("Color: Green")

        dot_settings_layout = QHBoxLayout()
        dot_settings_layout.addWidget(self.dot_size_label)
        dot_settings_layout.addWidget(self.dot_size_slider)
        dot_settings_layout.addWidget(self.dot_color_label)

        layout.addLayout(dot_settings_layout)

        self.toggle_dot_settings()

    def update_dot(self, state):
        is_dot = state
        if self.on_update:
            self.on_update('is_dot', is_dot)
        self.toggle_dot_settings()

    def toggle_dot_settings(self):
        should_show = self.show_dot_settings.isChecked()
        self.dot_size_slider.setVisible(should_show)
        self.dot_size_label.setVisible(should_show)
        self.dot_color_label.setVisible(should_show)

    def update_dot_size(self, value):
        if self.on_update:
            self.on_update('dot_size', value)
            self.last_dot_size = value