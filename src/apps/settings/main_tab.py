from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSlider
from PySide6.QtCore import Qt
from apps.settings.base_tab import BaseTab

class MainTab(BaseTab):
    def __init__(self, master, data_manager, on_update, *args, **kwargs):
        super().__init__(master, data_manager, on_update, *args, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.create_width_slider()
        self.create_length_slider()
        self.create_gap_slider()

    def create_width_slider(self):
        layout = QHBoxLayout()

        # Width label
        self.width_label = QLabel("Width")
        layout.addWidget(self.width_label)

        # Width slider
        self.width_slider = QSlider(Qt.Horizontal)
        self.width_slider.setMinimum(0)
        self.width_slider.setMaximum(50)
        self.width_slider.setValue(self.last_width)
        self.width_slider.valueChanged.connect(lambda value: self.update_width(value))
        layout.addWidget(self.width_slider)

        self.layout().addLayout(layout)

    def update_width(self, value):
        if self.on_update:
            self.on_update('width', value)

    def create_length_slider(self):
        layout = QHBoxLayout()

        self.length_label = QLabel("Length")
        layout.addWidget(self.length_label)

        self.length_slider = QSlider(Qt.Horizontal)
        self.length_slider.setMinimum(0)
        self.length_slider.setMaximum(100)
        self.length_slider.setValue(self.last_length)
        self.length_slider.valueChanged.connect(lambda value: self.update_length(value))
        layout.addWidget(self.length_slider)

        self.layout().addLayout(layout)

    def update_length(self, value):
        if self.on_update:
            self.on_update('length', value)

    def create_gap_slider(self):
        layout = QHBoxLayout()

        # Gap label
        self.gap_label = QLabel("Gap")
        layout.addWidget(self.gap_label)

        # Gap slider
        self.gap_slider = QSlider(Qt.Horizontal)
        self.gap_slider.setMinimum(0)
        self.gap_slider.setMaximum(200)
        self.gap_slider.setValue(self.last_gap)
        self.gap_slider.valueChanged.connect(lambda value: self.update_gap(value))
        layout.addWidget(self.gap_slider)

        self.layout().addLayout(layout)

    def update_gap(self, value):
        if self.on_update:
            self.on_update('gap', value)