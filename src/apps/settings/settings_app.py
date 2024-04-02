from PySide6.QtWidgets import QDialog, QVBoxLayout, QTabWidget
from PySide6.QtCore import Qt
from apps.settings.dot_tab import DotTab
from apps.settings.main_tab import MainTab

class SettingsApp(QDialog):
    def __init__(self, crosshair_manager, on_update, parent=None):
        super().__init__(parent)
        self.initialize_app()

        self.crosshair_manager = crosshair_manager
        self.data_manager = self.crosshair_manager.get_data_manager()
        self.on_update = on_update

        self.layout = QVBoxLayout(self)
        self.tab_control = QTabWidget()
        self.layout.addWidget(self.tab_control)
        self.initialize_tabs()
        
        self.move_to_top_left()
        self.show()
        

    def move_to_top_left(self): # Получаем геометрию основного экрана
        screen_size = self.crosshair_manager.get_screen_size()
        x = 200
        y = 50 
        self.move(x, y)

    def initialize_tabs(self):
        self.tab_main = MainTab(self.tab_control, self.data_manager, self.on_update)
        self.tab_dot = DotTab(self.tab_control, self.data_manager, self.on_update)

        self.tab_control.addTab(self.tab_main, "Main")
        self.tab_control.addTab(self.tab_dot, "Dot")
        self.layout.addWidget(self.tab_control)

    def initialize_app(self):
        self.setWindowTitle("Settings")
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.resize(300, 300)
        