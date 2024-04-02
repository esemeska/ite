from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from services.crosshair_manager import CrosshairManager
from apps.crosshair.crosshair_renderer import CrosshairRenderer
from services.data_manager import DataManager
from services.hotkey_listener import HotkeyListener
from apps.settings.settings_app import SettingsApp
from apps.tray_app import AppTray

class CrosshairApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_app()

        self.data_manager = DataManager()
        self.crosshair_manager = CrosshairManager(self.data_manager, self.get_screen_size()) 
        self.renderer = CrosshairRenderer(self, self.crosshair_manager.last_crosshair, self.crosshair_manager)
        self.layout.addWidget(self.renderer)

        self.settings_app = None
        self.initialize_hotkey()

        self.crosshair_visible = True

        screen = QApplication.primaryScreen()
        size = screen.size()
        self.resize(size.width(), size.height())

        self.app_tray = AppTray(self)

    def initialize_hotkey(self):
        self.hotkey_listener = HotkeyListener(self.toggle_settings)
        self.hotkey_listener.activated.connect(self.toggle_settings)
        self.hotkey_listener.start_listener()

    def initialize_app(self):
        self.setWindowTitle("Crosshair App")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

    def toggle_crosshair(self):
        self.update_screen_size()
        self.crosshair_visible = not self.crosshair_visible
        if self.crosshair_visible:
            self.show()
        else:
            self.hide()

    def toggle_settings(self):
        self.update_screen_size()
        if self.settings_app is None or not self.settings_app.isVisible():
            self.settings_app = SettingsApp(self.crosshair_manager, on_update=self.renderer.update_crosshair, parent=self)
        else:
            self.settings_app.destroy()
            self.settings_app = None

    def closeEvent(self, event):
        print("Close Event")
        if self.hotkey_listener is not None:
            self.hotkey_listener.stop_listener()

        if self.settings_app is not None and self.settings_app.isVisible():
            self.settings_app.close()
        event.accept() 

    def exit_app(self):
        self.close()
    
    def update_screen_size(self):
        self.crosshair_manager.update_screen_size(self.get_screen_size())

    def get_screen_size(self):
        screen = QApplication.primaryScreen()
        size = screen.size()
        return [size.width(), size.height()]