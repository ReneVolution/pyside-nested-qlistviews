import sys
from PySide import QtGui

from models import ParentListModel
from parent_delegate import ParentItemDelegate


class NestedList(QtGui.QListView):

    def __init__(self):
        super(NestedList, self).__init__()
        self._model = ParentListModel(self)
        self._delegate = ParentItemDelegate(self)

        self.setModel(self._model)
        self.setItemDelegate(self._delegate)
        self.image = QtGui.QIcon('Louie_Dewey_and_Huey.png').pixmap(512)

        items = []
        for _ in range(100):
            items.append({'name': 'test',
                          'childs': ['tick', 'trick', 'track'],
                          'img': self.image})

        self._model.add_items(items)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    widget = NestedList()
    widget.resize(600, 600)
    widget.setWindowTitle('QListview Demo')

    widget.show()

    sys.exit(app.exec_())
