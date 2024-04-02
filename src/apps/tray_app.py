from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction, QPixmap, QPainter, QColor

class AppTray:
    def __init__(self, app):
        self.app = app

        self.tray_icon = QSystemTrayIcon(QIcon(self.create_icon()), self.app)
        self.tray_icon.setToolTip("Crosshair App")

        self.menu = QMenu()
        toggle_action = QAction(self.crosshair_visibility(), self.menu)
        toggle_action.triggered.connect(self.toggle_crosshair_visibility)
        self.menu.addAction(toggle_action)

        settings_action = QAction("Settings", self.menu)
        settings_action.triggered.connect(self.app.toggle_settings)
        self.menu.addAction(settings_action)

        exit_action = QAction("Exit", self.menu)
        exit_action.triggered.connect(self.app.exit_app)
        self.menu.addAction(exit_action)

        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()

    def create_icon(self) -> QIcon:
        pixmap = QPixmap(64, 64)
        pixmap.fill(QColor("white"))

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(255, 0, 0))
        painter.drawEllipse(0, 0, 64, 64)
        painter.end()

        return QIcon(pixmap)
        

    def toggle_crosshair_visibility(self):
        self.app.toggle_crosshair()
        self.menu.actions()[0].setText(self.crosshair_visibility())
    
    def crosshair_visibility(self) -> str:
        return 'Hide' if self.app.crosshair_visible else 'Show'
    
    def stop_tray(self):
        self.tray_icon.hide()