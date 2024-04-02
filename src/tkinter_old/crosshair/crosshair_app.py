import sys
import threading
import customtkinter as ctk

from services.crosshair_manager import CrosshairManager
from apps.crosshair.crosshair_renderer import CrosshairRenderer
from services.data_manager import DataManager
from services.hotkey_listener import HotkeyListener
from apps.settings.settings_app import SettingsApp
from apps.tray import AppTray

# Создаем главное окно приложения
class CrosshairApp(ctk.CTk):  # Изменяем базовый класс на CTk из CustomTkinter
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__()
        self.initialize_app()
        
        self.data_manager = DataManager()
        self.crosshair_manager = CrosshairManager(self.data_manager, self.get_screen_size()) 
        self.renderer = CrosshairRenderer(self.canvas, self.crosshair_manager.last_crosshair, self.crosshair_manager)

        self.settings_app = None
        self.hotkey_listener = HotkeyListener(self.toggle_settings)
        self.hotkey_listener.start_listener()

        self.crosshair_visible = True

        self.tray = AppTray(self)
        threading.Thread(target=self.tray.start_tray, daemon=True).start()

    def initialize_app(self):
        self.title("Crosshair App")
        self.attributes("-topmost", True)
        self.attributes('-transparentcolor', 'white')
        self.attributes('-fullscreen', True)
        self.overrideredirect(True)

        # Используем CTkCanvas вместо tk.Canvas
        self.canvas = ctk.CTkCanvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), bg='white', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

    def toggle_crosshair(self):
        self.update_screen_size()
        self.crosshair_visible = not self.crosshair_visible
        if self.crosshair_visible:
            self.deiconify()
        else:
            self.withdraw()
        self.tray.update_tray_menu()

    def toggle_settings(self):
        self.update_screen_size()
        if self.settings_app is None or not self.settings_app.winfo_exists():
            self.settings_app = SettingsApp(self.data_manager, on_update=self.renderer.update_crosshair)
        else:
            self.settings_app.destroy()
            self.settings_app = None

    def exit_app(self):
        if self.hotkey_listener is not None:
            self.hotkey_listener.stop_listener()

        self.tray.stop_tray()

        if self.settings_app is not None and self.settings_app.winfo_exists():
            self.settings_app.destroy()

        self.destroy()
        sys.exit()

    def update_screen_size(self):
        self.crosshair_manager.update_screen_size(self.get_screen_size())

    def get_screen_size(self):
        return [self.winfo_screenwidth(), self.winfo_screenheight()]