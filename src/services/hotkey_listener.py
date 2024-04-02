from pynput import keyboard
import logging
from PySide6.QtCore import QObject, Signal

class HotkeyListener(QObject):
    activated = Signal()

    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.listener = None
        logging.basicConfig(level=logging.INFO)

    def start_listener(self):
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<ctrl>+<alt>+1'),
            self.on_activate)
        
        def for_canonical(f):
            return lambda k: f(self.listener.canonical(k))

        self.listener = keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release))
        self.listener.start()
        logging.info("Listener started!")

    def on_activate(self):
        self.activated.emit()
        logging.info("Callback activated!")

    def stop_listener(self):
        if self.listener is not None:
            self.listener.stop()
            logging.info("Listener stoped!")