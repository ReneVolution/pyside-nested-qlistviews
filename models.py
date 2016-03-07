from PySide import QtCore, QtGui


class ParentListModel(QtCore.QAbstractItemModel):

    def __init__(self, parent=None):
        super(ParentListModel, self).__init__(parent)
        self.items = []

    def rowCount(self, parent=None):
        return len(self.items)

    def columnCount(self, parent=None):
        return 1

    def index(self, row, column, parent=None):
        return self.createIndex(row, column)

    def parent(self, model_index):
        return QtCore.QModelIndex()

    def data(self, model_index, role):

        row = model_index.row()
        item = self.items[row]

        if role == QtCore.Qt.DisplayRole:
            return item.get('name')
        elif role == QtCore.Qt.UserRole:
            return item.get('childs')
        elif role == QtCore.Qt.DecorationRole:
            return item.get('img')

    def add_items(self, items):
        self.beginInsertRows(QtCore.QModelIndex(), len(self.items),
                             len(self.items) + len(items) - 1)
        self.items = items
        self.endInsertRows()


class ChildListModel(QtGui.QStringListModel):

    def __init__(self, parent=None):
        super(ChildListModel, self).__init__(parent)
