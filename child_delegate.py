from PySide import QtGui, QtCore
from child_list_item import ChildWidget


class ChildItemDelegate(QtGui.QStyledItemDelegate):

    PUBFILE_MAP = {'tick': {'code': 'Huey',
                            'color': 'green'},
                   'trick': {'code': 'Dewey',
                             'color': 'blue'},
                   'track': {'code': 'Louie',
                             'color': 'red'},
                   }

    def __init__(self, view):
        """
        Constructor
        """
        QtGui.QStyledItemDelegate.__init__(self, view)
        self.__view = view

        # set up the widget instance we will use
        # when 'painting' large number of cells
        self.__paint_widget = self._create_widget(view)

        # tracks the currently active cell
        self.__current_editor_indexes = []

        # help the GC
        self.__editors = []

        self.__selection_model = self.__view.selectionModel()
        if self.__selection_model:
            # note! Need to have a model connected to the view in order
            # to have a selection model.
            self.__selection_model.selectionChanged.connect(self._on_selection_changed)

    def _create_widget(self, parent):
        """
        Returns the widget to be used when creating items
        """

        widget = ChildWidget(parent)
        widget.setVisible(False)

        return widget

    def updateEditorGeometry(self, editor_widget, style_options, model_index):
        """
        Subclassed implementation which is typically called
        whenever a editor widget is set up and needs resizing.
        This happens immediately after creation and also for example
        if the grid element size is changing.
        """
        editor_widget.resize(style_options.rect.size())
        editor_widget.move(style_options.rect.topLeft())

    def paint(self, painter, style_options, model_index):
        """
        Paint method to handle all cells that are not being currently edited.
        """
        if model_index not in self.__current_editor_indexes:

            # paint_widget = self._create_widget(self.__view)
            # for performance reasons, we are not creating a widget every time
            # but merely moving the same widget around.
            # first call out to have the widget set the right values
            # if self.__view.selected.contains(model_index):
            #     self._on_before_selection(self.__paint_widget, model_index,
            #                               style_options)
            # else:
            self._on_before_paint(self.__paint_widget, model_index,
                                  style_options)

            # now paint!
            painter.save()
            self.__paint_widget.resize(style_options.rect.size())
            painter.translate(style_options.rect.topLeft())
            # note that we set the render flags NOT to render the background of
            # the widget this makes it consistent with the way the editor widget
            # is mounted inside each element upon hover.

            pixmap = QtGui.QPixmap(style_options.rect.size())
            pixmap.fill(QtCore.Qt.transparent)
            self.__paint_widget.resize(style_options.rect.size())
            self.__paint_widget.render(pixmap,
                                       QtCore.QPoint(0, 0),
                                       renderFlags=QtGui.QWidget.DrawChildren)
            painter.drawPixmap(style_options.rect, pixmap, pixmap.rect())
            painter.restore()

    def _on_before_paint(self, widget, model_index, style_options):
        """
        Called when a cell is being painted.
        """

        item_name = model_index.data(QtCore.Qt.DisplayRole)

        if item_name:
            item_opts = self.PUBFILE_MAP.get(item_name)
            if item_opts:
                widget.set_label(item_opts['code'])
                widget.set_background(item_opts['color'])
            else:
                widget.set_label(item_name)
                widget.set_background('#999999')

        else:
            widget.set_label('N/A')

    def _on_before_selection(self, widget, model_index, style_options):
        """
        Called when a cell is being selected.
        """
        # do std drawing first
        self._on_before_paint(widget, model_index, style_options)
        widget.set_selected(True)

    def sizeHint(self, style_options, model_index):
        """
        Base the size on the icon size property of the view
        """
        return ChildWidget.calculate_size()