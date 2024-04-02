from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QBrush
from PySide6.QtCore import Qt

class CrosshairRenderer(QWidget):
    def __init__(self, parent, crosshair, crosshair_manager):
        super().__init__(parent)
        self.crosshair = crosshair
        self.crosshair_manager = crosshair_manager
        self.update_screen_size()


    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_crosshair(painter)

    def draw_crosshair(self, painter):
        self.update_screen_size()

        color = QColor('#90EE90')
        width = self.crosshair.width
        line_size = self.crosshair.length
        gap = self.crosshair.gap

        x_center = self.screen_size[0] // 2
        y_center = self.screen_size[1] // 2

        pen = QPen(color, width)
        painter.setPen(pen)

        # Рисование линий
        painter.drawLine(x_center, y_center-gap, x_center, y_center-gap-line_size)
        painter.drawLine(x_center, y_center+gap, x_center, y_center+gap+line_size)
        painter.drawLine(x_center-gap, y_center, x_center-gap-line_size, y_center)
        painter.drawLine(x_center+gap, y_center, x_center+gap+line_size, y_center)

        dot = self.crosshair.get_dot()
        print(dot)
        if dot.is_it_dot():
            r = dot.dot_size
            brush = QBrush(color)
            painter.setBrush(brush)
            painter.drawEllipse(x_center-r, y_center-r, 2*r, 2*r)

        self.crosshair.save_to_json(self.crosshair_manager.get_data_manager().get_last_crosshair_path())

    def update_crosshair(self, attribute, value):
        self.update_screen_size()
        if "dot" in attribute:
            dot = self.crosshair.get_dot()
            setattr(dot, attribute, value)
            self.crosshair.set_dot(dot)
        else:
            setattr(self.crosshair, attribute, value)
        
        self.update()

    def update_screen_size(self):
        self.screen_size = self.crosshair_manager.get_screen_size()
        self.resize(self.screen_size[0], self.screen_size[1])