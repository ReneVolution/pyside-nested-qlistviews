from PySide import QtCore, QtGui

from child_delegate import ChildItemDelegate
from models import ChildListModel
from ui.parent_widget import Ui_ParentWidget


class ParentWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(ParentWidget, self).__init__(parent)
        self.ui = Ui_ParentWidget()
        self.ui.setupUi(self)
        self.ui.thumbnail.setScaledContents(False)

        self._model = ChildListModel(self.ui.child_list)
        self._delegate = ChildItemDelegate(self.ui.child_list)
        self.ui.child_list.setModel(self._model)
        self.ui.child_list.setItemDelegate(self._delegate)

    def mouseReleaseEvent(self, event):
        self.set_selected(True)

        super(ParentWidget, self).mouseReleaseEvent(event)

    def set_thumbnail(self, pixmap):
        rescaled = self.rescale_image(pixmap)
        self.ui.thumbnail.setPixmap(rescaled)

    def rescale_image(self, pixmap):
        width = 84
        height = 40
        scaled = pixmap.scaledToHeight(height,
                                       mode=QtCore.Qt.SmoothTransformation)

        if scaled.width() < width:
            scaled = pixmap.scaledToWidth(width,
                                          mode=QtCore.Qt.SmoothTransformation)
            x_offset = 0
            y_offset = (scaled.height() - height) / 2
        else:
            x_offset = (scaled.width() - width) / 2
            y_offset = 0

        cropped = scaled.copy(x_offset, y_offset, width, height)

        return cropped

    def set_text(self, text):
        self.ui.itemName.setText(text)

    def set_childs(self, files):
        self._model.setStringList(files)

    @staticmethod
    def calculate_size():
        """
        Calculates and returns a suitable size for this widget.
        """
        return QtCore.QSize(200, 60)
