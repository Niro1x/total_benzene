from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *

import resources


class Login(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        icon = QIcon()
        icon.addFile(":/images/icons/newl.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "QLabel{\n"
            '	font: 12pt "Arabic Transparent Bold";\n'
            "}\n"
            "\n"
            "QPushButton\n"
            "{\n"
            '	font: 12pt "Arabic Transparent Bold";\n'
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
            "}\n"
            ""
        )
        MainWindow.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "background-color: #003a5d;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QSize(500, 500))
        self.frame.setMaximumSize(QSize(500, 500))
        self.frame.setStyleSheet("\n" "background-color: #fffef7;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 50)
        self.passw = QLineEdit(self.frame)
        self.passw.setObjectName("passw")
        self.passw.setMinimumSize(QSize(250, 50))
        self.passw.setMaximumSize(QSize(400, 16777215))
        self.passw.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '	font: 12pt "Arabic Transparent Bold";\n'
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
        self.passw.setMaxLength(9999999)
        self.passw.setEchoMode(QLineEdit.Password)
        self.passw.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.passw, 3, 1, 1, 1)

        self.username = QLineEdit(self.frame)
        self.username.setObjectName("username")
        self.username.setMinimumSize(QSize(250, 50))
        self.username.setMaximumSize(QSize(400, 16777215))
        self.username.setStyleSheet(
            "QLineEdit\n"
            "{\n"
            '	font: 12pt "Arabic Transparent Bold";\n'
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
        self.username.setMaxLength(9999999)
        self.username.setEchoMode(QLineEdit.Normal)
        self.username.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.username, 2, 1, 1, 1)

        self.login_btn = QPushButton(self.frame)
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setMinimumSize(QSize(250, 50))
        self.login_btn.setMaximumSize(QSize(400, 50))
        self.login_btn.setStyleSheet(
            "QPushButton\n"
            "{\n"
            '	font: 12pt "Arabic Transparent Bold";\n'
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

        self.gridLayout_2.addWidget(self.login_btn, 4, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMinimumSize(QSize(0, 200))
        self.frame_2.setMaximumSize(QSize(16777215, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(":/images/icons/TTE_BIG.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(0)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setStyleSheet(
            "QLabel{\n"
            'font: 20pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "}"
        )
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                "\u062a\u0633\u062c\u064a\u0644 \u0627\u0644\u062f\u062e\u0648\u0644",
                None,
            )
        )
        self.passw.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0627\u062f\u062e\u0644 \u0643\u0644\u0645\u0647 \u0627\u0644\u0645\u0631\u0648\u0631",
                None,
            )
        )
        self.username.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0627\u062f\u062e\u0644 \u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645",
                None,
            )
        )
        self.login_btn.setText(
            QCoreApplication.translate("MainWindow", "\u062f\u062e\u0648\u0644", None)
        )
        # if QT_CONFIG(shortcut)
        self.login_btn.setShortcut(
            QCoreApplication.translate("MainWindow", "Return", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.label.setText("")
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0645\u062d\u0637\u0629 \u062a\u0648\u062a\u0627\u0644 \u0627\u0644\u0646\u062f\u064a",
                None,
            )
        )

    # retranslateUi
