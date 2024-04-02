from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item

class AppTray:
    def __init__(self, app):
        self.app = app
        self.menu = [item(self.crosshair_visibility(), self.app.toggle_crosshair),
                item('Settings', self.app.toggle_settings),
                item('Exit', self.app.exit_app)]
        
        self.tray_icon = pystray.Icon("name", self.create_icon_image() , "Title", menu=self.menu)

    def stop_tray(self):
        try:
            print("[Tray] Stopping tray icon...")
            self.tray_icon.stop()
            print("[Tray] Tray icon stopped.")
        except Exception as e:
            print("[Tray] Error stopping a tray!")
            raise
        
    def start_tray(self):
        try:
            self.tray_icon.run()
            self.update_tray_menu()
        except Exception as e:
            print("[Tray] Error starting a tray!")
            raise

    def update_tray_menu(self):
        try:
            self.menu[0] = item(self.crosshair_visibility(), self.app.toggle_crosshair)
            self.tray_icon.menu = self.menu
            self.tray_icon.update_menu()
        except Exception as e:
            print("[Tray] Error on menu update!")
            raise

    def create_icon_image(self) -> Image:
        icon_size = (64,64)
        icon_image = Image.new('RGB', icon_size, color='white')
        draw = ImageDraw.Draw(icon_image)
        draw.ellipse((0, 0, icon_size[0], icon_size[1]), fill='black')

        return icon_image

    def crosshair_visibility(self) -> bool:
        return 'Hide' if self.app.crosshair_visible else 'Show'