from PySide import QtCore, QtGui
from ui.child_widget import Ui_ChildWidget


class ChildWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(ChildWidget, self).__init__(parent)
        self.ui = Ui_ChildWidget()
        self.ui.setupUi(self)
        self.setContentsMargins(4, 4, 4, 4)
        self.set_background('#333333')

        font = self.ui.label.font()
        font.setPointSize(10)
        self.ui.label.setFont(font)

    def mouseReleaseEvent(self, event):
        event.ignore()

    def set_label(self, text):
        self.ui.label.setText(text)

    def set_background(self, hex_color):
        self.ui.box.setStyleSheet("""#box {background-color: %s;}
                                     #label {color: #FFFFFF;}""" % hex_color)

    def set_selected(self, selected):
        pass

    def sizeHint(self):
        return QtCore.QSize(70, 40)

    @staticmethod
    def calculate_size():
        """
        Calculates and returns a suitable size for this widget.
        """
        return QtCore.QSize(70, 40)
