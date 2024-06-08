from PyQt6.QtCore import QRect, Qt, QDateTime, QTimer
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QLabel, QPushButton

from TemplateRoom import TemplateRoom

class qrCodeRaum(TemplateRoom):
    def __init__(self, parent=None):
        super(qrCodeRaum, self).__init__(parent)

        self.init_room("QR-Code-Raum.png")

        self.offset_balloon_x = 0
        self.offset_balloon_y = 0
        self.set_offset_mouth(self.offset_balloon_x + self.offset_balloon_length, self.offset_balloon_y +
                              self.offset_balloon_width, 0, 0)

        self.hitbox_zurAula = QRect(1, 1, 250, 800)
        self.append_hitbox(self.hitbox_zurAula)