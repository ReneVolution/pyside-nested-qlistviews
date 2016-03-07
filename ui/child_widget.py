from PySide import QtCore, QtGui


class Ui_ChildWidget(object):
    def setupUi(self, ChildWidget):
        ChildWidget.setObjectName("ChildWidget")
        ChildWidget.resize(107, 30)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChildWidget.sizePolicy().hasHeightForWidth())
        ChildWidget.setSizePolicy(sizePolicy)
        ChildWidget.setMinimumSize(QtCore.QSize(50, 0))
        ChildWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.horizontalLayout = QtGui.QHBoxLayout(ChildWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.box = QtGui.QFrame(ChildWidget)
        self.box.setFrameShape(QtGui.QFrame.StyledPanel)
        self.box.setFrameShadow(QtGui.QFrame.Raised)
        self.box.setObjectName("box")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.box)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QPushButton(self.box)
        self.label.setFlat(True)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setMargin(3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.box)

        self.retranslateUi(ChildWidget)
        QtCore.QMetaObject.connectSlotsByName(ChildWidget)

    def retranslateUi(self, PublishedFileItem):
        PublishedFileItem.setWindowTitle(QtGui.QApplication.translate("ChildItem", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ChildItem", "FileType", None, QtGui.QApplication.UnicodeUTF8))

