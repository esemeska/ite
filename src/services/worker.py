from PySide6.QtCore import QObject, Signal

class Worker(QObject):
    finished = Signal()
    progress = Signal(int)

    def run(self):
        for i in range(100):
            self.progress.emit(i)
        self.finished.emit()