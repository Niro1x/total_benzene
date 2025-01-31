from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *

import resources


class Body(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1400, 900))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/images/icons/newl.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet(
            "\n"
            "\n"
            "QMainWindow {\n"
            "    background-color: #f2f2f2;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 15px;\n"
            "}\n"
            "QStatusBar {\n"
            '    font: 15pt "Arabic Transparent Bold";\n'
            "    color:#ffffff;\n"
            "}"
        )
        MainWindow.setLocale(
            QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt)
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "QStatusBar {\n" "    color:rgb(156, 14, 14);\n" "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_58 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.notf = QtWidgets.QFrame(self.centralwidget)
        self.notf.setMinimumSize(QtCore.QSize(0, 65))
        self.notf.setMaximumSize(QtCore.QSize(16777215, 65))
        self.notf.setStyleSheet("")
        self.notf.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notf.setObjectName("notf")
        self.gridLayout_155 = QtWidgets.QGridLayout(self.notf)
        self.gridLayout_155.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_155.setSpacing(0)
        self.gridLayout_155.setObjectName("gridLayout_155")
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_155.addItem(spacerItem, 0, 0, 1, 1)
        self.msg = QtWidgets.QLabel(self.notf)
        self.msg.setAutoFillBackground(False)
        self.msg.setStyleSheet(
            "QLabel{\n"
            'font: 15pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "}"
        )
        self.msg.setTextFormat(QtCore.Qt.AutoText)
        self.msg.setScaledContents(True)
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setWordWrap(False)
        self.msg.setOpenExternalLinks(False)
        self.msg.setObjectName("msg")
        self.gridLayout_155.addWidget(self.msg, 0, 1, 1, 1)
        self.gridLayout_58.addWidget(self.notf, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(242, 242, 242);\n" "\n" "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 75))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_9.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "\n"
            ""
        )
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_14.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_14.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_14.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_14.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_14.setTabletTracking(False)
        self.pushButton_14.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_14.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_14.setToolTipDuration(-1)
        self.pushButton_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet(
            "QPushButton {\n"
            "        text-align: right;\n"
            '        font: 20pt "Arabic Transparent Bold";\n'
            "        color: #1B1C1E;\n"
            "        border: 0px solid gray;\n"
            "        border-radius: 0px;\n"
            "        padding: 0 8px;\n"
            "        outline: none;\n"
            "    }\n"
            ""
        )
        self.pushButton_14.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_14.setAutoRepeat(False)
        self.pushButton_14.setAutoExclusive(False)
        self.pushButton_14.setAutoRepeatDelay(300)
        self.pushButton_14.setAutoRepeatInterval(100)
        self.pushButton_14.setAutoDefault(True)
        self.pushButton_14.setDefault(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_11.addWidget(self.pushButton_14, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            453, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_11.addItem(spacerItem1, 0, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_9)
        self.dateEdit.setMinimumSize(QtCore.QSize(200, 50))
        self.dateEdit.setMaximumSize(QtCore.QSize(250, 50))
        self.dateEdit.setStyleSheet(
            "QDateEdit {\n"
            '        font: 12pt "Arabic Transparent Bold";\n'
            "        color: #1e1d23;\n"
            "        border: 2px solid #1e1d23;\n"
            "        border-radius: 5px;\n"
            "        padding: 0 8px;\n"
            "        background-color: rgb(245, 245, 245);\n"
            "        border: 2px solid rgb(245, 245, 245);\n"
            "        padding: 5px;\n"
            "    }\n"
            "\n"
            "QDateEdit::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 3px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/cil-arrow-bottom.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "\n"
            "QFrame{\n"
            "    border-radius: 5px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "}\n"
            "\n"
            "QToolButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 0px;\n"
            "    border-radius: 0px;\n"
            "    outline: none;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "}\n"
            "QToolButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 0px;\n"
            "}"
        )
        self.dateEdit.setWrapping(False)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_11.addWidget(self.dateEdit, 0, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_13.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_13.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_13.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 5px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 5px;\n"
            "}"
        )
        self.pushButton_13.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-action-redo.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_11.addWidget(self.pushButton_13, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame_9, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget.setStyleSheet(
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;\n"
            "background-color: rgb(242, 242, 242);"
        )
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_3.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f2f2f2;\n"
            "\n"
            "}"
        )
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_81 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_81.setContentsMargins(0, 20, 0, 20)
        self.gridLayout_81.setSpacing(10)
        self.gridLayout_81.setObjectName("gridLayout_81")
        self.frame_33 = QtWidgets.QFrame(self.frame_3)
        self.frame_33.setMinimumSize(QtCore.QSize(360, 400))
        self.frame_33.setMaximumSize(QtCore.QSize(360, 600))
        self.frame_33.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "QLabel{\n"
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "}"
        )
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.gridLayout_85 = QtWidgets.QGridLayout(self.frame_33)
        self.gridLayout_85.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_85.setSpacing(10)
        self.gridLayout_85.setObjectName("gridLayout_85")
        self.frame_49 = QtWidgets.QFrame(self.frame_33)
        self.frame_49.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.gridLayout_82 = QtWidgets.QGridLayout(self.frame_49)
        self.gridLayout_82.setObjectName("gridLayout_82")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_49)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(90, 70))
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(90, 70))
        self.doubleSpinBox.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: #d9d9d9;\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid #d9d9d9;\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setMaximum(1000.0)
        self.doubleSpinBox.setSingleStep(0.25)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_82.addWidget(self.doubleSpinBox, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_49)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_82.addWidget(self.label_7, 1, 0, 1, 1)
        self.gridLayout_85.addWidget(self.frame_49, 1, 1, 1, 1)
        self.pushButton_53 = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_53.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_53.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_53.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_53.setObjectName("pushButton_53")
        self.gridLayout_85.addWidget(self.pushButton_53, 3, 0, 1, 2)
        self.frame_48 = QtWidgets.QFrame(self.frame_33)
        self.frame_48.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.gridLayout_80 = QtWidgets.QGridLayout(self.frame_48)
        self.gridLayout_80.setObjectName("gridLayout_80")
        self.label_6 = QtWidgets.QLabel(self.frame_48)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_80.addWidget(self.label_6, 0, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.frame_48)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(90, 70))
        self.doubleSpinBox_2.setMaximumSize(QtCore.QSize(90, 70))
        self.doubleSpinBox_2.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: #d9d9d9;\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid #d9d9d9;\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setMaximum(1000.0)
        self.doubleSpinBox_2.setSingleStep(0.25)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_80.addWidget(self.doubleSpinBox_2, 1, 0, 1, 1)
        self.gridLayout_85.addWidget(self.frame_48, 1, 0, 1, 1)
        self.frame_51 = QtWidgets.QFrame(self.frame_33)
        self.frame_51.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.gridLayout_84 = QtWidgets.QGridLayout(self.frame_51)
        self.gridLayout_84.setObjectName("gridLayout_84")
        self.label_9 = QtWidgets.QLabel(self.frame_51)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_84.addWidget(self.label_9, 0, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.frame_51)
        self.doubleSpinBox_3.setMinimumSize(QtCore.QSize(90, 70))
        self.doubleSpinBox_3.setMaximumSize(QtCore.QSize(90, 70))
        self.doubleSpinBox_3.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: #d9d9d9;\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid #d9d9d9;\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_3.setMaximum(1000.0)
        self.doubleSpinBox_3.setSingleStep(0.25)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_84.addWidget(self.doubleSpinBox_3, 1, 0, 1, 1)
        self.gridLayout_85.addWidget(self.frame_51, 2, 1, 1, 1)
        self.frame_50 = QtWidgets.QFrame(self.frame_33)
        self.frame_50.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.gridLayout_83 = QtWidgets.QGridLayout(self.frame_50)
        self.gridLayout_83.setObjectName("gridLayout_83")
        self.label_8 = QtWidgets.QLabel(self.frame_50)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_83.addWidget(self.label_8, 0, 0, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.frame_50)
        self.doubleSpinBox_4.setMinimumSize(QtCore.QSize(90, 70))
        self.doubleSpinBox_4.setMaximumSize(QtCore.QSize(90, 70))
        self.doubleSpinBox_4.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: #d9d9d9;\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid #d9d9d9;\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_4.setMaximum(1000.0)
        self.doubleSpinBox_4.setSingleStep(0.25)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_83.addWidget(self.doubleSpinBox_4, 1, 0, 1, 1)
        self.gridLayout_85.addWidget(self.frame_50, 2, 0, 1, 1)
        self.gridLayout_81.addWidget(self.frame_33, 0, 0, 2, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMinimumSize(QtCore.QSize(500, 400))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 600))
        self.frame_5.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #d9d9d9;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #d9d9d9;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #d9d9d9;\n"
            "    border-top: 1px solid #d9d9d9;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_78 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_78.setObjectName("gridLayout_78")
        self.tableWidget_20 = QtWidgets.QTableWidget(self.frame_5)
        self.tableWidget_20.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_20.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_20.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_20.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_20.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_20.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_20.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_20.setShowGrid(False)
        self.tableWidget_20.setObjectName("tableWidget_20")
        self.tableWidget_20.setColumnCount(4)
        self.tableWidget_20.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(3, item)
        self.tableWidget_20.horizontalHeader().setVisible(True)
        self.tableWidget_20.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_20.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget_20.horizontalHeader().setHighlightSections(True)
        self.tableWidget_20.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_20.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_20.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_20.verticalHeader().setVisible(False)
        self.tableWidget_20.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_20.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_20.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_78.addWidget(self.tableWidget_20, 0, 0, 1, 1)
        self.frame_20 = QtWidgets.QFrame(self.frame_5)
        self.frame_20.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_114 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_114.setObjectName("gridLayout_114")
        self.pushButton_64 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_64.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_64.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_64.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_64.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-print.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_64.setIcon(icon2)
        self.pushButton_64.setObjectName("pushButton_64")
        self.gridLayout_114.addWidget(self.pushButton_64, 0, 0, 1, 1)
        self.gridLayout_78.addWidget(self.frame_20, 1, 0, 1, 1)
        self.gridLayout_81.addWidget(self.frame_5, 0, 1, 2, 1)
        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_4.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #ffffff;\n"
            "\n"
            ""
        )
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_77 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_77.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_77.setSpacing(10)
        self.gridLayout_77.setObjectName("gridLayout_77")
        self.frame_44 = QtWidgets.QFrame(self.frame_4)
        self.frame_44.setMinimumSize(QtCore.QSize(260, 130))
        self.frame_44.setMaximumSize(QtCore.QSize(400, 250))
        self.frame_44.setStyleSheet(
            "QFrame{\n"
            "background-color:  rgb(27, 28, 30);\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "padding:15px;\n"
            "\n"
            "}\n"
            "QLabel{\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "}"
        )
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.gridLayout_73 = QtWidgets.QGridLayout(self.frame_44)
        self.gridLayout_73.setObjectName("gridLayout_73")
        self.pushButton_47 = QtWidgets.QPushButton(self.frame_44)
        self.pushButton_47.setEnabled(False)
        self.pushButton_47.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_47.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_47.setStyleSheet(
            "background-color: rgb(74, 74, 74);\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;"
        )
        self.pushButton_47.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-clipboard.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_47.setIcon(icon3)
        self.pushButton_47.setObjectName("pushButton_47")
        self.gridLayout_73.addWidget(self.pushButton_47, 0, 1, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.frame_44)
        self.label_69.setStyleSheet("")
        self.label_69.setScaledContents(True)
        self.label_69.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_69.setObjectName("label_69")
        self.gridLayout_73.addWidget(self.label_69, 2, 0, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.frame_44)
        self.label_68.setAutoFillBackground(False)
        self.label_68.setStyleSheet("")
        self.label_68.setTextFormat(QtCore.Qt.AutoText)
        self.label_68.setScaledContents(True)
        self.label_68.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_68.setWordWrap(False)
        self.label_68.setOpenExternalLinks(False)
        self.label_68.setObjectName("label_68")
        self.gridLayout_73.addWidget(self.label_68, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_44)
        self.line.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_73.addWidget(self.line, 3, 0, 1, 1)
        self.gridLayout_77.addWidget(self.frame_44, 0, 0, 1, 1)
        self.frame_45 = QtWidgets.QFrame(self.frame_4)
        self.frame_45.setMinimumSize(QtCore.QSize(260, 130))
        self.frame_45.setMaximumSize(QtCore.QSize(400, 250))
        self.frame_45.setStyleSheet(
            "QFrame{\n"
            "background-color:  rgb(27, 28, 30);\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "padding:15px;\n"
            "\n"
            "}\n"
            "QLabel{\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "}"
        )
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.gridLayout_74 = QtWidgets.QGridLayout(self.frame_45)
        self.gridLayout_74.setObjectName("gridLayout_74")
        self.line_2 = QtWidgets.QFrame(self.frame_45)
        self.line_2.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_74.addWidget(self.line_2, 3, 0, 1, 1)
        self.pushButton_48 = QtWidgets.QPushButton(self.frame_45)
        self.pushButton_48.setEnabled(False)
        self.pushButton_48.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_48.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_48.setStyleSheet(
            "background-color: rgb(74, 74, 74);\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;"
        )
        self.pushButton_48.setText("")
        self.pushButton_48.setIcon(icon3)
        self.pushButton_48.setObjectName("pushButton_48")
        self.gridLayout_74.addWidget(self.pushButton_48, 0, 1, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.frame_45)
        self.label_71.setAutoFillBackground(False)
        self.label_71.setStyleSheet("")
        self.label_71.setTextFormat(QtCore.Qt.AutoText)
        self.label_71.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_71.setWordWrap(False)
        self.label_71.setOpenExternalLinks(False)
        self.label_71.setObjectName("label_71")
        self.gridLayout_74.addWidget(self.label_71, 0, 0, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.frame_45)
        self.label_70.setStyleSheet("")
        self.label_70.setScaledContents(True)
        self.label_70.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_70.setObjectName("label_70")
        self.gridLayout_74.addWidget(self.label_70, 2, 0, 1, 1)
        self.gridLayout_77.addWidget(self.frame_45, 0, 1, 1, 1)
        self.frame_46 = QtWidgets.QFrame(self.frame_4)
        self.frame_46.setMinimumSize(QtCore.QSize(260, 130))
        self.frame_46.setMaximumSize(QtCore.QSize(400, 250))
        self.frame_46.setStyleSheet(
            "QFrame{\n"
            "background-color:  rgb(27, 28, 30);\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "padding:15px;\n"
            "\n"
            "}\n"
            "QLabel{\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "}"
        )
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.gridLayout_75 = QtWidgets.QGridLayout(self.frame_46)
        self.gridLayout_75.setObjectName("gridLayout_75")
        self.label_73 = QtWidgets.QLabel(self.frame_46)
        self.label_73.setAutoFillBackground(False)
        self.label_73.setStyleSheet("")
        self.label_73.setTextFormat(QtCore.Qt.AutoText)
        self.label_73.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_73.setWordWrap(False)
        self.label_73.setOpenExternalLinks(False)
        self.label_73.setObjectName("label_73")
        self.gridLayout_75.addWidget(self.label_73, 0, 0, 1, 1)
        self.pushButton_49 = QtWidgets.QPushButton(self.frame_46)
        self.pushButton_49.setEnabled(False)
        self.pushButton_49.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_49.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_49.setStyleSheet(
            "background-color: rgb(74, 74, 74);\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;"
        )
        self.pushButton_49.setText("")
        self.pushButton_49.setIcon(icon3)
        self.pushButton_49.setObjectName("pushButton_49")
        self.gridLayout_75.addWidget(self.pushButton_49, 0, 1, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.frame_46)
        self.label_72.setStyleSheet("")
        self.label_72.setScaledContents(True)
        self.label_72.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_72.setObjectName("label_72")
        self.gridLayout_75.addWidget(self.label_72, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame_46)
        self.line_3.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_75.addWidget(self.line_3, 3, 0, 1, 1)
        self.gridLayout_77.addWidget(self.frame_46, 0, 2, 1, 1)
        self.frame_47 = QtWidgets.QFrame(self.frame_4)
        self.frame_47.setMinimumSize(QtCore.QSize(260, 130))
        self.frame_47.setMaximumSize(QtCore.QSize(400, 250))
        self.frame_47.setStyleSheet(
            "QFrame{\n"
            "background-color:  rgb(27, 28, 30);\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "padding:15px;\n"
            "\n"
            "}\n"
            "QLabel{\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "}"
        )
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.gridLayout_76 = QtWidgets.QGridLayout(self.frame_47)
        self.gridLayout_76.setObjectName("gridLayout_76")
        self.pushButton_50 = QtWidgets.QPushButton(self.frame_47)
        self.pushButton_50.setEnabled(False)
        self.pushButton_50.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_50.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_50.setStyleSheet(
            "background-color: rgb(74, 74, 74);\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;"
        )
        self.pushButton_50.setText("")
        self.pushButton_50.setIcon(icon3)
        self.pushButton_50.setObjectName("pushButton_50")
        self.gridLayout_76.addWidget(self.pushButton_50, 0, 1, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.frame_47)
        self.label_74.setStyleSheet("")
        self.label_74.setScaledContents(True)
        self.label_74.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_74.setObjectName("label_74")
        self.gridLayout_76.addWidget(self.label_74, 2, 0, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.frame_47)
        self.label_75.setAutoFillBackground(False)
        self.label_75.setStyleSheet("")
        self.label_75.setTextFormat(QtCore.Qt.AutoText)
        self.label_75.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label_75.setWordWrap(False)
        self.label_75.setOpenExternalLinks(False)
        self.label_75.setObjectName("label_75")
        self.gridLayout_76.addWidget(self.label_75, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.frame_47)
        self.line_4.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_76.addWidget(self.line_4, 3, 0, 1, 1)
        self.gridLayout_77.addWidget(self.frame_47, 0, 3, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.tab_2)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_8.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 5px;\n"
            "      border: none;\n"
            "      border-bottom: 1px solid #ccc;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_8)
        self.scrollArea_2.setStyleSheet(
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1117, 703))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_46 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1117, 703))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_8.addItem(spacerItem2, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_8.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.frame_59 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_59.setMinimumSize(QtCore.QSize(260, 60))
        self.frame_59.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_59.setStyleSheet(
            "QFrame{\n"
            'font: 9pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "background-color: #003a5d;\n"
            "border-width: 0x;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "}"
        )
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.gridLayout_72 = QtWidgets.QGridLayout(self.frame_59)
        self.gridLayout_72.setObjectName("gridLayout_72")
        self.label_176 = QtWidgets.QLabel(self.frame_59)
        self.label_176.setMinimumSize(QtCore.QSize(38, 0))
        self.label_176.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_176.setAlignment(QtCore.Qt.AlignCenter)
        self.label_176.setObjectName("label_176")
        self.gridLayout_72.addWidget(self.label_176, 0, 3, 3, 1)
        self.label_177 = QtWidgets.QLabel(self.frame_59)
        self.label_177.setMinimumSize(QtCore.QSize(125, 0))
        self.label_177.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_177.setAlignment(QtCore.Qt.AlignCenter)
        self.label_177.setObjectName("label_177")
        self.gridLayout_72.addWidget(self.label_177, 0, 1, 3, 1)
        self.label_181 = QtWidgets.QLabel(self.frame_59)
        self.label_181.setMinimumSize(QtCore.QSize(62, 0))
        self.label_181.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_181.setAlignment(QtCore.Qt.AlignCenter)
        self.label_181.setObjectName("label_181")
        self.gridLayout_72.addWidget(self.label_181, 0, 4, 3, 1)
        self.label_178 = QtWidgets.QLabel(self.frame_59)
        self.label_178.setMinimumSize(QtCore.QSize(45, 0))
        self.label_178.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_178.setAlignment(QtCore.Qt.AlignCenter)
        self.label_178.setObjectName("label_178")
        self.gridLayout_72.addWidget(self.label_178, 0, 2, 3, 1)
        self.label_39 = QtWidgets.QLabel(self.frame_59)
        self.label_39.setMinimumSize(QtCore.QSize(65, 0))
        self.label_39.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_72.addWidget(self.label_39, 0, 5, 3, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_72.addItem(spacerItem3, 1, 6, 1, 1)
        self.gridLayout_8.addWidget(self.frame_59, 0, 0, 1, 1)
        self.pushButton_67 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_67.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_67.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_67.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_67.setText("")
        self.pushButton_67.setIcon(icon2)
        self.pushButton_67.setObjectName("pushButton_67")
        self.gridLayout_8.addWidget(self.pushButton_67, 0, 1, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_46.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_4.setEnabled(True)
        self.tabWidget_4.setAutoFillBackground(False)
        self.tabWidget_4.setStyleSheet(
            "\n"
            "/*-----QTabWidget-----*/\n"
            "QTabBar::tab\n"
            "{\n"
            '    font: 11pt "Arabic Transparent Bold";\n'
            "    background-color: #262626;\n"
            "    color: rgb(27, 28, 30);\n"
            "    border-style: solid;\n"
            "    border-width: 0px;\n"
            "    border-top-left-radius: 3px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-color: #051a39;\n"
            "    width: 100px;\n"
            "    height: 30px;\n"
            "}\n"
            "QTabBar::tab:selected\n"
            "{\n"
            "    background-color: #003a5d;\n"
            "    color: #ffffff;\n"
            "    border-style: solid;\n"
            "    border-width: 0px;\n"
            "    border-top-left-radius: 3px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-color: #051a39;\n"
            "    width: 100px;\n"
            "    height: 30px;\n"
            "}\n"
            "QTabBar::tab:!selected \n"
            "{\n"
            "    background-color: #DFECFF;\n"
            "}\n"
            ""
        )
        self.tabWidget_4.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_4.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_4.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_4.setDocumentMode(False)
        self.tabWidget_4.setTabsClosable(False)
        self.tabWidget_4.setMovable(False)
        self.tabWidget_4.setTabBarAutoHide(False)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.gridLayout_49 = QtWidgets.QGridLayout(self.tab_18)
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_49.setSpacing(0)
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.frame_12 = QtWidgets.QFrame(self.tab_18)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_12.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "    border-top: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(85, 170, 255);\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_147 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_147.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_147.setVerticalSpacing(15)
        self.gridLayout_147.setObjectName("gridLayout_147")
        self.frame_11 = QtWidgets.QFrame(self.frame_12)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_11.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_12.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_12.setSpacing(5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.spinBox_17 = QtWidgets.QSpinBox(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox_17.sizePolicy().hasHeightForWidth())
        self.spinBox_17.setSizePolicy(sizePolicy)
        self.spinBox_17.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_17.setMaximumSize(QtCore.QSize(250, 50))
        self.spinBox_17.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_17.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_17.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_17.setMaximum(999999999)
        self.spinBox_17.setObjectName("spinBox_17")
        self.gridLayout_12.addWidget(self.spinBox_17, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_11)
        self.label_13.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_12.addWidget(self.label_13, 0, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_16.setMaximumSize(QtCore.QSize(120, 50))
        self.pushButton_16.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_12.addWidget(self.pushButton_16, 1, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_11)
        self.label_14.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_12.addWidget(self.label_14, 0, 1, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.frame_11)
        self.comboBox_10.setMinimumSize(QtCore.QSize(200, 50))
        self.comboBox_10.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBox_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_10.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }"
        )
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.gridLayout_12.addWidget(self.comboBox_10, 1, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.frame_11)
        self.label_35.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_12.addWidget(self.label_35, 0, 0, 1, 1)
        self.spinBox_18 = QtWidgets.QSpinBox(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox_18.sizePolicy().hasHeightForWidth())
        self.spinBox_18.setSizePolicy(sizePolicy)
        self.spinBox_18.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_18.setMaximumSize(QtCore.QSize(250, 50))
        self.spinBox_18.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_18.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_18.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_18.setMaximum(999999999)
        self.spinBox_18.setObjectName("spinBox_18")
        self.gridLayout_12.addWidget(self.spinBox_18, 1, 2, 1, 1)
        self.spinBox_19 = QtWidgets.QSpinBox(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox_19.sizePolicy().hasHeightForWidth())
        self.spinBox_19.setSizePolicy(sizePolicy)
        self.spinBox_19.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_19.setMaximumSize(QtCore.QSize(250, 50))
        self.spinBox_19.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_19.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_19.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_19.setMaximum(999999999)
        self.spinBox_19.setObjectName("spinBox_19")
        self.gridLayout_12.addWidget(self.spinBox_19, 1, 3, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.frame_11)
        self.label_40.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_12.addWidget(self.label_40, 0, 3, 1, 1)
        self.pushButton_81 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_81.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_81.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_81.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_81.setText("")
        self.pushButton_81.setIcon(icon2)
        self.pushButton_81.setObjectName("pushButton_81")
        self.gridLayout_12.addWidget(self.pushButton_81, 1, 5, 1, 1)
        self.gridLayout_147.addWidget(self.frame_11, 0, 0, 1, 1)
        self.frame_106 = QtWidgets.QFrame(self.frame_12)
        self.frame_106.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_106.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_106.setObjectName("frame_106")
        self.gridLayout_145 = QtWidgets.QGridLayout(self.frame_106)
        self.gridLayout_145.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_145.setVerticalSpacing(6)
        self.gridLayout_145.setObjectName("gridLayout_145")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_106)
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_19.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_19.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_145.addWidget(self.pushButton_19, 1, 0, 1, 1)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.frame_106)
        self.tableWidget_4.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_4.setShowGrid(False)
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_4.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(50)
        self.gridLayout_145.addWidget(self.tableWidget_4, 0, 0, 1, 1)
        self.gridLayout_147.addWidget(self.frame_106, 1, 0, 1, 1)
        self.gridLayout_49.addWidget(self.frame_12, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.tab_19)
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.frame_36 = QtWidgets.QFrame(self.tab_19)
        self.frame_36.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_36.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "    border-top: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(85, 170, 255);\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.gridLayout_150 = QtWidgets.QGridLayout(self.frame_36)
        self.gridLayout_150.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_150.setVerticalSpacing(15)
        self.gridLayout_150.setObjectName("gridLayout_150")
        self.frame_105 = QtWidgets.QFrame(self.frame_36)
        self.frame_105.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_105.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_105.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_105.setObjectName("frame_105")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_105)
        self.gridLayout_13.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_13.setSpacing(5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_36 = QtWidgets.QLabel(self.frame_105)
        self.label_36.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_13.addWidget(self.label_36, 0, 0, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_105)
        self.pushButton_23.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_23.setMaximumSize(QtCore.QSize(120, 50))
        self.pushButton_23.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_13.addWidget(self.pushButton_23, 1, 4, 1, 1)
        self.comboBox_14 = QtWidgets.QComboBox(self.frame_105)
        self.comboBox_14.setMinimumSize(QtCore.QSize(150, 50))
        self.comboBox_14.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBox_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_14.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}"
        )
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.gridLayout_13.addWidget(self.comboBox_14, 1, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame_105)
        self.label_30.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_13.addWidget(self.label_30, 0, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.frame_105)
        self.label_43.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_13.addWidget(self.label_43, 0, 3, 1, 1)
        self.spinBox_8 = QtWidgets.QSpinBox(self.frame_105)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox_8.sizePolicy().hasHeightForWidth())
        self.spinBox_8.setSizePolicy(sizePolicy)
        self.spinBox_8.setMinimumSize(QtCore.QSize(100, 50))
        self.spinBox_8.setMaximumSize(QtCore.QSize(250, 50))
        self.spinBox_8.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_8.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_8.setMaximum(999999999)
        self.spinBox_8.setObjectName("spinBox_8")
        self.gridLayout_13.addWidget(self.spinBox_8, 1, 2, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.frame_105)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox_6.sizePolicy().hasHeightForWidth())
        self.spinBox_6.setSizePolicy(sizePolicy)
        self.spinBox_6.setMinimumSize(QtCore.QSize(100, 50))
        self.spinBox_6.setMaximumSize(QtCore.QSize(250, 50))
        self.spinBox_6.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_6.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_6.setMaximum(999999999)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_13.addWidget(self.spinBox_6, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_105)
        self.label_16.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_13.addWidget(self.label_16, 0, 2, 1, 1)
        self.spinBox_16 = QtWidgets.QSpinBox(self.frame_105)
        self.spinBox_16.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox_16.sizePolicy().hasHeightForWidth())
        self.spinBox_16.setSizePolicy(sizePolicy)
        self.spinBox_16.setMinimumSize(QtCore.QSize(100, 50))
        self.spinBox_16.setMaximumSize(QtCore.QSize(250, 50))
        self.spinBox_16.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_16.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_16.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_16.setMaximum(999999999)
        self.spinBox_16.setObjectName("spinBox_16")
        self.gridLayout_13.addWidget(self.spinBox_16, 1, 3, 1, 1)
        self.pushButton_82 = QtWidgets.QPushButton(self.frame_105)
        self.pushButton_82.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_82.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_82.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_82.setText("")
        self.pushButton_82.setIcon(icon2)
        self.pushButton_82.setObjectName("pushButton_82")
        self.gridLayout_13.addWidget(self.pushButton_82, 1, 5, 1, 1)
        self.gridLayout_150.addWidget(self.frame_105, 0, 0, 1, 2)
        self.frame_108 = QtWidgets.QFrame(self.frame_36)
        self.frame_108.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_108.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_108.setObjectName("frame_108")
        self.gridLayout_148 = QtWidgets.QGridLayout(self.frame_108)
        self.gridLayout_148.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_148.setVerticalSpacing(6)
        self.gridLayout_148.setObjectName("gridLayout_148")
        self.tableWidget_9 = QtWidgets.QTableWidget(self.frame_108)
        self.tableWidget_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_9.setAutoFillBackground(False)
        self.tableWidget_9.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_9.setLineWidth(1)
        self.tableWidget_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_9.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_9.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_9.setAlternatingRowColors(True)
        self.tableWidget_9.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.tableWidget_9.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_9.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_9.setShowGrid(False)
        self.tableWidget_9.setWordWrap(True)
        self.tableWidget_9.setCornerButtonEnabled(True)
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(6)
        self.tableWidget_9.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(5, item)
        self.tableWidget_9.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_9.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_9.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_9.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_9.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_9.verticalHeader().setVisible(False)
        self.tableWidget_9.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_9.verticalHeader().setDefaultSectionSize(50)
        self.gridLayout_148.addWidget(self.tableWidget_9, 0, 0, 1, 1)
        self.pushButton_58 = QtWidgets.QPushButton(self.frame_108)
        self.pushButton_58.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_58.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_58.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_58.setObjectName("pushButton_58")
        self.gridLayout_148.addWidget(self.pushButton_58, 1, 0, 1, 1)
        self.gridLayout_150.addWidget(self.frame_108, 1, 0, 2, 2)
        self.gridLayout_51.addWidget(self.frame_36, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_19, "")
        self.gridLayout_7.addWidget(self.tabWidget_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.frame_15 = QtWidgets.QFrame(self.tab_4)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_15.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border: 1px solid #1e1d23;\n"
            "border-radius: 2px;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(85, 170, 255);\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_115 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_115.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_115.setSpacing(15)
        self.gridLayout_115.setObjectName("gridLayout_115")
        self.frame_14 = QtWidgets.QFrame(self.frame_15)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_14.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_15.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_18.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_18.setMaximumSize(QtCore.QSize(120, 50))
        self.pushButton_18.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_15.addWidget(self.pushButton_18, 1, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox.setMaximumSize(QtCore.QSize(250, 50))
        self.spinBox.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_15.addWidget(self.spinBox, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_14)
        self.label_17.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_15.addWidget(self.label_17, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_14)
        self.label_15.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_15.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_25.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit_25.setMaximumSize(QtCore.QSize(600, 16777215))
        self.lineEdit_25.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_25.setMaxLength(9999999)
        self.lineEdit_25.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_15.addWidget(self.lineEdit_25, 1, 0, 1, 1)
        self.pushButton_68 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_68.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_68.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_68.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_68.setText("")
        self.pushButton_68.setIcon(icon2)
        self.pushButton_68.setObjectName("pushButton_68")
        self.gridLayout_15.addWidget(self.pushButton_68, 1, 3, 1, 1)
        self.gridLayout_115.addWidget(self.frame_14, 0, 0, 1, 1)
        self.frame_94 = QtWidgets.QFrame(self.frame_15)
        self.frame_94.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_94.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_94.setObjectName("frame_94")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_94)
        self.gridLayout_16.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_16.setSpacing(6)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.frame_94)
        self.tableWidget_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_5.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 13pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_5.setLineWidth(1)
        self.tableWidget_5.setMidLineWidth(0)
        self.tableWidget_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_5.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget_5.setAlternatingRowColors(False)
        self.tableWidget_5.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_5.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_5.setShowGrid(False)
        self.tableWidget_5.setWordWrap(True)
        self.tableWidget_5.setCornerButtonEnabled(True)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(4)
        self.tableWidget_5.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        self.tableWidget_5.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_5.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.tableWidget_5.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_5.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_16.addWidget(self.tableWidget_5, 0, 0, 1, 1)
        self.gridLayout_115.addWidget(self.frame_94, 1, 0, 1, 1)
        self.gridLayout_17.addWidget(self.frame_15, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_6.setStyleSheet(
            "\n"
            "/*-----QTabWidget-----*/\n"
            "QTabBar::tab\n"
            "{\n"
            '    font: 11pt "Arabic Transparent Bold";\n'
            "    background-color: #262626;\n"
            "    color: rgb(27, 28, 30);\n"
            "    border-style: solid;\n"
            "    border-width: 0px;\n"
            "    border-top-left-radius: 3px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-color: #051a39;\n"
            "    width: 100px;\n"
            "    height: 30px;\n"
            "}\n"
            "QTabBar::tab:selected\n"
            "{\n"
            "    background-color: #003a5d;\n"
            "    color: #ffffff;\n"
            "    border-style: solid;\n"
            "    border-width: 0px;\n"
            "    border-top-left-radius: 3px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-color: #051a39;\n"
            "    width: 100px;\n"
            "    height: 30px;\n"
            "}\n"
            "QTabBar::tab:!selected \n"
            "{\n"
            "    background-color: #DFECFF;\n"
            "}\n"
            ""
        )
        self.tabWidget_6.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tab_23)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.frame_18 = QtWidgets.QFrame(self.tab_23)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_18.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "    border-top: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(85, 170, 255);\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_117 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_117.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_117.setSpacing(15)
        self.gridLayout_117.setObjectName("gridLayout_117")
        self.frame_96 = QtWidgets.QFrame(self.frame_18)
        self.frame_96.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_96.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_96.setObjectName("frame_96")
        self.gridLayout_116 = QtWidgets.QGridLayout(self.frame_96)
        self.gridLayout_116.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_116.setSpacing(6)
        self.gridLayout_116.setObjectName("gridLayout_116")
        self.label_21 = QtWidgets.QLabel(self.frame_96)
        self.label_21.setMinimumSize(QtCore.QSize(0, 30))
        self.label_21.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(245, 245, 245);\n"
            "border-style: solid;\n"
            "border-radius:0px;"
        )
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_116.addWidget(self.label_21, 0, 0, 1, 1)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.frame_96)
        self.tableWidget_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_6.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 13pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_6.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_6.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_6.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_6.setShowGrid(False)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(7)
        self.tableWidget_6.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, item)
        self.tableWidget_6.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_6.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_6.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tableWidget_6.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_6.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_6.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_116.addWidget(self.tableWidget_6, 1, 0, 1, 1)
        self.gridLayout_117.addWidget(self.frame_96, 2, 0, 1, 2)
        self.frame_17 = QtWidgets.QFrame(self.frame_18)
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_17.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_19.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_19.setHorizontalSpacing(5)
        self.gridLayout_19.setVerticalSpacing(0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_17)
        self.comboBox_7.setMinimumSize(QtCore.QSize(150, 50))
        self.comboBox_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_7.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}"
        )
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_19.addWidget(self.comboBox_7, 1, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_7.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_7.setMaxLength(9999999)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_19.addWidget(self.lineEdit_7, 1, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame_17)
        self.label_20.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_19.addWidget(self.label_20, 0, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_22.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_22.setMaximumSize(QtCore.QSize(120, 50))
        self.pushButton_22.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_19.addWidget(self.pushButton_22, 1, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame_17)
        self.label_18.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_19.addWidget(self.label_18, 0, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_17)
        self.label_19.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_19.addWidget(self.label_19, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_17)
        self.label_12.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_19.addWidget(self.label_12, 0, 0, 1, 1)
        self.spinBox_20 = QtWidgets.QSpinBox(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox_20.sizePolicy().hasHeightForWidth())
        self.spinBox_20.setSizePolicy(sizePolicy)
        self.spinBox_20.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_20.setMaximumSize(QtCore.QSize(250, 50))
        self.spinBox_20.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_20.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_20.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_20.setMaximum(999999999)
        self.spinBox_20.setObjectName("spinBox_20")
        self.gridLayout_19.addWidget(self.spinBox_20, 1, 3, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_17)
        self.comboBox_6.setMinimumSize(QtCore.QSize(150, 50))
        self.comboBox_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_6.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_6.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}"
        )
        self.comboBox_6.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.comboBox_6.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_6.setFrame(True)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_19.addWidget(self.comboBox_6, 1, 0, 1, 1)
        self.pushButton_69 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_69.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_69.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_69.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_69.setText("")
        self.pushButton_69.setIcon(icon2)
        self.pushButton_69.setObjectName("pushButton_69")
        self.gridLayout_19.addWidget(self.pushButton_69, 1, 5, 1, 1)
        self.gridLayout_117.addWidget(self.frame_17, 0, 0, 1, 2)
        self.gridLayout_21.addWidget(self.frame_18, 0, 0, 1, 1)
        self.tabWidget_6.addTab(self.tab_23, "")
        self.tab_25 = QtWidgets.QWidget()
        self.tab_25.setObjectName("tab_25")
        self.gridLayout_87 = QtWidgets.QGridLayout(self.tab_25)
        self.gridLayout_87.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_87.setSpacing(0)
        self.gridLayout_87.setObjectName("gridLayout_87")
        self.frame_52 = QtWidgets.QFrame(self.tab_25)
        self.frame_52.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_52.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "    border-top: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(85, 170, 255);\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.gridLayout_86 = QtWidgets.QGridLayout(self.frame_52)
        self.gridLayout_86.setObjectName("gridLayout_86")
        self.tabWidget_7 = QtWidgets.QTabWidget(self.frame_52)
        self.tabWidget_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_7.setStyleSheet(
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            ""
        )
        self.tabWidget_7.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.tab_26 = QtWidgets.QWidget()
        self.tab_26.setObjectName("tab_26")
        self.gridLayout_89 = QtWidgets.QGridLayout(self.tab_26)
        self.gridLayout_89.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_89.setSpacing(10)
        self.gridLayout_89.setObjectName("gridLayout_89")
        self.frame_53 = QtWidgets.QFrame(self.tab_26)
        self.frame_53.setMinimumSize(QtCore.QSize(400, 68))
        self.frame_53.setMaximumSize(QtCore.QSize(400, 68))
        self.frame_53.setStyleSheet(
            "\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.gridLayout_88 = QtWidgets.QGridLayout(self.frame_53)
        self.gridLayout_88.setObjectName("gridLayout_88")
        self.label_41 = QtWidgets.QLabel(self.frame_53)
        self.label_41.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_88.addWidget(self.label_41, 0, 0, 1, 1)
        self.spinBox_9 = QtWidgets.QDoubleSpinBox(self.frame_53)
        self.spinBox_9.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_9.setMaximumSize(QtCore.QSize(400, 50))
        self.spinBox_9.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_9.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_9.setMaximum(1e19)
        self.spinBox_9.setSingleStep(0.5)
        self.spinBox_9.setObjectName("spinBox_9")
        self.gridLayout_88.addWidget(self.spinBox_9, 0, 1, 1, 1)
        self.pushButton_83 = QtWidgets.QPushButton(self.frame_53)
        self.pushButton_83.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_83.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_83.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_83.setText("")
        self.pushButton_83.setIcon(icon2)
        self.pushButton_83.setObjectName("pushButton_83")
        self.gridLayout_88.addWidget(self.pushButton_83, 0, 2, 1, 1)
        self.gridLayout_89.addWidget(self.frame_53, 2, 0, 1, 1)
        self.tableWidget_21 = QtWidgets.QTableWidget(self.tab_26)
        self.tableWidget_21.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_21.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_21.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_21.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_21.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_21.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_21.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_21.setShowGrid(False)
        self.tableWidget_21.setRowCount(2)
        self.tableWidget_21.setObjectName("tableWidget_21")
        self.tableWidget_21.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(2, item)
        self.tableWidget_21.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_21.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_21.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_21.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_21.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_21.verticalHeader().setVisible(False)
        self.tableWidget_21.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_21.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_21.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_89.addWidget(self.tableWidget_21, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_26, "")
        self.tab_27 = QtWidgets.QWidget()
        self.tab_27.setObjectName("tab_27")
        self.gridLayout_93 = QtWidgets.QGridLayout(self.tab_27)
        self.gridLayout_93.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_93.setSpacing(10)
        self.gridLayout_93.setObjectName("gridLayout_93")
        self.tableWidget_23 = QtWidgets.QTableWidget(self.tab_27)
        self.tableWidget_23.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_23.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_23.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_23.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_23.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_23.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_23.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_23.setShowGrid(False)
        self.tableWidget_23.setRowCount(2)
        self.tableWidget_23.setObjectName("tableWidget_23")
        self.tableWidget_23.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(2, item)
        self.tableWidget_23.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_23.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_23.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_23.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_23.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_23.verticalHeader().setVisible(False)
        self.tableWidget_23.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_23.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_23.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_93.addWidget(self.tableWidget_23, 0, 0, 1, 1)
        self.frame_55 = QtWidgets.QFrame(self.tab_27)
        self.frame_55.setMinimumSize(QtCore.QSize(400, 68))
        self.frame_55.setMaximumSize(QtCore.QSize(400, 68))
        self.frame_55.setStyleSheet(
            "\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.gridLayout_92 = QtWidgets.QGridLayout(self.frame_55)
        self.gridLayout_92.setObjectName("gridLayout_92")
        self.label_44 = QtWidgets.QLabel(self.frame_55)
        self.label_44.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_92.addWidget(self.label_44, 0, 0, 1, 1)
        self.pushButton_84 = QtWidgets.QPushButton(self.frame_55)
        self.pushButton_84.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_84.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_84.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_84.setText("")
        self.pushButton_84.setIcon(icon2)
        self.pushButton_84.setObjectName("pushButton_84")
        self.gridLayout_92.addWidget(self.pushButton_84, 0, 2, 1, 1)
        self.spinBox_11 = QtWidgets.QDoubleSpinBox(self.frame_55)
        self.spinBox_11.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_11.setMaximumSize(QtCore.QSize(400, 50))
        self.spinBox_11.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_11.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_11.setMaximum(1e20)
        self.spinBox_11.setSingleStep(0.5)
        self.spinBox_11.setObjectName("spinBox_11")
        self.gridLayout_92.addWidget(self.spinBox_11, 0, 1, 1, 1)
        self.gridLayout_93.addWidget(self.frame_55, 1, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_27, "")
        self.tab_28 = QtWidgets.QWidget()
        self.tab_28.setObjectName("tab_28")
        self.gridLayout_95 = QtWidgets.QGridLayout(self.tab_28)
        self.gridLayout_95.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_95.setSpacing(10)
        self.gridLayout_95.setObjectName("gridLayout_95")
        self.tableWidget_24 = QtWidgets.QTableWidget(self.tab_28)
        self.tableWidget_24.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_24.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_24.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_24.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_24.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_24.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_24.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_24.setShowGrid(False)
        self.tableWidget_24.setRowCount(2)
        self.tableWidget_24.setObjectName("tableWidget_24")
        self.tableWidget_24.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(2, item)
        self.tableWidget_24.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_24.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_24.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_24.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_24.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_24.verticalHeader().setVisible(False)
        self.tableWidget_24.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_24.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_24.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_95.addWidget(self.tableWidget_24, 0, 0, 1, 1)
        self.frame_56 = QtWidgets.QFrame(self.tab_28)
        self.frame_56.setMinimumSize(QtCore.QSize(400, 68))
        self.frame_56.setMaximumSize(QtCore.QSize(400, 68))
        self.frame_56.setStyleSheet(
            "\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.gridLayout_94 = QtWidgets.QGridLayout(self.frame_56)
        self.gridLayout_94.setObjectName("gridLayout_94")
        self.label_45 = QtWidgets.QLabel(self.frame_56)
        self.label_45.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout_94.addWidget(self.label_45, 0, 0, 1, 1)
        self.pushButton_87 = QtWidgets.QPushButton(self.frame_56)
        self.pushButton_87.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_87.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_87.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_87.setText("")
        self.pushButton_87.setIcon(icon2)
        self.pushButton_87.setObjectName("pushButton_87")
        self.gridLayout_94.addWidget(self.pushButton_87, 0, 2, 1, 1)
        self.spinBox_12 = QtWidgets.QDoubleSpinBox(self.frame_56)
        self.spinBox_12.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_12.setMaximumSize(QtCore.QSize(400, 50))
        self.spinBox_12.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_12.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_12.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_12.setMaximum(1e20)
        self.spinBox_12.setSingleStep(0.5)
        self.spinBox_12.setObjectName("spinBox_12")
        self.gridLayout_94.addWidget(self.spinBox_12, 0, 1, 1, 1)
        self.gridLayout_95.addWidget(self.frame_56, 1, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_28, "")
        self.tab_29 = QtWidgets.QWidget()
        self.tab_29.setObjectName("tab_29")
        self.gridLayout_97 = QtWidgets.QGridLayout(self.tab_29)
        self.gridLayout_97.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_97.setSpacing(10)
        self.gridLayout_97.setObjectName("gridLayout_97")
        self.tableWidget_25 = QtWidgets.QTableWidget(self.tab_29)
        self.tableWidget_25.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_25.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_25.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_25.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_25.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_25.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_25.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_25.setShowGrid(False)
        self.tableWidget_25.setRowCount(2)
        self.tableWidget_25.setObjectName("tableWidget_25")
        self.tableWidget_25.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(2, item)
        self.tableWidget_25.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_25.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_25.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_25.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_25.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_25.verticalHeader().setVisible(False)
        self.tableWidget_25.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_25.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_25.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_97.addWidget(self.tableWidget_25, 0, 0, 1, 1)
        self.frame_61 = QtWidgets.QFrame(self.tab_29)
        self.frame_61.setMinimumSize(QtCore.QSize(400, 68))
        self.frame_61.setMaximumSize(QtCore.QSize(400, 68))
        self.frame_61.setStyleSheet(
            "\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.gridLayout_96 = QtWidgets.QGridLayout(self.frame_61)
        self.gridLayout_96.setObjectName("gridLayout_96")
        self.pushButton_88 = QtWidgets.QPushButton(self.frame_61)
        self.pushButton_88.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_88.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_88.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_88.setText("")
        self.pushButton_88.setIcon(icon2)
        self.pushButton_88.setObjectName("pushButton_88")
        self.gridLayout_96.addWidget(self.pushButton_88, 0, 2, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.frame_61)
        self.label_46.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout_96.addWidget(self.label_46, 0, 0, 1, 1)
        self.spinBox_13 = QtWidgets.QDoubleSpinBox(self.frame_61)
        self.spinBox_13.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_13.setMaximumSize(QtCore.QSize(400, 50))
        self.spinBox_13.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_13.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_13.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_13.setMaximum(1e24)
        self.spinBox_13.setSingleStep(0.5)
        self.spinBox_13.setObjectName("spinBox_13")
        self.gridLayout_96.addWidget(self.spinBox_13, 0, 1, 1, 1)
        self.gridLayout_97.addWidget(self.frame_61, 1, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_29, "")
        self.tab_30 = QtWidgets.QWidget()
        self.tab_30.setObjectName("tab_30")
        self.gridLayout_99 = QtWidgets.QGridLayout(self.tab_30)
        self.gridLayout_99.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_99.setSpacing(10)
        self.gridLayout_99.setObjectName("gridLayout_99")
        self.frame_62 = QtWidgets.QFrame(self.tab_30)
        self.frame_62.setMinimumSize(QtCore.QSize(400, 68))
        self.frame_62.setMaximumSize(QtCore.QSize(400, 68))
        self.frame_62.setStyleSheet(
            "\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.gridLayout_98 = QtWidgets.QGridLayout(self.frame_62)
        self.gridLayout_98.setObjectName("gridLayout_98")
        self.pushButton_89 = QtWidgets.QPushButton(self.frame_62)
        self.pushButton_89.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_89.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_89.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_89.setText("")
        self.pushButton_89.setIcon(icon2)
        self.pushButton_89.setObjectName("pushButton_89")
        self.gridLayout_98.addWidget(self.pushButton_89, 0, 2, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.frame_62)
        self.label_47.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout_98.addWidget(self.label_47, 0, 0, 1, 1)
        self.spinBox_14 = QtWidgets.QDoubleSpinBox(self.frame_62)
        self.spinBox_14.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_14.setMaximumSize(QtCore.QSize(400, 50))
        self.spinBox_14.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_14.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_14.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_14.setMaximum(1e21)
        self.spinBox_14.setSingleStep(0.5)
        self.spinBox_14.setObjectName("spinBox_14")
        self.gridLayout_98.addWidget(self.spinBox_14, 0, 1, 1, 1)
        self.gridLayout_99.addWidget(self.frame_62, 1, 0, 1, 1)
        self.tableWidget_26 = QtWidgets.QTableWidget(self.tab_30)
        self.tableWidget_26.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_26.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_26.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_26.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_26.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_26.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_26.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_26.setShowGrid(False)
        self.tableWidget_26.setRowCount(2)
        self.tableWidget_26.setObjectName("tableWidget_26")
        self.tableWidget_26.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_26.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_26.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_26.setHorizontalHeaderItem(2, item)
        self.tableWidget_26.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_26.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_26.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_26.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_26.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_26.verticalHeader().setVisible(False)
        self.tableWidget_26.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_26.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_26.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_99.addWidget(self.tableWidget_26, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_30, "")
        self.tab_31 = QtWidgets.QWidget()
        self.tab_31.setObjectName("tab_31")
        self.gridLayout_101 = QtWidgets.QGridLayout(self.tab_31)
        self.gridLayout_101.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_101.setSpacing(10)
        self.gridLayout_101.setObjectName("gridLayout_101")
        self.tableWidget_27 = QtWidgets.QTableWidget(self.tab_31)
        self.tableWidget_27.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_27.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_27.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_27.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_27.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_27.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_27.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_27.setShowGrid(False)
        self.tableWidget_27.setRowCount(2)
        self.tableWidget_27.setObjectName("tableWidget_27")
        self.tableWidget_27.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(2, item)
        self.tableWidget_27.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_27.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_27.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_27.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_27.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_27.verticalHeader().setVisible(False)
        self.tableWidget_27.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_27.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_27.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_101.addWidget(self.tableWidget_27, 0, 0, 1, 1)
        self.frame_63 = QtWidgets.QFrame(self.tab_31)
        self.frame_63.setMinimumSize(QtCore.QSize(400, 68))
        self.frame_63.setMaximumSize(QtCore.QSize(400, 68))
        self.frame_63.setStyleSheet(
            "\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.gridLayout_100 = QtWidgets.QGridLayout(self.frame_63)
        self.gridLayout_100.setObjectName("gridLayout_100")
        self.label_48 = QtWidgets.QLabel(self.frame_63)
        self.label_48.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.gridLayout_100.addWidget(self.label_48, 0, 0, 1, 1)
        self.pushButton_90 = QtWidgets.QPushButton(self.frame_63)
        self.pushButton_90.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_90.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_90.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_90.setText("")
        self.pushButton_90.setIcon(icon2)
        self.pushButton_90.setObjectName("pushButton_90")
        self.gridLayout_100.addWidget(self.pushButton_90, 0, 2, 1, 1)
        self.spinBox_15 = QtWidgets.QDoubleSpinBox(self.frame_63)
        self.spinBox_15.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_15.setMaximumSize(QtCore.QSize(400, 50))
        self.spinBox_15.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_15.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_15.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_15.setMaximum(1e29)
        self.spinBox_15.setSingleStep(0.5)
        self.spinBox_15.setObjectName("spinBox_15")
        self.gridLayout_100.addWidget(self.spinBox_15, 0, 1, 1, 1)
        self.gridLayout_101.addWidget(self.frame_63, 1, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_31, "")
        self.gridLayout_86.addWidget(self.tabWidget_7, 0, 0, 1, 1)
        self.gridLayout_87.addWidget(self.frame_52, 0, 0, 1, 1)
        self.tabWidget_6.addTab(self.tab_25, "")
        self.gridLayout_45.addWidget(self.tabWidget_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.frame_25 = QtWidgets.QFrame(self.tab_6)
        self.frame_25.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_25.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "    border-top: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(85, 170, 255);\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.gridLayout_152 = QtWidgets.QGridLayout(self.frame_25)
        self.gridLayout_152.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_152.setHorizontalSpacing(0)
        self.gridLayout_152.setVerticalSpacing(15)
        self.gridLayout_152.setObjectName("gridLayout_152")
        self.frame_24 = QtWidgets.QFrame(self.frame_25)
        self.frame_24.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_24.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.frame_24)
        self.gridLayout_27.setContentsMargins(25, 25, 25, 25)
        self.gridLayout_27.setSpacing(5)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_22 = QtWidgets.QLabel(self.frame_24)
        self.label_22.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_27.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_24)
        self.label_23.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_27.addWidget(self.label_23, 0, 2, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimumSize(QtCore.QSize(250, 50))
        self.spinBox_2.setMaximumSize(QtCore.QSize(250, 50))
        self.spinBox_2.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_27.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.comboBox_17 = QtWidgets.QComboBox(self.frame_24)
        self.comboBox_17.setMinimumSize(QtCore.QSize(250, 50))
        self.comboBox_17.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox_17.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_17.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }"
        )
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.gridLayout_27.addWidget(self.comboBox_17, 1, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_10.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_10.setMaxLength(9999999)
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_27.addWidget(self.lineEdit_10, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame_24)
        self.label_25.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_27.addWidget(self.label_25, 0, 1, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_29.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_29.setMaximumSize(QtCore.QSize(120, 50))
        self.pushButton_29.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_27.addWidget(self.pushButton_29, 1, 3, 1, 1)
        self.pushButton_70 = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_70.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_70.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_70.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_70.setText("")
        self.pushButton_70.setIcon(icon2)
        self.pushButton_70.setObjectName("pushButton_70")
        self.gridLayout_27.addWidget(self.pushButton_70, 1, 4, 1, 1)
        self.gridLayout_152.addWidget(self.frame_24, 0, 0, 1, 4)
        self.frame_110 = QtWidgets.QFrame(self.frame_25)
        self.frame_110.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_110.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_110.setObjectName("frame_110")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.frame_110)
        self.gridLayout_29.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_29.setSpacing(6)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.frame_110)
        self.tableWidget_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_7.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 13pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_7.setMidLineWidth(0)
        self.tableWidget_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_7.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_7.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget_7.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_7.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_7.setShowGrid(False)
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(5)
        self.tableWidget_7.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        self.tableWidget_7.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget_7.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_7.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_7.verticalHeader().setVisible(False)
        self.tableWidget_7.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_7.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_7.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_29.addWidget(self.tableWidget_7, 0, 0, 1, 1)
        self.gridLayout_152.addWidget(self.frame_110, 1, 0, 1, 4)
        self.frame_6 = QtWidgets.QFrame(self.frame_25)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_6.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_9.addWidget(self.label_24, 0, 2, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        self.spinBox_3.setMinimumSize(QtCore.QSize(200, 50))
        self.spinBox_3.setMaximumSize(QtCore.QSize(200, 50))
        self.spinBox_3.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_3.setMaximum(999999999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_9.addWidget(self.spinBox_3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            725, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_9.addItem(spacerItem4, 0, 1, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_30.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_30.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_30.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_9.addWidget(self.pushButton_30, 0, 0, 1, 1)
        self.gridLayout_152.addWidget(self.frame_6, 2, 2, 1, 1)
        self.gridLayout_28.addWidget(self.frame_25, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.frame_26 = QtWidgets.QFrame(self.tab_7)
        self.frame_26.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_26.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "    border-top: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.frame_26)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.frame_60 = QtWidgets.QFrame(self.frame_26)
        self.frame_60.setMinimumSize(QtCore.QSize(260, 50))
        self.frame_60.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_60.setStyleSheet(
            "QFrame{\n"
            'font: 9pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "background-color: #003a5d;\n"
            "border-width: 0x;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "}"
        )
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.gridLayout_103 = QtWidgets.QGridLayout(self.frame_60)
        self.gridLayout_103.setObjectName("gridLayout_103")
        self.label_183 = QtWidgets.QLabel(self.frame_60)
        self.label_183.setMinimumSize(QtCore.QSize(45, 0))
        self.label_183.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_183.setAlignment(QtCore.Qt.AlignCenter)
        self.label_183.setObjectName("label_183")
        self.gridLayout_103.addWidget(self.label_183, 0, 2, 3, 1)
        self.label_179 = QtWidgets.QLabel(self.frame_60)
        self.label_179.setMinimumSize(QtCore.QSize(38, 0))
        self.label_179.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_179.setAlignment(QtCore.Qt.AlignCenter)
        self.label_179.setObjectName("label_179")
        self.gridLayout_103.addWidget(self.label_179, 0, 3, 3, 1)
        self.label_180 = QtWidgets.QLabel(self.frame_60)
        self.label_180.setMinimumSize(QtCore.QSize(125, 0))
        self.label_180.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_180.setAlignment(QtCore.Qt.AlignCenter)
        self.label_180.setObjectName("label_180")
        self.gridLayout_103.addWidget(self.label_180, 0, 1, 3, 1)
        self.label_182 = QtWidgets.QLabel(self.frame_60)
        self.label_182.setMinimumSize(QtCore.QSize(62, 0))
        self.label_182.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_182.setAlignment(QtCore.Qt.AlignCenter)
        self.label_182.setObjectName("label_182")
        self.gridLayout_103.addWidget(self.label_182, 0, 4, 3, 1)
        self.label_49 = QtWidgets.QLabel(self.frame_60)
        self.label_49.setMinimumSize(QtCore.QSize(230, 0))
        self.label_49.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_49.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_49.setText("")
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout_103.addWidget(self.label_49, 0, 5, 3, 1)
        self.gridLayout_32.addWidget(self.frame_60, 0, 0, 1, 1)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.frame_26)
        self.scrollArea_4.setStyleSheet(
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1103, 839))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_30 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_30.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_30.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.gridLayout_118 = QtWidgets.QGridLayout(self.frame_30)
        self.gridLayout_118.setObjectName("gridLayout_118")
        self.label_185 = QtWidgets.QLabel(self.frame_30)
        self.label_185.setMinimumSize(QtCore.QSize(45, 0))
        self.label_185.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_185.setAlignment(QtCore.Qt.AlignCenter)
        self.label_185.setObjectName("label_185")
        self.gridLayout_118.addWidget(self.label_185, 0, 2, 1, 1)
        self.label_184 = QtWidgets.QLabel(self.frame_30)
        self.label_184.setMinimumSize(QtCore.QSize(45, 0))
        self.label_184.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_184.setAlignment(QtCore.Qt.AlignCenter)
        self.label_184.setObjectName("label_184")
        self.gridLayout_118.addWidget(self.label_184, 0, 3, 1, 1)
        self.label_186 = QtWidgets.QLabel(self.frame_30)
        self.label_186.setMinimumSize(QtCore.QSize(45, 0))
        self.label_186.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_186.setAlignment(QtCore.Qt.AlignCenter)
        self.label_186.setObjectName("label_186")
        self.gridLayout_118.addWidget(self.label_186, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_30)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_118.addWidget(self.label_2, 0, 4, 1, 1)
        self.label_187 = QtWidgets.QLabel(self.frame_30)
        self.label_187.setMinimumSize(QtCore.QSize(45, 0))
        self.label_187.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_187.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_187.setAlignment(QtCore.Qt.AlignCenter)
        self.label_187.setObjectName("label_187")
        self.gridLayout_118.addWidget(self.label_187, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_30)
        self.frame_41 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_41.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_41.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.gridLayout_119 = QtWidgets.QGridLayout(self.frame_41)
        self.gridLayout_119.setObjectName("gridLayout_119")
        self.label_244 = QtWidgets.QLabel(self.frame_41)
        self.label_244.setMinimumSize(QtCore.QSize(45, 0))
        self.label_244.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_244.setAlignment(QtCore.Qt.AlignCenter)
        self.label_244.setObjectName("label_244")
        self.gridLayout_119.addWidget(self.label_244, 0, 3, 1, 1)
        self.label_245 = QtWidgets.QLabel(self.frame_41)
        self.label_245.setMinimumSize(QtCore.QSize(45, 0))
        self.label_245.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_245.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_245.setAlignment(QtCore.Qt.AlignCenter)
        self.label_245.setObjectName("label_245")
        self.gridLayout_119.addWidget(self.label_245, 0, 0, 1, 1)
        self.label_246 = QtWidgets.QLabel(self.frame_41)
        self.label_246.setMinimumSize(QtCore.QSize(45, 0))
        self.label_246.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_246.setAlignment(QtCore.Qt.AlignCenter)
        self.label_246.setObjectName("label_246")
        self.gridLayout_119.addWidget(self.label_246, 0, 1, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.frame_41)
        self.label_57.setMinimumSize(QtCore.QSize(150, 0))
        self.label_57.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_57.setText("")
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.gridLayout_119.addWidget(self.label_57, 0, 4, 1, 1)
        self.label_247 = QtWidgets.QLabel(self.frame_41)
        self.label_247.setMinimumSize(QtCore.QSize(45, 0))
        self.label_247.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_247.setAlignment(QtCore.Qt.AlignCenter)
        self.label_247.setObjectName("label_247")
        self.gridLayout_119.addWidget(self.label_247, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_41)
        self.frame_64 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_64.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_64.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_64.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.gridLayout_120 = QtWidgets.QGridLayout(self.frame_64)
        self.gridLayout_120.setObjectName("gridLayout_120")
        self.label_248 = QtWidgets.QLabel(self.frame_64)
        self.label_248.setMinimumSize(QtCore.QSize(45, 0))
        self.label_248.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_248.setAlignment(QtCore.Qt.AlignCenter)
        self.label_248.setObjectName("label_248")
        self.gridLayout_120.addWidget(self.label_248, 0, 3, 1, 1)
        self.label_249 = QtWidgets.QLabel(self.frame_64)
        self.label_249.setMinimumSize(QtCore.QSize(45, 0))
        self.label_249.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_249.setAlignment(QtCore.Qt.AlignCenter)
        self.label_249.setObjectName("label_249")
        self.gridLayout_120.addWidget(self.label_249, 0, 0, 1, 1)
        self.label_250 = QtWidgets.QLabel(self.frame_64)
        self.label_250.setMinimumSize(QtCore.QSize(45, 0))
        self.label_250.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_250.setAlignment(QtCore.Qt.AlignCenter)
        self.label_250.setObjectName("label_250")
        self.gridLayout_120.addWidget(self.label_250, 0, 1, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.frame_64)
        self.label_58.setMinimumSize(QtCore.QSize(150, 0))
        self.label_58.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_58.setText("")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.gridLayout_120.addWidget(self.label_58, 0, 4, 1, 1)
        self.label_251 = QtWidgets.QLabel(self.frame_64)
        self.label_251.setMinimumSize(QtCore.QSize(45, 0))
        self.label_251.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_251.setAlignment(QtCore.Qt.AlignCenter)
        self.label_251.setObjectName("label_251")
        self.gridLayout_120.addWidget(self.label_251, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_64)
        self.frame_65 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_65.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_65.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.gridLayout_121 = QtWidgets.QGridLayout(self.frame_65)
        self.gridLayout_121.setObjectName("gridLayout_121")
        self.label_252 = QtWidgets.QLabel(self.frame_65)
        self.label_252.setMinimumSize(QtCore.QSize(45, 0))
        self.label_252.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_252.setAlignment(QtCore.Qt.AlignCenter)
        self.label_252.setObjectName("label_252")
        self.gridLayout_121.addWidget(self.label_252, 0, 3, 1, 1)
        self.label_253 = QtWidgets.QLabel(self.frame_65)
        self.label_253.setMinimumSize(QtCore.QSize(45, 0))
        self.label_253.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_253.setAlignment(QtCore.Qt.AlignCenter)
        self.label_253.setObjectName("label_253")
        self.gridLayout_121.addWidget(self.label_253, 0, 0, 1, 1)
        self.label_254 = QtWidgets.QLabel(self.frame_65)
        self.label_254.setMinimumSize(QtCore.QSize(45, 0))
        self.label_254.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_254.setAlignment(QtCore.Qt.AlignCenter)
        self.label_254.setObjectName("label_254")
        self.gridLayout_121.addWidget(self.label_254, 0, 1, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.frame_65)
        self.label_59.setMinimumSize(QtCore.QSize(150, 0))
        self.label_59.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_59.setText("")
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.gridLayout_121.addWidget(self.label_59, 0, 4, 1, 1)
        self.label_255 = QtWidgets.QLabel(self.frame_65)
        self.label_255.setMinimumSize(QtCore.QSize(45, 0))
        self.label_255.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_255.setAlignment(QtCore.Qt.AlignCenter)
        self.label_255.setObjectName("label_255")
        self.gridLayout_121.addWidget(self.label_255, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_65)
        self.frame_75 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_75.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_75.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_75.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.gridLayout_131 = QtWidgets.QGridLayout(self.frame_75)
        self.gridLayout_131.setObjectName("gridLayout_131")
        self.label_292 = QtWidgets.QLabel(self.frame_75)
        self.label_292.setMinimumSize(QtCore.QSize(45, 0))
        self.label_292.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_292.setAlignment(QtCore.Qt.AlignCenter)
        self.label_292.setObjectName("label_292")
        self.gridLayout_131.addWidget(self.label_292, 0, 3, 1, 1)
        self.label_293 = QtWidgets.QLabel(self.frame_75)
        self.label_293.setMinimumSize(QtCore.QSize(45, 0))
        self.label_293.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_293.setAlignment(QtCore.Qt.AlignCenter)
        self.label_293.setObjectName("label_293")
        self.gridLayout_131.addWidget(self.label_293, 0, 0, 1, 1)
        self.label_294 = QtWidgets.QLabel(self.frame_75)
        self.label_294.setMinimumSize(QtCore.QSize(45, 0))
        self.label_294.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_294.setAlignment(QtCore.Qt.AlignCenter)
        self.label_294.setObjectName("label_294")
        self.gridLayout_131.addWidget(self.label_294, 0, 1, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.frame_75)
        self.label_77.setMinimumSize(QtCore.QSize(150, 0))
        self.label_77.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_77.setText("")
        self.label_77.setAlignment(QtCore.Qt.AlignCenter)
        self.label_77.setObjectName("label_77")
        self.gridLayout_131.addWidget(self.label_77, 0, 4, 1, 1)
        self.label_295 = QtWidgets.QLabel(self.frame_75)
        self.label_295.setMinimumSize(QtCore.QSize(45, 0))
        self.label_295.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_295.setAlignment(QtCore.Qt.AlignCenter)
        self.label_295.setObjectName("label_295")
        self.gridLayout_131.addWidget(self.label_295, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_75)
        self.frame_74 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_74.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_74.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_74.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.gridLayout_130 = QtWidgets.QGridLayout(self.frame_74)
        self.gridLayout_130.setObjectName("gridLayout_130")
        self.label_288 = QtWidgets.QLabel(self.frame_74)
        self.label_288.setMinimumSize(QtCore.QSize(45, 0))
        self.label_288.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_288.setAlignment(QtCore.Qt.AlignCenter)
        self.label_288.setObjectName("label_288")
        self.gridLayout_130.addWidget(self.label_288, 0, 3, 1, 1)
        self.label_289 = QtWidgets.QLabel(self.frame_74)
        self.label_289.setMinimumSize(QtCore.QSize(45, 0))
        self.label_289.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_289.setAlignment(QtCore.Qt.AlignCenter)
        self.label_289.setObjectName("label_289")
        self.gridLayout_130.addWidget(self.label_289, 0, 0, 1, 1)
        self.label_290 = QtWidgets.QLabel(self.frame_74)
        self.label_290.setMinimumSize(QtCore.QSize(45, 0))
        self.label_290.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_290.setAlignment(QtCore.Qt.AlignCenter)
        self.label_290.setObjectName("label_290")
        self.gridLayout_130.addWidget(self.label_290, 0, 1, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.frame_74)
        self.label_76.setMinimumSize(QtCore.QSize(150, 0))
        self.label_76.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_76.setText("")
        self.label_76.setAlignment(QtCore.Qt.AlignCenter)
        self.label_76.setObjectName("label_76")
        self.gridLayout_130.addWidget(self.label_76, 0, 4, 1, 1)
        self.label_291 = QtWidgets.QLabel(self.frame_74)
        self.label_291.setMinimumSize(QtCore.QSize(45, 0))
        self.label_291.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_291.setAlignment(QtCore.Qt.AlignCenter)
        self.label_291.setObjectName("label_291")
        self.gridLayout_130.addWidget(self.label_291, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_74)
        self.frame_73 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_73.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_73.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_73.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.gridLayout_129 = QtWidgets.QGridLayout(self.frame_73)
        self.gridLayout_129.setObjectName("gridLayout_129")
        self.label_284 = QtWidgets.QLabel(self.frame_73)
        self.label_284.setMinimumSize(QtCore.QSize(45, 0))
        self.label_284.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_284.setAlignment(QtCore.Qt.AlignCenter)
        self.label_284.setObjectName("label_284")
        self.gridLayout_129.addWidget(self.label_284, 0, 3, 1, 1)
        self.label_285 = QtWidgets.QLabel(self.frame_73)
        self.label_285.setMinimumSize(QtCore.QSize(45, 0))
        self.label_285.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;\n"
            ""
        )
        self.label_285.setAlignment(QtCore.Qt.AlignCenter)
        self.label_285.setObjectName("label_285")
        self.gridLayout_129.addWidget(self.label_285, 0, 0, 1, 1)
        self.label_286 = QtWidgets.QLabel(self.frame_73)
        self.label_286.setMinimumSize(QtCore.QSize(45, 0))
        self.label_286.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_286.setAlignment(QtCore.Qt.AlignCenter)
        self.label_286.setObjectName("label_286")
        self.gridLayout_129.addWidget(self.label_286, 0, 1, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.frame_73)
        self.label_67.setMinimumSize(QtCore.QSize(150, 0))
        self.label_67.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_67.setText("")
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.gridLayout_129.addWidget(self.label_67, 0, 4, 1, 1)
        self.label_287 = QtWidgets.QLabel(self.frame_73)
        self.label_287.setMinimumSize(QtCore.QSize(45, 0))
        self.label_287.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_287.setAlignment(QtCore.Qt.AlignCenter)
        self.label_287.setObjectName("label_287")
        self.gridLayout_129.addWidget(self.label_287, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_73)
        self.frame_72 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_72.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_72.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_72.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.gridLayout_128 = QtWidgets.QGridLayout(self.frame_72)
        self.gridLayout_128.setObjectName("gridLayout_128")
        self.label_280 = QtWidgets.QLabel(self.frame_72)
        self.label_280.setMinimumSize(QtCore.QSize(45, 0))
        self.label_280.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_280.setAlignment(QtCore.Qt.AlignCenter)
        self.label_280.setObjectName("label_280")
        self.gridLayout_128.addWidget(self.label_280, 0, 3, 1, 1)
        self.label_281 = QtWidgets.QLabel(self.frame_72)
        self.label_281.setMinimumSize(QtCore.QSize(45, 0))
        self.label_281.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_281.setAlignment(QtCore.Qt.AlignCenter)
        self.label_281.setObjectName("label_281")
        self.gridLayout_128.addWidget(self.label_281, 0, 0, 1, 1)
        self.label_282 = QtWidgets.QLabel(self.frame_72)
        self.label_282.setMinimumSize(QtCore.QSize(45, 0))
        self.label_282.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_282.setAlignment(QtCore.Qt.AlignCenter)
        self.label_282.setObjectName("label_282")
        self.gridLayout_128.addWidget(self.label_282, 0, 1, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.frame_72)
        self.label_66.setMinimumSize(QtCore.QSize(150, 0))
        self.label_66.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_66.setText("")
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.gridLayout_128.addWidget(self.label_66, 0, 4, 1, 1)
        self.label_283 = QtWidgets.QLabel(self.frame_72)
        self.label_283.setMinimumSize(QtCore.QSize(45, 0))
        self.label_283.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_283.setAlignment(QtCore.Qt.AlignCenter)
        self.label_283.setObjectName("label_283")
        self.gridLayout_128.addWidget(self.label_283, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_72)
        self.frame_66 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_66.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_66.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.gridLayout_122 = QtWidgets.QGridLayout(self.frame_66)
        self.gridLayout_122.setObjectName("gridLayout_122")
        self.label_256 = QtWidgets.QLabel(self.frame_66)
        self.label_256.setMinimumSize(QtCore.QSize(45, 0))
        self.label_256.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_256.setAlignment(QtCore.Qt.AlignCenter)
        self.label_256.setObjectName("label_256")
        self.gridLayout_122.addWidget(self.label_256, 0, 3, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.frame_66)
        self.label_60.setMinimumSize(QtCore.QSize(150, 0))
        self.label_60.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_60.setText("")
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.gridLayout_122.addWidget(self.label_60, 0, 4, 1, 1)
        self.label_259 = QtWidgets.QLabel(self.frame_66)
        self.label_259.setMinimumSize(QtCore.QSize(45, 0))
        self.label_259.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_259.setAlignment(QtCore.Qt.AlignCenter)
        self.label_259.setObjectName("label_259")
        self.gridLayout_122.addWidget(self.label_259, 0, 2, 1, 1)
        self.label_257 = QtWidgets.QLabel(self.frame_66)
        self.label_257.setMinimumSize(QtCore.QSize(45, 0))
        self.label_257.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_257.setAlignment(QtCore.Qt.AlignCenter)
        self.label_257.setObjectName("label_257")
        self.gridLayout_122.addWidget(self.label_257, 0, 0, 1, 1)
        self.label_258 = QtWidgets.QLabel(self.frame_66)
        self.label_258.setMinimumSize(QtCore.QSize(45, 0))
        self.label_258.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_258.setAlignment(QtCore.Qt.AlignCenter)
        self.label_258.setObjectName("label_258")
        self.gridLayout_122.addWidget(self.label_258, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_66)
        self.frame_71 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_71.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_71.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_71.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.gridLayout_127 = QtWidgets.QGridLayout(self.frame_71)
        self.gridLayout_127.setObjectName("gridLayout_127")
        self.label_276 = QtWidgets.QLabel(self.frame_71)
        self.label_276.setMinimumSize(QtCore.QSize(45, 0))
        self.label_276.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_276.setAlignment(QtCore.Qt.AlignCenter)
        self.label_276.setObjectName("label_276")
        self.gridLayout_127.addWidget(self.label_276, 0, 3, 1, 1)
        self.label_277 = QtWidgets.QLabel(self.frame_71)
        self.label_277.setMinimumSize(QtCore.QSize(45, 0))
        self.label_277.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_277.setAlignment(QtCore.Qt.AlignCenter)
        self.label_277.setObjectName("label_277")
        self.gridLayout_127.addWidget(self.label_277, 0, 0, 1, 1)
        self.label_278 = QtWidgets.QLabel(self.frame_71)
        self.label_278.setMinimumSize(QtCore.QSize(45, 0))
        self.label_278.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_278.setAlignment(QtCore.Qt.AlignCenter)
        self.label_278.setObjectName("label_278")
        self.gridLayout_127.addWidget(self.label_278, 0, 1, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.frame_71)
        self.label_65.setMinimumSize(QtCore.QSize(150, 0))
        self.label_65.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_65.setText("")
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.gridLayout_127.addWidget(self.label_65, 0, 4, 1, 1)
        self.label_279 = QtWidgets.QLabel(self.frame_71)
        self.label_279.setMinimumSize(QtCore.QSize(45, 0))
        self.label_279.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_279.setAlignment(QtCore.Qt.AlignCenter)
        self.label_279.setObjectName("label_279")
        self.gridLayout_127.addWidget(self.label_279, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_71)
        self.frame_70 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_70.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_70.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_70.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.gridLayout_126 = QtWidgets.QGridLayout(self.frame_70)
        self.gridLayout_126.setObjectName("gridLayout_126")
        self.label_272 = QtWidgets.QLabel(self.frame_70)
        self.label_272.setMinimumSize(QtCore.QSize(45, 0))
        self.label_272.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_272.setAlignment(QtCore.Qt.AlignCenter)
        self.label_272.setObjectName("label_272")
        self.gridLayout_126.addWidget(self.label_272, 0, 3, 1, 1)
        self.label_273 = QtWidgets.QLabel(self.frame_70)
        self.label_273.setMinimumSize(QtCore.QSize(45, 0))
        self.label_273.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_273.setAlignment(QtCore.Qt.AlignCenter)
        self.label_273.setObjectName("label_273")
        self.gridLayout_126.addWidget(self.label_273, 0, 0, 1, 1)
        self.label_274 = QtWidgets.QLabel(self.frame_70)
        self.label_274.setMinimumSize(QtCore.QSize(45, 0))
        self.label_274.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_274.setAlignment(QtCore.Qt.AlignCenter)
        self.label_274.setObjectName("label_274")
        self.gridLayout_126.addWidget(self.label_274, 0, 1, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.frame_70)
        self.label_64.setMinimumSize(QtCore.QSize(150, 0))
        self.label_64.setStyleSheet(
            "    border-radius: 15px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.label_64.setText("")
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.gridLayout_126.addWidget(self.label_64, 0, 4, 1, 1)
        self.label_275 = QtWidgets.QLabel(self.frame_70)
        self.label_275.setMinimumSize(QtCore.QSize(45, 0))
        self.label_275.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_275.setAlignment(QtCore.Qt.AlignCenter)
        self.label_275.setObjectName("label_275")
        self.gridLayout_126.addWidget(self.label_275, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_70)
        self.frame_67 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_67.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_67.setStyleSheet(
            "    border-radius: 5px;\n"
            "    border: 1;\n"
            '    font: 11pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.gridLayout_123 = QtWidgets.QGridLayout(self.frame_67)
        self.gridLayout_123.setObjectName("gridLayout_123")
        self.label_261 = QtWidgets.QLabel(self.frame_67)
        self.label_261.setMinimumSize(QtCore.QSize(150, 0))
        self.label_261.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width:0px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: #8B8B8B;"
        )
        self.label_261.setAlignment(QtCore.Qt.AlignCenter)
        self.label_261.setObjectName("label_261")
        self.gridLayout_123.addWidget(self.label_261, 0, 0, 1, 1)
        self.label_262 = QtWidgets.QLabel(self.frame_67)
        self.label_262.setMinimumSize(QtCore.QSize(45, 0))
        self.label_262.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_262.setAlignment(QtCore.Qt.AlignCenter)
        self.label_262.setObjectName("label_262")
        self.gridLayout_123.addWidget(self.label_262, 0, 1, 1, 1)
        self.label_260 = QtWidgets.QLabel(self.frame_67)
        self.label_260.setMinimumSize(QtCore.QSize(45, 0))
        self.label_260.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_260.setAlignment(QtCore.Qt.AlignCenter)
        self.label_260.setObjectName("label_260")
        self.gridLayout_123.addWidget(self.label_260, 0, 3, 1, 1)
        self.label_263 = QtWidgets.QLabel(self.frame_67)
        self.label_263.setMinimumSize(QtCore.QSize(45, 0))
        self.label_263.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_263.setAlignment(QtCore.Qt.AlignCenter)
        self.label_263.setObjectName("label_263")
        self.gridLayout_123.addWidget(self.label_263, 0, 2, 1, 1)
        self.frame_21 = QtWidgets.QFrame(self.frame_67)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_142 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_142.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_142.setSpacing(0)
        self.gridLayout_142.setObjectName("gridLayout_142")
        self.pushButton_72 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_72.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_72.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_72.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_72.setText("")
        self.pushButton_72.setIcon(icon2)
        self.pushButton_72.setObjectName("pushButton_72")
        self.gridLayout_142.addWidget(self.pushButton_72, 0, 0, 1, 1)
        self.gridLayout_123.addWidget(self.frame_21, 0, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_67)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_32.addWidget(self.scrollArea_4, 1, 0, 1, 1)
        self.gridLayout_31.addWidget(self.frame_26, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_37.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_37.setSpacing(10)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.frame_31 = QtWidgets.QFrame(self.tab_8)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_31.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    \n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 5px;\n"
            "      border: none;\n"
            "      border-bottom: 1px solid #ccc;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(85, 170, 255);\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.frame_31)
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_36.setSpacing(15)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.gridLayout_37.addWidget(self.frame_31, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_43.setSpacing(0)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_9)
        self.tabWidget_3.setStyleSheet(
            "\n"
            "/*-----QTabWidget-----*/\n"
            "QTabBar::tab\n"
            "{\n"
            '    font: 11pt "Arabic Transparent Bold";\n'
            "    background-color: #262626;\n"
            "    color: rgb(27, 28, 30);\n"
            "    border-style: solid;\n"
            "    border-width: 0px;\n"
            "    border-top-left-radius: 3px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-color: #051a39;\n"
            "    width: 100px;\n"
            "    height: 30px;\n"
            "}\n"
            "QTabBar::tab:selected\n"
            "{\n"
            "    background-color: #003a5d;\n"
            "    color: #ffffff;\n"
            "    border-style: solid;\n"
            "    border-width: 0px;\n"
            "    border-top-left-radius: 3px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-color: #051a39;\n"
            "    width: 100px;\n"
            "    height: 30px;\n"
            "}\n"
            "QTabBar::tab:!selected \n"
            "{\n"
            "    background-color: #DFECFF;\n"
            "}\n"
            ""
        )
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.gridLayout_44 = QtWidgets.QGridLayout(self.tab_15)
        self.gridLayout_44.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.frame_34 = QtWidgets.QFrame(self.tab_15)
        self.frame_34.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_34.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "    border-top: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(85, 170, 255);\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.frame_34)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.tabWidget_8 = QtWidgets.QTabWidget(self.frame_34)
        self.tabWidget_8.setTabBarAutoHide(True)
        self.tabWidget_8.setObjectName("tabWidget_8")
        self.tab_24 = QtWidgets.QWidget()
        self.tab_24.setObjectName("tab_24")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tab_24)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setSpacing(25)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.frame_89 = QtWidgets.QFrame(self.tab_24)
        self.frame_89.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 1;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_89.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_89.setObjectName("frame_89")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.frame_89)
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_33.setSpacing(25)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.frame_10 = QtWidgets.QFrame(self.frame_89)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_10.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.frame_86 = QtWidgets.QFrame(self.frame_10)
        self.frame_86.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_86.setObjectName("frame_86")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_86)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_217 = QtWidgets.QLabel(self.frame_86)
        self.label_217.setMinimumSize(QtCore.QSize(38, 0))
        self.label_217.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_217.setAlignment(QtCore.Qt.AlignCenter)
        self.label_217.setObjectName("label_217")
        self.verticalLayout_6.addWidget(self.label_217)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame_86)
        self.lineEdit_34.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_34.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_34.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_34.setMaxLength(9999999)
        self.lineEdit_34.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_34.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.verticalLayout_6.addWidget(self.lineEdit_34)
        self.gridLayout_25.addWidget(self.frame_86, 0, 1, 1, 1)
        self.frame_88 = QtWidgets.QFrame(self.frame_10)
        self.frame_88.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_88.setObjectName("frame_88")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_88)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_218 = QtWidgets.QLabel(self.frame_88)
        self.label_218.setMinimumSize(QtCore.QSize(38, 0))
        self.label_218.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_218.setAlignment(QtCore.Qt.AlignCenter)
        self.label_218.setObjectName("label_218")
        self.verticalLayout_5.addWidget(self.label_218)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.frame_88)
        self.doubleSpinBox_7.setMinimumSize(QtCore.QSize(250, 50))
        self.doubleSpinBox_7.setMaximumSize(QtCore.QSize(400, 50))
        self.doubleSpinBox_7.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_7.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_7.setMaximum(1e28)
        self.doubleSpinBox_7.setSingleStep(0.5)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.verticalLayout_5.addWidget(self.doubleSpinBox_7)
        self.gridLayout_25.addWidget(self.frame_88, 0, 2, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_35.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_35.setMaximumSize(QtCore.QSize(120, 50))
        self.pushButton_35.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_25.addWidget(self.pushButton_35, 0, 3, 1, 1)
        self.frame_85 = QtWidgets.QFrame(self.frame_10)
        self.frame_85.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_85.setObjectName("frame_85")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_85)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_216 = QtWidgets.QLabel(self.frame_85)
        self.label_216.setMinimumSize(QtCore.QSize(38, 0))
        self.label_216.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_216.setAlignment(QtCore.Qt.AlignCenter)
        self.label_216.setObjectName("label_216")
        self.verticalLayout_7.addWidget(self.label_216)
        self.comboBox_12 = QtWidgets.QComboBox(self.frame_85)
        self.comboBox_12.setMinimumSize(QtCore.QSize(200, 50))
        self.comboBox_12.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_12.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}"
        )
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_12)
        self.gridLayout_25.addWidget(self.frame_85, 0, 0, 1, 1)
        self.pushButton_91 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_91.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_91.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_91.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_91.setText("")
        self.pushButton_91.setIcon(icon2)
        self.pushButton_91.setObjectName("pushButton_91")
        self.gridLayout_25.addWidget(self.pushButton_91, 0, 4, 1, 1)
        self.gridLayout_33.addWidget(self.frame_10, 0, 0, 1, 1)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame_89)
        self.tableWidget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.tableWidget_3.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 13pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_3.setShowGrid(False)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_33.addWidget(self.tableWidget_3, 1, 0, 1, 1)
        self.frame_57 = QtWidgets.QFrame(self.frame_89)
        self.frame_57.setMinimumSize(QtCore.QSize(400, 68))
        self.frame_57.setMaximumSize(QtCore.QSize(400, 68))
        self.frame_57.setStyleSheet(
            "\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.gridLayout_157 = QtWidgets.QGridLayout(self.frame_57)
        self.gridLayout_157.setObjectName("gridLayout_157")
        self.label_62 = QtWidgets.QLabel(self.frame_57)
        self.label_62.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.gridLayout_157.addWidget(self.label_62, 0, 0, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.frame_57)
        self.doubleSpinBox_9.setMinimumSize(QtCore.QSize(250, 50))
        self.doubleSpinBox_9.setMaximumSize(QtCore.QSize(400, 50))
        self.doubleSpinBox_9.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_9.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_9.setMaximum(100000.0)
        self.doubleSpinBox_9.setSingleStep(0.5)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout_157.addWidget(self.doubleSpinBox_9, 0, 1, 1, 1)
        self.gridLayout_33.addWidget(self.frame_57, 2, 0, 1, 1)
        self.gridLayout_24.addWidget(self.frame_89, 0, 0, 1, 1)
        self.tabWidget_8.addTab(self.tab_24, "")
        self.tab_32 = QtWidgets.QWidget()
        self.tab_32.setObjectName("tab_32")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tab_32)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.frame_90 = QtWidgets.QFrame(self.tab_32)
        self.frame_90.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 1;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;"
        )
        self.frame_90.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_90.setObjectName("frame_90")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.frame_90)
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_40.setSpacing(25)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.frame_13 = QtWidgets.QFrame(self.frame_90)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_13.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}"
        )
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.frame_92 = QtWidgets.QFrame(self.frame_13)
        self.frame_92.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_92.setObjectName("frame_92")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_92)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_221 = QtWidgets.QLabel(self.frame_92)
        self.label_221.setMinimumSize(QtCore.QSize(38, 0))
        self.label_221.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_221.setAlignment(QtCore.Qt.AlignCenter)
        self.label_221.setObjectName("label_221")
        self.verticalLayout_10.addWidget(self.label_221)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.frame_92)
        self.doubleSpinBox_8.setMinimumSize(QtCore.QSize(250, 50))
        self.doubleSpinBox_8.setMaximumSize(QtCore.QSize(400, 50))
        self.doubleSpinBox_8.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_8.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_8.setMaximum(1e24)
        self.doubleSpinBox_8.setSingleStep(0.5)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.verticalLayout_10.addWidget(self.doubleSpinBox_8)
        self.gridLayout_34.addWidget(self.frame_92, 0, 2, 1, 1)
        self.frame_91 = QtWidgets.QFrame(self.frame_13)
        self.frame_91.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_91.setObjectName("frame_91")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_91)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_220 = QtWidgets.QLabel(self.frame_91)
        self.label_220.setMinimumSize(QtCore.QSize(38, 0))
        self.label_220.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_220.setAlignment(QtCore.Qt.AlignCenter)
        self.label_220.setObjectName("label_220")
        self.verticalLayout_9.addWidget(self.label_220)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.frame_91)
        self.lineEdit_36.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_36.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_36.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_36.setMaxLength(9999999)
        self.lineEdit_36.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_36.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.verticalLayout_9.addWidget(self.lineEdit_36)
        self.gridLayout_34.addWidget(self.frame_91, 0, 1, 1, 1)
        self.frame_87 = QtWidgets.QFrame(self.frame_13)
        self.frame_87.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_87.setObjectName("frame_87")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_87)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_219 = QtWidgets.QLabel(self.frame_87)
        self.label_219.setMinimumSize(QtCore.QSize(38, 0))
        self.label_219.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_219.setAlignment(QtCore.Qt.AlignCenter)
        self.label_219.setObjectName("label_219")
        self.verticalLayout_8.addWidget(self.label_219)
        self.comboBox_15 = QtWidgets.QComboBox(self.frame_87)
        self.comboBox_15.setMinimumSize(QtCore.QSize(200, 50))
        self.comboBox_15.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox_15.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_15.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}"
        )
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox_15)
        self.gridLayout_34.addWidget(self.frame_87, 0, 0, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_37.setMinimumSize(QtCore.QSize(60, 50))
        self.pushButton_37.setMaximumSize(QtCore.QSize(120, 50))
        self.pushButton_37.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_34.addWidget(self.pushButton_37, 0, 3, 1, 1)
        self.pushButton_92 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_92.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_92.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_92.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_92.setText("")
        self.pushButton_92.setIcon(icon2)
        self.pushButton_92.setObjectName("pushButton_92")
        self.gridLayout_34.addWidget(self.pushButton_92, 0, 4, 1, 1)
        self.gridLayout_40.addWidget(self.frame_13, 0, 0, 1, 1)
        self.frame_114 = QtWidgets.QFrame(self.frame_90)
        self.frame_114.setMinimumSize(QtCore.QSize(400, 68))
        self.frame_114.setMaximumSize(QtCore.QSize(400, 68))
        self.frame_114.setStyleSheet(
            "\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;"
        )
        self.frame_114.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_114.setObjectName("frame_114")
        self.gridLayout_91 = QtWidgets.QGridLayout(self.frame_114)
        self.gridLayout_91.setObjectName("gridLayout_91")
        self.label_63 = QtWidgets.QLabel(self.frame_114)
        self.label_63.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.gridLayout_91.addWidget(self.label_63, 0, 0, 1, 1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.frame_114)
        self.doubleSpinBox_10.setMinimumSize(QtCore.QSize(250, 50))
        self.doubleSpinBox_10.setMaximumSize(QtCore.QSize(400, 50))
        self.doubleSpinBox_10.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_10.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_10.setMaximum(100000.0)
        self.doubleSpinBox_10.setSingleStep(0.5)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout_91.addWidget(self.doubleSpinBox_10, 0, 1, 1, 1)
        self.gridLayout_40.addWidget(self.frame_114, 2, 0, 1, 1)
        self.tableWidget_846 = QtWidgets.QTableWidget(self.frame_90)
        self.tableWidget_846.setMinimumSize(QtCore.QSize(0, 100))
        self.tableWidget_846.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 13pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_846.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_846.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows
        )
        self.tableWidget_846.setShowGrid(False)
        self.tableWidget_846.setObjectName("tableWidget_846")
        self.tableWidget_846.setColumnCount(5)
        self.tableWidget_846.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_846.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_846.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_846.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_846.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_846.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_846.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_846.setHorizontalHeaderItem(4, item)
        self.tableWidget_846.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_846.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget_846.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_846.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_846.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_846.verticalHeader().setVisible(False)
        self.tableWidget_846.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_846.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_846.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_40.addWidget(self.tableWidget_846, 1, 0, 1, 1)
        self.gridLayout_23.addWidget(self.frame_90, 0, 0, 1, 1)
        self.tabWidget_8.addTab(self.tab_32, "")
        self.gridLayout_22.addWidget(self.tabWidget_8, 0, 0, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.frame_34)
        self.pushButton_33.setMinimumSize(QtCore.QSize(120, 50))
        self.pushButton_33.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_33.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_22.addWidget(self.pushButton_33, 1, 0, 1, 1)
        self.gridLayout_44.addWidget(self.frame_34, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_15, "")
        self.gridLayout_43.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_108 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_108.setObjectName("gridLayout_108")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_11)
        self.scrollArea_5.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border: none;\n"
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #1e1d23;\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 5px;\n"
            "      border: none;\n"
            "      border-bottom: 1px solid #ccc;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: #ffffff;\n"
            "    background-color: #1e1d23;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            ""
        )
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1038, 614))
        self.scrollAreaWidgetContents_5.setStyleSheet(
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }"
        )
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_110 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_110.setObjectName("gridLayout_110")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gridLayout_110.addLayout(self.verticalLayout_12, 3, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_37.setMinimumSize(QtCore.QSize(0, 30))
        self.label_37.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_37.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(245, 245, 245);\n"
            "border-style: solid;\n"
            "border-radius:0px;"
        )
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_110.addWidget(self.label_37, 2, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_34.setMinimumSize(QtCore.QSize(0, 30))
        self.label_34.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_34.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: rgb(0, 0, 0);\n"
            "background-color: rgb(245, 245, 245);\n"
            "border-style: solid;\n"
            "border-radius:0px;"
        )
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_110.addWidget(self.label_34, 0, 0, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout_110.addLayout(self.verticalLayout_11, 1, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_108.addWidget(self.scrollArea_5, 2, 0, 1, 1)
        self.frame_117 = QtWidgets.QFrame(self.tab_11)
        self.frame_117.setMinimumSize(QtCore.QSize(260, 60))
        self.frame_117.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_117.setStyleSheet(
            "QFrame{\n"
            'font: 9pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "background-color: #003a5d;\n"
            "border-width: 0x;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            ""
        )
        self.frame_117.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_117.setObjectName("frame_117")
        self.gridLayout_107 = QtWidgets.QGridLayout(self.frame_117)
        self.gridLayout_107.setObjectName("gridLayout_107")
        self.label_305 = QtWidgets.QLabel(self.frame_117)
        self.label_305.setMinimumSize(QtCore.QSize(62, 0))
        self.label_305.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_305.setAlignment(QtCore.Qt.AlignCenter)
        self.label_305.setObjectName("label_305")
        self.gridLayout_107.addWidget(self.label_305, 0, 5, 3, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            1, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_107.addItem(spacerItem5, 1, 1, 1, 1)
        self.label_307 = QtWidgets.QLabel(self.frame_117)
        self.label_307.setMinimumSize(QtCore.QSize(45, 0))
        self.label_307.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_307.setAlignment(QtCore.Qt.AlignCenter)
        self.label_307.setObjectName("label_307")
        self.gridLayout_107.addWidget(self.label_307, 0, 9, 3, 1)
        self.label_308 = QtWidgets.QLabel(self.frame_117)
        self.label_308.setMinimumSize(QtCore.QSize(45, 0))
        self.label_308.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_308.setAlignment(QtCore.Qt.AlignCenter)
        self.label_308.setObjectName("label_308")
        self.gridLayout_107.addWidget(self.label_308, 0, 3, 3, 1)
        self.label_309 = QtWidgets.QLabel(self.frame_117)
        self.label_309.setMinimumSize(QtCore.QSize(125, 0))
        self.label_309.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_309.setAlignment(QtCore.Qt.AlignCenter)
        self.label_309.setObjectName("label_309")
        self.gridLayout_107.addWidget(self.label_309, 0, 2, 3, 1)
        self.label_78 = QtWidgets.QLabel(self.frame_117)
        self.label_78.setMinimumSize(QtCore.QSize(60, 0))
        self.label_78.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_78.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_78.setText("")
        self.label_78.setAlignment(QtCore.Qt.AlignCenter)
        self.label_78.setObjectName("label_78")
        self.gridLayout_107.addWidget(self.label_78, 0, 6, 3, 1)
        self.label_310 = QtWidgets.QLabel(self.frame_117)
        self.label_310.setMinimumSize(QtCore.QSize(50, 0))
        self.label_310.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_310.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_310.setText("")
        self.label_310.setAlignment(QtCore.Qt.AlignCenter)
        self.label_310.setObjectName("label_310")
        self.gridLayout_107.addWidget(self.label_310, 0, 4, 3, 1)
        self.label_311 = QtWidgets.QLabel(self.frame_117)
        self.label_311.setMinimumSize(QtCore.QSize(100, 0))
        self.label_311.setStyleSheet(
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.label_311.setAlignment(QtCore.Qt.AlignCenter)
        self.label_311.setObjectName("label_311")
        self.gridLayout_107.addWidget(self.label_311, 0, 8, 3, 1)
        self.gridLayout_108.addWidget(self.frame_117, 1, 0, 1, 1)
        self.pushButton_94 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_94.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_94.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_94.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_94.setText("")
        self.pushButton_94.setIcon(icon2)
        self.pushButton_94.setObjectName("pushButton_94")
        self.gridLayout_108.addWidget(self.pushButton_94, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_52 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_52.setSpacing(0)
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_12)
        self.tabWidget_5.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget_5.setStyleSheet(
            "\n"
            "/*-----QTabWidget-----*/\n"
            "QTabBar::tab\n"
            "{\n"
            '    font: 11pt "Arabic Transparent Bold";\n'
            "    background-color: #262626;\n"
            "    color: rgb(27, 28, 30);\n"
            "    border-style: solid;\n"
            "    border-width: 0px;\n"
            "    border-top-left-radius: 3px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-color: #051a39;\n"
            "    width: 100px;\n"
            "    height: 30px;\n"
            "}\n"
            "QTabBar::tab:selected\n"
            "{\n"
            "    background-color: #003a5d;\n"
            "    color: #ffffff;\n"
            "    border-style: solid;\n"
            "    border-width: 0px;\n"
            "    border-top-left-radius: 3px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-color: #051a39;\n"
            "    width: 100px;\n"
            "    height: 30px;\n"
            "}\n"
            "QTabBar::tab:!selected \n"
            "{\n"
            "    background-color: #DFECFF;\n"
            "}\n"
            ""
        )
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.gridLayout_53 = QtWidgets.QGridLayout(self.tab_20)
        self.gridLayout_53.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_53.setSpacing(25)
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.frame_38 = QtWidgets.QFrame(self.tab_20)
        self.frame_38.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_38.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}"
        )
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.gridLayout_60 = QtWidgets.QGridLayout(self.frame_38)
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_38)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_2.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_36.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_36.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_36.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout.addWidget(self.pushButton_36, 2, 1, 1, 1)
        self.pushButton_75 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_75.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_75.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_75.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_75.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-view-stream.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_75.setIcon(icon4)
        self.pushButton_75.setObjectName("pushButton_75")
        self.gridLayout.addWidget(self.pushButton_75, 2, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_16.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_16.setMaxLength(9999999)
        self.lineEdit_16.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 0, 1, 1, 1)
        self.pushButton_76 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_76.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_76.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_76.setStyleSheet("")
        self.pushButton_76.setText("")
        self.pushButton_76.setObjectName("pushButton_76")
        self.gridLayout.addWidget(self.pushButton_76, 2, 0, 1, 1)
        self.gridLayout_60.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame_38)
        self.groupBox.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            "\n"
            ""
        )
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_12.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_12.setMaxLength(9999999)
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_41.addWidget(self.lineEdit_12, 0, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_13.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_13.setMaxLength(9999999)
        self.lineEdit_13.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_41.addWidget(self.lineEdit_13, 1, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_14.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_14.setMaxLength(9999999)
        self.lineEdit_14.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_41.addWidget(self.lineEdit_14, 2, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_15.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_15.setMaxLength(9999999)
        self.lineEdit_15.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_41.addWidget(self.lineEdit_15, 3, 0, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_22.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_22.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_22.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_22.setMaxLength(9999999)
        self.lineEdit_22.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_41.addWidget(self.lineEdit_22, 4, 0, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_38.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_38.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_38.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_41.addWidget(self.pushButton_38, 5, 0, 1, 1)
        self.gridLayout_60.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_38)
        self.groupBox_3.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_59 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_21.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_21.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_21.setMaxLength(9999999)
        self.lineEdit_21.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_59.addWidget(self.lineEdit_21, 4, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_17.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_17.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_17.setMaxLength(9999999)
        self.lineEdit_17.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_59.addWidget(self.lineEdit_17, 0, 0, 1, 1)
        self.pushButton_45 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_45.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_45.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_45.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_45.setObjectName("pushButton_45")
        self.gridLayout_59.addWidget(self.pushButton_45, 5, 0, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_19.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_19.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_19.setMaxLength(9999999)
        self.lineEdit_19.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_59.addWidget(self.lineEdit_19, 2, 0, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_20.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_20.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_20.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_20.setMaxLength(9999999)
        self.lineEdit_20.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_59.addWidget(self.lineEdit_20, 3, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_18.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_18.setMaxLength(9999999)
        self.lineEdit_18.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_59.addWidget(self.lineEdit_18, 1, 0, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_40.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_40.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_40.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout_59.addWidget(self.pushButton_40, 6, 0, 1, 1)
        self.gridLayout_60.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.gridLayout_53.addWidget(self.frame_38, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_20, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.gridLayout_54 = QtWidgets.QGridLayout(self.tab_21)
        self.gridLayout_54.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_54.setSpacing(25)
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.frame_39 = QtWidgets.QFrame(self.tab_21)
        self.frame_39.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_39.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}"
        )
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.gridLayout_68 = QtWidgets.QGridLayout(self.frame_39)
        self.gridLayout_68.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_68.setSpacing(0)
        self.gridLayout_68.setObjectName("gridLayout_68")
        self.frame_42 = QtWidgets.QFrame(self.frame_39)
        self.frame_42.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_42.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}"
        )
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.gridLayout_61 = QtWidgets.QGridLayout(self.frame_42)
        self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_61.setSpacing(15)
        self.gridLayout_61.setObjectName("gridLayout_61")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_42)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_4.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_62 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_62.setObjectName("gridLayout_62")
        self.pushButton_77 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_77.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_77.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_77.setStyleSheet("")
        self.pushButton_77.setText("")
        self.pushButton_77.setObjectName("pushButton_77")
        self.gridLayout_62.addWidget(self.pushButton_77, 2, 0, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_39.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_39.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_39.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_62.addWidget(self.pushButton_39, 2, 1, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_23.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_23.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_23.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_23.setMaxLength(9999999)
        self.lineEdit_23.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_62.addWidget(self.lineEdit_23, 0, 1, 1, 1)
        self.pushButton_78 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_78.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_78.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_78.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_78.setText("")
        self.pushButton_78.setIcon(icon4)
        self.pushButton_78.setObjectName("pushButton_78")
        self.gridLayout_62.addWidget(self.pushButton_78, 2, 2, 1, 1)
        self.gridLayout_61.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_42)
        self.groupBox_5.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            "\n"
            ""
        )
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_65 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_65.setObjectName("gridLayout_65")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_26.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_26.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_26.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_26.setMaxLength(9999999)
        self.lineEdit_26.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_65.addWidget(self.lineEdit_26, 0, 0, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_27.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_27.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_27.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_27.setMaxLength(9999999)
        self.lineEdit_27.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_27.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_65.addWidget(self.lineEdit_27, 1, 0, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_11.setMinimumSize(QtCore.QSize(250, 50))
        self.comboBox_11.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_11.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox_11.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_11.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}"
        )
        self.comboBox_11.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.comboBox_11.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_11.setFrame(True)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.gridLayout_65.addWidget(self.comboBox_11, 2, 0, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_41.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_41.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_41.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout_65.addWidget(self.pushButton_41, 3, 0, 1, 1)
        self.gridLayout_61.addWidget(self.groupBox_5, 0, 0, 2, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_42)
        self.groupBox_6.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_67 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_67.setObjectName("gridLayout_67")
        self.pushButton_43 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_43.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_43.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_43.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout_67.addWidget(self.pushButton_43, 4, 0, 1, 1)
        self.pushButton_44 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_44.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_44.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_44.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_44.setObjectName("pushButton_44")
        self.gridLayout_67.addWidget(self.pushButton_44, 3, 0, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_29.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_29.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_29.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_29.setMaxLength(9999999)
        self.lineEdit_29.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_29.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_67.addWidget(self.lineEdit_29, 0, 0, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_33.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_33.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_33.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_33.setMaxLength(9999999)
        self.lineEdit_33.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_67.addWidget(self.lineEdit_33, 1, 0, 1, 1)
        self.comboBox_13 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_13.setMinimumSize(QtCore.QSize(250, 50))
        self.comboBox_13.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_13.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox_13.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_13.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}"
        )
        self.comboBox_13.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.comboBox_13.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_13.setFrame(True)
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.gridLayout_67.addWidget(self.comboBox_13, 2, 0, 1, 1)
        self.gridLayout_61.addWidget(self.groupBox_6, 1, 1, 1, 1)
        self.gridLayout_68.addWidget(self.frame_42, 0, 0, 1, 1)
        self.gridLayout_54.addWidget(self.frame_39, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_21, "")
        self.gridLayout_52.addWidget(self.tabWidget_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_69 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_69.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_69.setSpacing(0)
        self.gridLayout_69.setObjectName("gridLayout_69")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_10)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_7.setStyleSheet(
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_70 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_70.setObjectName("gridLayout_70")
        self.pushButton_46 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_46.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_46.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_46.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_46.setObjectName("pushButton_46")
        self.gridLayout_70.addWidget(self.pushButton_46, 2, 0, 1, 1)
        self.comboBox_19 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_19.setMinimumSize(QtCore.QSize(250, 50))
        self.comboBox_19.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_19.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_19.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}"
        )
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.gridLayout_70.addWidget(self.comboBox_19, 0, 0, 1, 1)
        self.frame_32 = QtWidgets.QFrame(self.groupBox_7)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.gridLayout_166 = QtWidgets.QGridLayout(self.frame_32)
        self.gridLayout_166.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_166.setSpacing(0)
        self.gridLayout_166.setObjectName("gridLayout_166")
        self.pushButton_71 = QtWidgets.QPushButton(self.frame_32)
        self.pushButton_71.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_71.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_71.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_71.setText("")
        self.pushButton_71.setIcon(icon2)
        self.pushButton_71.setObjectName("pushButton_71")
        self.gridLayout_166.addWidget(self.pushButton_71, 0, 0, 1, 1)
        self.gridLayout_70.addWidget(self.frame_32, 3, 0, 1, 1)
        self.gridLayout_69.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.frame_43 = QtWidgets.QFrame(self.tab_10)
        self.frame_43.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_43.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}"
        )
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.gridLayout_71 = QtWidgets.QGridLayout(self.frame_43)
        self.gridLayout_71.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_71.setObjectName("gridLayout_71")
        self.tableWidget_19 = QtWidgets.QTableWidget(self.frame_43)
        self.tableWidget_19.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_19.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 13pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_19.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_19.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_19.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget_19.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_19.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_19.setShowGrid(False)
        self.tableWidget_19.setObjectName("tableWidget_19")
        self.tableWidget_19.setColumnCount(6)
        self.tableWidget_19.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(5, item)
        self.tableWidget_19.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_19.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget_19.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_19.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_19.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_19.verticalHeader().setVisible(False)
        self.tableWidget_19.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_19.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_19.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_71.addWidget(self.tableWidget_19, 1, 0, 1, 1)
        self.gridLayout_69.addWidget(self.frame_43, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.gridLayout_57 = QtWidgets.QGridLayout(self.tab_22)
        self.gridLayout_57.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_57.setSpacing(0)
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.frame_40 = QtWidgets.QFrame(self.tab_22)
        self.frame_40.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_40.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}"
        )
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.gridLayout_66 = QtWidgets.QGridLayout(self.frame_40)
        self.gridLayout_66.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_66.setSpacing(15)
        self.gridLayout_66.setObjectName("gridLayout_66")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame_40)
        self.groupBox_8.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_8.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_28.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_28.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_28.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_28.setMaxLength(9999999)
        self.lineEdit_28.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_28.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_35.addWidget(self.lineEdit_28, 0, 1, 1, 1)
        self.pushButton_42 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_42.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_42.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_42.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_42.setObjectName("pushButton_42")
        self.gridLayout_35.addWidget(self.pushButton_42, 1, 1, 1, 1)
        self.pushButton_74 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_74.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_74.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_74.setStyleSheet("")
        self.pushButton_74.setText("")
        self.pushButton_74.setObjectName("pushButton_74")
        self.gridLayout_35.addWidget(self.pushButton_74, 1, 0, 1, 1)
        self.pushButton_73 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_73.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_73.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_73.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_73.setText("")
        self.pushButton_73.setIcon(icon4)
        self.pushButton_73.setObjectName("pushButton_73")
        self.gridLayout_35.addWidget(self.pushButton_73, 1, 2, 1, 1)
        self.gridLayout_66.addWidget(self.groupBox_8, 0, 1, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.frame_40)
        self.groupBox_9.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            "\n"
            ""
        )
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_56 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_30.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_30.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_30.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_30.setMaxLength(9999999)
        self.lineEdit_30.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_30.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_56.addWidget(self.lineEdit_30, 0, 0, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_31.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_31.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_31.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_31.setMaxLength(9999999)
        self.lineEdit_31.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_56.addWidget(self.lineEdit_31, 1, 0, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_32.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_32.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_32.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_32.setMaxLength(9999999)
        self.lineEdit_32.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_56.addWidget(self.lineEdit_32, 2, 0, 1, 1)
        self.pushButton_54 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_54.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_54.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_54.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_54.setObjectName("pushButton_54")
        self.gridLayout_56.addWidget(self.pushButton_54, 3, 0, 1, 1)
        self.gridLayout_66.addWidget(self.groupBox_9, 0, 0, 2, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.frame_40)
        self.groupBox_10.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_102 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_102.setObjectName("gridLayout_102")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_40.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_40.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_40.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_40.setMaxLength(9999999)
        self.lineEdit_40.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_40.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.gridLayout_102.addWidget(self.lineEdit_40, 1, 0, 1, 1)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_38.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_38.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_38.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_38.setMaxLength(9999999)
        self.lineEdit_38.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_38.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout_102.addWidget(self.lineEdit_38, 2, 0, 1, 1)
        self.pushButton_56 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_56.setMinimumSize(QtCore.QSize(250, 40))
        self.pushButton_56.setMaximumSize(QtCore.QSize(400, 40))
        self.pushButton_56.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_56.setObjectName("pushButton_56")
        self.gridLayout_102.addWidget(self.pushButton_56, 4, 0, 1, 1)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_37.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_37.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_37.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_37.setMaxLength(9999999)
        self.lineEdit_37.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_37.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout_102.addWidget(self.lineEdit_37, 0, 0, 1, 1)
        self.pushButton_55 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_55.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_55.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_55.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_55.setObjectName("pushButton_55")
        self.gridLayout_102.addWidget(self.pushButton_55, 3, 0, 1, 1)
        self.gridLayout_66.addWidget(self.groupBox_10, 1, 1, 1, 1)
        self.gridLayout_57.addWidget(self.frame_40, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_22, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_16)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_113 = QtWidgets.QFrame(self.tab_16)
        self.frame_113.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_113.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}"
        )
        self.frame_113.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_113.setObjectName("frame_113")
        self.gridLayout_153 = QtWidgets.QGridLayout(self.frame_113)
        self.gridLayout_153.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_153.setSpacing(15)
        self.gridLayout_153.setObjectName("gridLayout_153")
        self.groupBox_11 = QtWidgets.QGroupBox(self.frame_113)
        self.groupBox_11.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_11.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_55 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.pushButton_51 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_51.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_51.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_51.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_51.setObjectName("pushButton_51")
        self.gridLayout_55.addWidget(self.pushButton_51, 2, 1, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_35.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_35.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_35.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_35.setMaxLength(9999999)
        self.lineEdit_35.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_35.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_55.addWidget(self.lineEdit_35, 0, 1, 1, 1)
        self.pushButton_79 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_79.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_79.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_79.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_79.setText("")
        self.pushButton_79.setIcon(icon4)
        self.pushButton_79.setObjectName("pushButton_79")
        self.gridLayout_55.addWidget(self.pushButton_79, 2, 2, 1, 1)
        self.pushButton_80 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_80.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_80.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_80.setStyleSheet("")
        self.pushButton_80.setText("")
        self.pushButton_80.setObjectName("pushButton_80")
        self.gridLayout_55.addWidget(self.pushButton_80, 2, 0, 1, 1)
        self.gridLayout_153.addWidget(self.groupBox_11, 0, 1, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.frame_113)
        self.groupBox_12.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            "\n"
            ""
        )
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_154 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_154.setObjectName("gridLayout_154")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_41.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_41.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_41.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_41.setMaxLength(9999999)
        self.lineEdit_41.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_41.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.gridLayout_154.addWidget(self.lineEdit_41, 0, 0, 1, 1)
        self.pushButton_60 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_60.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_60.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_60.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_60.setObjectName("pushButton_60")
        self.gridLayout_154.addWidget(self.pushButton_60, 2, 0, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox_12)
        self.doubleSpinBox_5.setMinimumSize(QtCore.QSize(250, 50))
        self.doubleSpinBox_5.setMaximumSize(QtCore.QSize(400, 50))
        self.doubleSpinBox_5.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_5.setMaximum(100000.0)
        self.doubleSpinBox_5.setSingleStep(0.5)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_154.addWidget(self.doubleSpinBox_5, 1, 0, 1, 1)
        self.gridLayout_153.addWidget(self.groupBox_12, 0, 0, 2, 1)
        self.groupBox_13 = QtWidgets.QGroupBox(self.frame_113)
        self.groupBox_13.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_156 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_156.setObjectName("gridLayout_156")
        self.pushButton_62 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_62.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_62.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_62.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_62.setObjectName("pushButton_62")
        self.gridLayout_156.addWidget(self.pushButton_62, 2, 0, 1, 1)
        self.pushButton_61 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_61.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_61.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_61.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_61.setObjectName("pushButton_61")
        self.gridLayout_156.addWidget(self.pushButton_61, 3, 0, 1, 1)
        self.lineEdit_46 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_46.setEnabled(True)
        self.lineEdit_46.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_46.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_46.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_46.setMaxLength(9999999)
        self.lineEdit_46.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_46.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.gridLayout_156.addWidget(self.lineEdit_46, 0, 0, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_6.setMinimumSize(QtCore.QSize(250, 50))
        self.doubleSpinBox_6.setMaximumSize(QtCore.QSize(400, 50))
        self.doubleSpinBox_6.setStyleSheet(
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color: rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;"
        )
        self.doubleSpinBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_6.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_6.setMaximum(100000.0)
        self.doubleSpinBox_6.setSingleStep(0.5)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout_156.addWidget(self.doubleSpinBox_6, 1, 0, 1, 1)
        self.gridLayout_153.addWidget(self.groupBox_13, 1, 1, 1, 1)
        self.gridLayout_10.addWidget(self.frame_113, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_16, "")
        self.tab_33 = QtWidgets.QWidget()
        self.tab_33.setObjectName("tab_33")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tab_33)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.frame_115 = QtWidgets.QFrame(self.tab_33)
        self.frame_115.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_115.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}"
        )
        self.frame_115.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_115.setObjectName("frame_115")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_115)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.groupBox_15 = QtWidgets.QGroupBox(self.frame_115)
        self.groupBox_15.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            "\n"
            ""
        )
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_159 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_159.setObjectName("gridLayout_159")
        self.pushButton_63 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_63.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_63.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_63.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_63.setObjectName("pushButton_63")
        self.gridLayout_159.addWidget(self.pushButton_63, 2, 0, 1, 1)
        self.lineEdit_43 = QtWidgets.QLineEdit(self.groupBox_15)
        self.lineEdit_43.setMinimumSize(QtCore.QSize(250, 50))
        self.lineEdit_43.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_43.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    background-color: rgb(245, 245, 245);\n"
            "    selection-background-color: rgb(245, 245, 245);\n"
            "    selection-color: 1e1d23;\n"
            "    padding: 5px;\n"
            "    border-style: solid;\n"
            "    border: 2px solid rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    color: #1e1d23;\n"
            "}"
        )
        self.lineEdit_43.setMaxLength(9999999)
        self.lineEdit_43.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_43.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.gridLayout_159.addWidget(self.lineEdit_43, 0, 0, 1, 1)
        self.verticalLayout_13.addWidget(self.groupBox_15)
        self.groupBox_16 = QtWidgets.QGroupBox(self.frame_115)
        self.groupBox_16.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_16.setStyleSheet(
            "    border-radius: 10px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "\n"
            ""
        )
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_160 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_160.setObjectName("gridLayout_160")
        self.comboBox_18 = QtWidgets.QComboBox(self.groupBox_16)
        self.comboBox_18.setMinimumSize(QtCore.QSize(250, 50))
        self.comboBox_18.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_18.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_18.setStyleSheet(
            "QComboBox{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #1e1d23;\n"
            "    background-color:  rgb(245, 245, 245);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid  rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox:hover{\n"
            "    color: rgb(245, 245, 245);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    color: #1e1d23;\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    border-right-width: 2px;\n"
            "    border-left-color: #1e1d23;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:images/icons/fi-rs-angle-small-down.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "    color: #1e1d23;    \n"
            "    background-color:#ffffff;\n"
            "    padding: 10px;\n"
            "    selection-background-color: #00a94f;\n"
            "}\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }"
        )
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.gridLayout_160.addWidget(self.comboBox_18, 0, 0, 1, 1)
        self.pushButton_65 = QtWidgets.QPushButton(self.groupBox_16)
        self.pushButton_65.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton_65.setMaximumSize(QtCore.QSize(400, 50))
        self.pushButton_65.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #00a94f;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #B2B6C3;\n"
            "    background-color: #454B59;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.pushButton_65.setObjectName("pushButton_65")
        self.gridLayout_160.addWidget(self.pushButton_65, 1, 0, 1, 1)
        self.verticalLayout_13.addWidget(self.groupBox_16)
        self.gridLayout_26.addWidget(self.frame_115, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_33, "")
        self.tab_37 = QtWidgets.QWidget()
        self.tab_37.setObjectName("tab_37")
        self.gridLayout_63 = QtWidgets.QGridLayout(self.tab_37)
        self.gridLayout_63.setObjectName("gridLayout_63")
        self.frame_104 = QtWidgets.QFrame(self.tab_37)
        self.frame_104.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_104.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: 0px solid #1e1d23;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #f5f3f4;\n"
            "}"
        )
        self.frame_104.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_104.setObjectName("frame_104")
        self.gridLayout_111 = QtWidgets.QGridLayout(self.frame_104)
        self.gridLayout_111.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_111.setObjectName("gridLayout_111")
        self.tableWidget_22 = QtWidgets.QTableWidget(self.frame_104)
        self.tableWidget_22.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_22.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_22.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_22.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_22.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_22.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_22.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_22.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_22.setShowGrid(False)
        self.tableWidget_22.setObjectName("tableWidget_22")
        self.tableWidget_22.setColumnCount(6)
        self.tableWidget_22.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(5, item)
        self.tableWidget_22.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_22.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_22.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_22.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_22.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_22.verticalHeader().setVisible(False)
        self.tableWidget_22.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_22.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_22.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout_111.addWidget(self.tableWidget_22, 0, 0, 1, 1)
        self.gridLayout_63.addWidget(self.frame_104, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_37, "")
        self.tab_38 = QtWidgets.QWidget()
        self.tab_38.setObjectName("tab_38")
        self.gridLayout_143 = QtWidgets.QGridLayout(self.tab_38)
        self.gridLayout_143.setObjectName("gridLayout_143")
        self.tableWidget_28 = QtWidgets.QTableWidget(self.tab_38)
        self.tableWidget_28.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_28.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_28.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_28.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_28.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_28.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_28.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_28.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_28.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_28.setShowGrid(False)
        self.tableWidget_28.setObjectName("tableWidget_28")
        self.tableWidget_28.setColumnCount(4)
        self.tableWidget_28.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_28.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_28.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(3, item)
        self.tableWidget_28.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_28.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidget_28.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_28.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_28.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_28.verticalHeader().setVisible(False)
        self.tableWidget_28.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_28.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_28.verticalHeader().setMinimumSectionSize(50)
        self.gridLayout_143.addWidget(self.tableWidget_28, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_38, "")
        self.tab_40 = QtWidgets.QWidget()
        self.tab_40.setObjectName("tab_40")
        self.gridLayout_149 = QtWidgets.QGridLayout(self.tab_40)
        self.gridLayout_149.setObjectName("gridLayout_149")
        self.tableWidget_29 = QtWidgets.QTableWidget(self.tab_40)
        self.tableWidget_29.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_29.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_29.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_29.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_29.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_29.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_29.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_29.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_29.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_29.setShowGrid(False)
        self.tableWidget_29.setObjectName("tableWidget_29")
        self.tableWidget_29.setColumnCount(4)
        self.tableWidget_29.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_29.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_29.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(3, item)
        self.tableWidget_29.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_29.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidget_29.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_29.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_29.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_29.verticalHeader().setVisible(False)
        self.tableWidget_29.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_29.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_29.verticalHeader().setMinimumSectionSize(50)
        self.gridLayout_149.addWidget(self.tableWidget_29, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_40, "")
        self.tab_39 = QtWidgets.QWidget()
        self.tab_39.setObjectName("tab_39")
        self.gridLayout_151 = QtWidgets.QGridLayout(self.tab_39)
        self.gridLayout_151.setObjectName("gridLayout_151")
        self.tableWidget_30 = QtWidgets.QTableWidget(self.tab_39)
        self.tableWidget_30.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_30.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget_30.setStyleSheet(
            "QFrame{\n"
            "    border-radius: 0px;\n"
            "    border: none;\n"
            '    font: 10pt "Arabic Transparent";\n'
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableCornerButton::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border: none;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "}\n"
            "QTableView {\n"
            "    color: #1e1d23;\n"
            "    background-color: #ffffff;\n"
            "    border:none;\n"
            "}\n"
            "QHeaderView::section {\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border:none;\n"
            "    padding: 4px;\n"
            "    border: none;\n"
            '    font: 12pt "Arabic Transparent";\n'
            "      border-bottom: 1px solid #003a5d;\n"
            "    border-top: 1px solid #003a5d;\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "\n"
            "}\n"
            "QTableView::item {\n"
            "    color: #1e1d23;\n"
            "     padding: 10px;\n"
            "      border: 0px solid #ccc;\n"
            "    border-bottom: 1px solid;\n"
            "    border-bottom-color: rgb(204, 204, 204);\n"
            "    border-radius: 0px;\n"
            "    background-color: #ffffff;\n"
            "}\n"
            "\n"
            "QTableWidget::item:selected{\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: #f5f5f5;\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QPushButton {\n"
            '    font: 10pt "Arabic Transparent Bold";    \n'
            "    background-color: #ec0f04;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "        \n"
            "    background-color: rgb(214, 89, 31);\n"
            "}\n"
            ""
        )
        self.tableWidget_30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_30.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_30.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.tableWidget_30.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_30.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_30.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_30.setShowGrid(False)
        self.tableWidget_30.setObjectName("tableWidget_30")
        self.tableWidget_30.setColumnCount(3)
        self.tableWidget_30.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_30.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_30.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(2, item)
        self.tableWidget_30.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_30.horizontalHeader().setDefaultSectionSize(600)
        self.tableWidget_30.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_30.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_30.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_30.verticalHeader().setVisible(False)
        self.tableWidget_30.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_30.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_30.verticalHeader().setMinimumSectionSize(50)
        self.gridLayout_151.addWidget(self.tableWidget_30, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_39, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_58.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setStyleSheet(
            "QFrame{\n"
            "\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;\n"
            "}\n"
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            ""
        )
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_6.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_6.setStyleSheet("")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 239, 878))
        self.scrollAreaWidgetContents_6.setStyleSheet(
            "\n"
            "/* SCROLL BARS */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    height: 14px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: #ffffff;\n"
            "    min-width: 25px;\n"
            "    border-radius: 7px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: #ffffff;\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background:#d9d9d9;\n"
            "    min-height: 25px;\n"
            "    border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;    background: #ffffff;\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            ""
        )
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_112 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_112.setObjectName("gridLayout_112")
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_10.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_10.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-cursor-move.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_112.addWidget(self.pushButton_10, 8, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_5.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_5.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-browser.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_112.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_7.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_7.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-move.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_112.addWidget(self.pushButton_7, 11, 0, 1, 1)
        self.frame_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_16.setMinimumSize(QtCore.QSize(215, 165))
        self.frame_16.setMaximumSize(QtCore.QSize(215, 165))
        self.frame_16.setStyleSheet("")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_79 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_79.setContentsMargins(0, 0, 0, 15)
        self.gridLayout_79.setObjectName("gridLayout_79")
        self.label = QtWidgets.QLabel(self.frame_16)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 150))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/icons/TTE_BIG.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_79.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_112.addWidget(self.frame_16, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_4.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_112.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_11.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_11.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-wrap-text.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_11.setIcon(icon8)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_112.addWidget(self.pushButton_11, 9, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_6.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-user.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_6.setIcon(icon9)
        self.pushButton_6.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_112.addWidget(self.pushButton_6, 6, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_112.addItem(spacerItem6, 12, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setTabletTracking(False)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-chart.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton.setIcon(icon10)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoRepeatDelay(300)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_112.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_3.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-fire.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_3.setIcon(icon11)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_112.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_2.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-calendar-check.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_2.setIcon(icon12)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_112.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_32.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_32.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(":/images/icons/cil-people.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_32.setIcon(icon13)
        self.pushButton_32.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_112.addWidget(self.pushButton_32, 10, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_8.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_8.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    text-align: left;\n"
            '    font: 12pt "Arabic Transparent Bold";\n'
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding: 12px;\n"
            "    border-radius: 10px;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QPushButton:disabled\n"
            "{\n"
            "    background-color: #1B1C1E;\n"
            "    border-width: 0px;\n"
            "    border-style: solid;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    padding-left: 12px;\n"
            "    padding-right: 12px;\n"
            "    border-radius: 10px;\n"
            "    color: #757778;\n"
            "}\n"
            "\n"
            "QPushButton:focus {\n"
            "    background-color: #ffffff;\n"
            "    color: rgb(27, 28, 30);\n"
            "}\n"
            "\n"
            ".QPushButton:hover{\n"
            "    color: rgb(27, 28, 30);\n"
            "    background-color: #ffffff;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    color: #ffffff;\n"
            "    background-color: #003a5d;\n"
            "    padding-top: 12px;\n"
            "    padding-bottom: 12px;\n"
            "    border-radius: 10px;\n"
            "}\n"
            ""
        )
        self.pushButton_8.setIcon(icon12)
        self.pushButton_8.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_112.addWidget(self.pushButton_8, 7, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_2.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.gridLayout_58.addWidget(self.frame, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(1)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Total system"))
        self.msg.setText(_translate("MainWindow", "."))
        self.pushButton_14.setText(_translate("MainWindow", "نظره عامه"))
        self.label_7.setText(_translate("MainWindow", "بنزين 80"))
        self.pushButton_53.setText(_translate("MainWindow", "حفظ"))
        self.label_6.setText(_translate("MainWindow", "سولار"))
        self.label_9.setText(_translate("MainWindow", "بنزين 95"))
        self.label_8.setText(_translate("MainWindow", "بنزين 92"))
        item = self.tableWidget_20.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_20.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_20.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_20.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_20.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "التاريخ"))
        item = self.tableWidget_20.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الوقت"))
        item = self.tableWidget_20.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "النوع"))
        item = self.tableWidget_20.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "اسم المستخدم"))
        self.label_69.setText(_translate("MainWindow", "سولار"))
        self.label_68.setText(_translate("MainWindow", "0"))
        self.label_71.setText(_translate("MainWindow", "0"))
        self.label_70.setText(_translate("MainWindow", "بنزين 80"))
        self.label_73.setText(_translate("MainWindow", "0"))
        self.label_72.setText(_translate("MainWindow", "بنزين 92"))
        self.label_74.setText(_translate("MainWindow", "بنزين 95"))
        self.label_75.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1")
        )
        self.label_176.setText(_translate("MainWindow", "البدايه"))
        self.label_177.setText(_translate("MainWindow", "رقم الطلمبه"))
        self.label_181.setText(_translate("MainWindow", "النهايه"))
        self.label_178.setText(_translate("MainWindow", "النوع"))
        self.label_39.setText(_translate("MainWindow", "الاجمالي"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2")
        )
        self.label_13.setText(_translate("MainWindow", "رصيد النهايه"))
        self.pushButton_16.setText(_translate("MainWindow", "حفظ"))
        self.label_14.setText(_translate("MainWindow", "رصيد البدايه"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "New Item"))
        self.label_35.setText(_translate("MainWindow", "اختر نوع الزيت"))
        self.label_40.setText(_translate("MainWindow", "وارد مخزن"))
        self.pushButton_19.setText(_translate("MainWindow", "اضافه / حذف"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "نوع الزيت"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "رصيد البدايه"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "رصيد النهايه"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "وارد مخزن"))
        self.tabWidget_4.setTabText(
            self.tabWidget_4.indexOf(self.tab_18),
            _translate("MainWindow", "   المخزن   "),
        )
        self.label_36.setText(_translate("MainWindow", "اختر نوع الزيت"))
        self.pushButton_23.setText(_translate("MainWindow", "حفظ"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "New Item"))
        self.label_30.setText(_translate("MainWindow", "رصيد اول المده"))
        self.label_43.setText(_translate("MainWindow", "مباع"))
        self.label_16.setText(_translate("MainWindow", "رصيد اخر المده"))
        item = self.tableWidget_9.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_9.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "نوع الزيت"))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "رصيد اول المده"))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "رصيد اخر المده"))
        item = self.tableWidget_9.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "مباع"))
        item = self.tableWidget_9.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "سعر"))
        item = self.tableWidget_9.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "الاجمالي"))
        self.pushButton_58.setText(_translate("MainWindow", "اضافه / حذف"))
        self.tabWidget_4.setTabText(
            self.tabWidget_4.indexOf(self.tab_19),
            _translate("MainWindow", "   الورديه   "),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page")
        )
        self.pushButton_18.setText(_translate("MainWindow", "حفظ"))
        self.label_17.setText(_translate("MainWindow", "ادخل المبلغ"))
        self.label_15.setText(_translate("MainWindow", "السند"))
        self.tableWidget_5.setSortingEnabled(False)
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "المبلغ"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "السند"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page")
        )
        self.label_21.setText(_translate("MainWindow", "سولار"))
        item = self.tableWidget_6.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_6.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "السعر"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الفئه"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "الاجمالي"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "سريال البون"))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "الجهة"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "شرطه"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "جمعية"))
        self.label_20.setText(_translate("MainWindow", "الجهة"))
        self.pushButton_22.setText(_translate("MainWindow", "حفظ"))
        self.label_18.setText(_translate("MainWindow", "ادخل الفئة"))
        self.label_19.setText(_translate("MainWindow", "ادخل سريال البون"))
        self.label_12.setText(_translate("MainWindow", "اختر نوع البنزين"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "سولار"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "بنزين 80"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "بنزين 92"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "بنزين 95"))
        self.tabWidget_6.setTabText(
            self.tabWidget_6.indexOf(self.tab_23), _translate("MainWindow", "البونات")
        )
        self.label_41.setText(_translate("MainWindow", "الاجمالي"))
        item = self.tableWidget_21.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "العدد"))
        item = self.tableWidget_21.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الفئه"))
        item = self.tableWidget_21.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الاجمالي"))
        self.tabWidget_7.setTabText(
            self.tabWidget_7.indexOf(self.tab_26), _translate("MainWindow", "سولار")
        )
        item = self.tableWidget_23.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "العدد"))
        item = self.tableWidget_23.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الفئه"))
        item = self.tableWidget_23.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الاجمالي"))
        self.label_44.setText(_translate("MainWindow", "الاجمالي"))
        self.tabWidget_7.setTabText(
            self.tabWidget_7.indexOf(self.tab_27), _translate("MainWindow", "بنزين 80")
        )
        item = self.tableWidget_24.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "العدد"))
        item = self.tableWidget_24.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الفئه"))
        item = self.tableWidget_24.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الاجمالي"))
        self.label_45.setText(_translate("MainWindow", "الاجمالي"))
        self.tabWidget_7.setTabText(
            self.tabWidget_7.indexOf(self.tab_28), _translate("MainWindow", "بنزين 92")
        )
        item = self.tableWidget_25.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "العدد"))
        item = self.tableWidget_25.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الفئه"))
        item = self.tableWidget_25.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الاجمالي"))
        self.label_46.setText(_translate("MainWindow", "الاجمالي"))
        self.tabWidget_7.setTabText(
            self.tabWidget_7.indexOf(self.tab_29), _translate("MainWindow", "بنزين 95")
        )
        self.label_47.setText(_translate("MainWindow", "الاجمالي"))
        item = self.tableWidget_26.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "العدد"))
        item = self.tableWidget_26.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الفئه"))
        item = self.tableWidget_26.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الاجمالي"))
        self.tabWidget_7.setTabText(
            self.tabWidget_7.indexOf(self.tab_30), _translate("MainWindow", "شرطه")
        )
        item = self.tableWidget_27.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "العدد"))
        item = self.tableWidget_27.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الفئه"))
        item = self.tableWidget_27.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الاجمالي"))
        self.label_48.setText(_translate("MainWindow", "الاجمالي"))
        self.tabWidget_7.setTabText(
            self.tabWidget_7.indexOf(self.tab_31), _translate("MainWindow", "جمعيه")
        )
        self.tabWidget_6.setTabText(
            self.tabWidget_6.indexOf(self.tab_25),
            _translate("MainWindow", "مطابقه البونات"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page")
        )
        self.label_22.setText(_translate("MainWindow", "العميل"))
        self.label_23.setText(_translate("MainWindow", "ادخل المبلغ"))
        self.comboBox_17.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox_17.setItemText(1, _translate("MainWindow", "New Item"))
        self.label_25.setText(_translate("MainWindow", "سند"))
        self.pushButton_29.setText(_translate("MainWindow", "حفظ"))
        item = self.tableWidget_7.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "العميل"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "المبلغ"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "السند"))
        self.label_24.setText(_translate("MainWindow", "الاجمالي"))
        self.pushButton_30.setText(_translate("MainWindow", "اضافه / حذف"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page")
        )
        self.label_183.setText(_translate("MainWindow", "الكميه"))
        self.label_179.setText(_translate("MainWindow", "السعر"))
        self.label_180.setText(_translate("MainWindow", "البيان"))
        self.label_182.setText(_translate("MainWindow", "المبلغ"))
        self.label_185.setText(_translate("MainWindow", "0"))
        self.label_184.setText(_translate("MainWindow", "0"))
        self.label_186.setText(_translate("MainWindow", "0"))
        self.label_187.setText(_translate("MainWindow", "سولار"))
        self.label_244.setText(_translate("MainWindow", "0"))
        self.label_245.setText(_translate("MainWindow", "بنزين 80"))
        self.label_246.setText(_translate("MainWindow", "0"))
        self.label_247.setText(_translate("MainWindow", "0"))
        self.label_248.setText(_translate("MainWindow", "0"))
        self.label_249.setText(_translate("MainWindow", "بنزين 92"))
        self.label_250.setText(_translate("MainWindow", "0"))
        self.label_251.setText(_translate("MainWindow", "0"))
        self.label_252.setText(_translate("MainWindow", "0"))
        self.label_253.setText(_translate("MainWindow", "بنزين 95"))
        self.label_254.setText(_translate("MainWindow", "0"))
        self.label_255.setText(_translate("MainWindow", "0"))
        self.label_292.setText(_translate("MainWindow", "0"))
        self.label_293.setText(_translate("MainWindow", "زيوت"))
        self.label_294.setText(_translate("MainWindow", "0"))
        self.label_295.setText(_translate("MainWindow", "-"))
        self.label_288.setText(_translate("MainWindow", "0"))
        self.label_289.setText(_translate("MainWindow", "الاجمالي"))
        self.label_290.setText(_translate("MainWindow", "-"))
        self.label_291.setText(_translate("MainWindow", "-"))
        self.label_284.setText(_translate("MainWindow", "0"))
        self.label_285.setText(_translate("MainWindow", "بونات"))
        self.label_286.setText(_translate("MainWindow", "0"))
        self.label_287.setText(_translate("MainWindow", "-"))
        self.label_280.setText(_translate("MainWindow", "0"))
        self.label_281.setText(_translate("MainWindow", "عملاء اجله"))
        self.label_282.setText(_translate("MainWindow", "0"))
        self.label_283.setText(_translate("MainWindow", "-"))
        self.label_256.setText(_translate("MainWindow", "0"))
        self.label_259.setText(_translate("MainWindow", "-"))
        self.label_257.setText(_translate("MainWindow", "المصاريف"))
        self.label_258.setText(_translate("MainWindow", "0"))
        self.label_276.setText(_translate("MainWindow", "0"))
        self.label_277.setText(_translate("MainWindow", "الاجمالي"))
        self.label_278.setText(_translate("MainWindow", "-"))
        self.label_279.setText(_translate("MainWindow", "-"))
        self.label_272.setText(_translate("MainWindow", "0"))
        self.label_273.setText(_translate("MainWindow", "الصافي"))
        self.label_274.setText(_translate("MainWindow", "-"))
        self.label_275.setText(_translate("MainWindow", "-"))
        self.label_261.setText(_translate("MainWindow", "صافي النقديه"))
        self.label_262.setText(_translate("MainWindow", "-"))
        self.label_260.setText(_translate("MainWindow", "0"))
        self.label_263.setText(_translate("MainWindow", "-"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Page")
        )
        self.label_217.setText(_translate("MainWindow", "السند"))
        self.label_218.setText(_translate("MainWindow", "المبلغ"))
        self.pushButton_35.setText(_translate("MainWindow", "حفظ"))
        self.label_216.setText(_translate("MainWindow", "البيان"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(4, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(5, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(6, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(7, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(8, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(9, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(10, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(11, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(12, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(13, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(14, _translate("MainWindow", "New Item"))
        self.comboBox_12.setItemText(15, _translate("MainWindow", "New Item"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "البيان"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "السند"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "المبلغ"))
        self.label_62.setText(_translate("MainWindow", "الاجمالي"))
        self.tabWidget_8.setTabText(
            self.tabWidget_8.indexOf(self.tab_24), _translate("MainWindow", "مقبوضات")
        )
        self.label_221.setText(_translate("MainWindow", "المبلغ"))
        self.label_220.setText(_translate("MainWindow", "السند"))
        self.label_219.setText(_translate("MainWindow", "البيان"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox_15.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox_15.setItemText(4, _translate("MainWindow", "New Item"))
        self.comboBox_15.setItemText(5, _translate("MainWindow", "New Item"))
        self.pushButton_37.setText(_translate("MainWindow", "حفظ"))
        self.label_63.setText(_translate("MainWindow", "الاجمالي"))
        item = self.tableWidget_846.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_846.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_846.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_846.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "البيان"))
        item = self.tableWidget_846.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "السند"))
        item = self.tableWidget_846.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "المبلغ"))
        self.tabWidget_8.setTabText(
            self.tabWidget_8.indexOf(self.tab_32), _translate("MainWindow", "مدفوعات")
        )
        self.pushButton_33.setText(_translate("MainWindow", "اضافه / حذف"))
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_15),
            _translate("MainWindow", "حركة الخزينة"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Page")
        )
        self.label_37.setText(_translate("MainWindow", "الي مذكورين"))
        self.label_34.setText(_translate("MainWindow", "من مذكورين"))
        self.label_305.setText(_translate("MainWindow", "البيان"))
        self.label_307.setText(_translate("MainWindow", "فرق السعر"))
        self.label_308.setText(_translate("MainWindow", "دائن"))
        self.label_309.setText(_translate("MainWindow", "مدين"))
        self.label_311.setText(_translate("MainWindow", "نقل"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "Page")
        )
        self.groupBox_2.setTitle(_translate("MainWindow", "بحث"))
        self.pushButton_36.setText(_translate("MainWindow", "بحث"))
        self.lineEdit_16.setPlaceholderText(_translate("MainWindow", "ادخل الاسم"))
        self.groupBox.setTitle(_translate("MainWindow", "اضافه"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "ادخل الاسم"))
        self.lineEdit_13.setPlaceholderText(
            _translate("MainWindow", "ادخل الرقم القومي")
        )
        self.lineEdit_14.setPlaceholderText(_translate("MainWindow", "ادخل رقم الهاتف"))
        self.lineEdit_15.setPlaceholderText(_translate("MainWindow", "ادخل الوظيفه"))
        self.lineEdit_22.setPlaceholderText(_translate("MainWindow", "ادخل المرتب"))
        self.pushButton_38.setText(_translate("MainWindow", "حفظ"))
        self.groupBox_3.setTitle(_translate("MainWindow", "تعديل"))
        self.lineEdit_21.setPlaceholderText(_translate("MainWindow", "المرتب"))
        self.lineEdit_17.setPlaceholderText(_translate("MainWindow", "الاسم"))
        self.pushButton_45.setText(_translate("MainWindow", "حفظ"))
        self.lineEdit_19.setPlaceholderText(_translate("MainWindow", "رقم الهاتف"))
        self.lineEdit_20.setPlaceholderText(_translate("MainWindow", "الوظيفه"))
        self.lineEdit_18.setPlaceholderText(_translate("MainWindow", "الرقم القومي"))
        self.pushButton_40.setText(_translate("MainWindow", "حذف"))
        self.tabWidget_5.setTabText(
            self.tabWidget_5.indexOf(self.tab_20), _translate("MainWindow", "العمال")
        )
        self.groupBox_4.setTitle(_translate("MainWindow", "بحث"))
        self.pushButton_39.setText(_translate("MainWindow", "بحث"))
        self.lineEdit_23.setPlaceholderText(
            _translate("MainWindow", "ادخل اسم المستخدم")
        )
        self.groupBox_5.setTitle(_translate("MainWindow", "اضافه"))
        self.lineEdit_26.setPlaceholderText(
            _translate("MainWindow", "ادخل اسم المستخدم")
        )
        self.lineEdit_27.setPlaceholderText(_translate("MainWindow", "ادخل كلمه السري"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "ادمن"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "محاسب"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "عامل"))
        self.pushButton_41.setText(_translate("MainWindow", "حفظ"))
        self.groupBox_6.setTitle(_translate("MainWindow", "تعديل"))
        self.pushButton_43.setText(_translate("MainWindow", "حذف"))
        self.pushButton_44.setText(_translate("MainWindow", "حفظ"))
        self.lineEdit_29.setPlaceholderText(_translate("MainWindow", "اسم المستخدم"))
        self.lineEdit_33.setPlaceholderText(_translate("MainWindow", "كلمه السري"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "ادمن"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "محاسب"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "عامل"))
        self.tabWidget_5.setTabText(
            self.tabWidget_5.indexOf(self.tab_21),
            _translate("MainWindow", "المستخدمين"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "Page")
        )
        self.pushButton_46.setText(_translate("MainWindow", "بحث"))
        self.comboBox_19.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox_19.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox_19.setItemText(2, _translate("MainWindow", "New Item"))
        item = self.tableWidget_19.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_19.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_19.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "في تاريخ"))
        item = self.tableWidget_19.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "الوقت"))
        item = self.tableWidget_19.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "اسم المستخدم"))
        item = self.tableWidget_19.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "النوع"))
        item = self.tableWidget_19.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_19.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "الحركه"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Page")
        )
        self.groupBox_8.setTitle(_translate("MainWindow", "بحث"))
        self.lineEdit_28.setPlaceholderText(_translate("MainWindow", "ادخل الاسم"))
        self.pushButton_42.setText(_translate("MainWindow", "بحث"))
        self.groupBox_9.setTitle(_translate("MainWindow", "اضافه"))
        self.lineEdit_30.setPlaceholderText(_translate("MainWindow", "ادخل الاسم"))
        self.lineEdit_31.setPlaceholderText(
            _translate("MainWindow", "ادخل الرقم القومي")
        )
        self.lineEdit_32.setPlaceholderText(_translate("MainWindow", "ادخل رقم الهاتف"))
        self.pushButton_54.setText(_translate("MainWindow", "حفظ"))
        self.groupBox_10.setTitle(_translate("MainWindow", "تعديل"))
        self.lineEdit_40.setPlaceholderText(_translate("MainWindow", "الرقم القومي"))
        self.lineEdit_38.setPlaceholderText(_translate("MainWindow", "رقم الهاتف"))
        self.pushButton_56.setText(_translate("MainWindow", "حذف"))
        self.lineEdit_37.setPlaceholderText(_translate("MainWindow", "الاسم"))
        self.pushButton_55.setText(_translate("MainWindow", "حفظ"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_22), _translate("MainWindow", "Page")
        )
        self.groupBox_11.setTitle(_translate("MainWindow", "بحث"))
        self.pushButton_51.setText(_translate("MainWindow", "بحث"))
        self.lineEdit_35.setPlaceholderText(_translate("MainWindow", "ادخل الاسم"))
        self.groupBox_12.setTitle(_translate("MainWindow", "اضافه"))
        self.lineEdit_41.setPlaceholderText(_translate("MainWindow", "ادخل الاسم"))
        self.pushButton_60.setText(_translate("MainWindow", "حفظ"))
        self.groupBox_13.setTitle(_translate("MainWindow", "تعديل"))
        self.pushButton_62.setText(_translate("MainWindow", "حفظ"))
        self.pushButton_61.setText(_translate("MainWindow", "حذف"))
        self.lineEdit_46.setPlaceholderText(_translate("MainWindow", "الاسم"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_16), _translate("MainWindow", "Page")
        )
        self.groupBox_15.setTitle(_translate("MainWindow", "اضافه"))
        self.pushButton_63.setText(_translate("MainWindow", "حفظ"))
        self.lineEdit_43.setPlaceholderText(_translate("MainWindow", "ادخل البيان"))
        self.groupBox_16.setTitle(_translate("MainWindow", "تعديل"))
        self.comboBox_18.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox_18.setItemText(1, _translate("MainWindow", "New Item"))
        self.pushButton_65.setText(_translate("MainWindow", "حذف"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_33), _translate("MainWindow", "Page")
        )
        item = self.tableWidget_22.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_22.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_22.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_22.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_22.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_22.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_22.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_22.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_37), _translate("MainWindow", "Page")
        )
        item = self.tableWidget_28.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_28.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_28.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_28.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_28.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_28.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_38), _translate("MainWindow", "Page")
        )
        item = self.tableWidget_29.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_29.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_29.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_29.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_29.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_29.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_40), _translate("MainWindow", "Page")
        )
        item = self.tableWidget_30.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_30.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_30.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_30.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_30.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_39), _translate("MainWindow", "Page")
        )
        self.pushButton_10.setText(_translate("MainWindow", "        حركة الخزينة"))
        self.pushButton_5.setText(_translate("MainWindow", "        البونات"))
        self.pushButton_7.setText(_translate("MainWindow", "        حركه النظام"))
        self.pushButton_4.setText(_translate("MainWindow", "        المصاريف"))
        self.pushButton_11.setText(_translate("MainWindow", "        قيد يومي"))
        self.pushButton_6.setText(_translate("MainWindow", "        عملاء آجله"))
        self.pushButton.setText(_translate("MainWindow", "        نظره عامه"))
        self.pushButton_3.setText(_translate("MainWindow", "        الزيوت"))
        self.pushButton_2.setText(_translate("MainWindow", "        يومية الورديه"))
        self.pushButton_32.setText(_translate("MainWindow", "        الموظفين"))
        self.pushButton_8.setText(_translate("MainWindow", "        يومية الخزينه"))

