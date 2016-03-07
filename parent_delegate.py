from PySide import QtGui, QtCore
from parent_list_item import ParentWidget


class ParentItemDelegate(QtGui.QStyledItemDelegate):

    def __init__(self, view):
        """
        Constructor
        """
        super(ParentItemDelegate, self).__init__(view)
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

        widget = ParentWidget(parent)
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

            self.__paint_widget.render(painter,
                                       QtCore.QPoint(0, 0),
                                       renderFlags=QtGui.QWidget.DrawChildren)

            painter.restore()

    def _on_before_paint(self, widget, model_index, style_options):
        """
        Called when a cell is being painted.
        """

        item_name = model_index.data(QtCore.Qt.DisplayRole)
        childs = model_index.data(QtCore.Qt.UserRole)
        thumb = model_index.data(QtCore.Qt.DecorationRole)

        widget.set_text(item_name)
        widget.set_childs(childs)
        widget.set_thumbnail(thumb)

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
        return ParentWidget.calculate_size()


