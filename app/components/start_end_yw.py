from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *

import resources


class Start_End_YW(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName("Form")
        Form.resize(655, 135)
        Form.setMinimumSize(QSize(655, 135))
        Form.setMaximumSize(QSize(760, 135))
        icon = QIcon()
        icon.addFile(":/images/icons/newl.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(Qt.RightToLeft)
        Form.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(Form)
        self.frame_14.setObjectName("frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 130))
        self.frame_14.setStyleSheet(
            "QFrame{\n"
            "	border-radius: 15px;\n"
            "	border: none;\n"
            '	font: 10pt "Arabic Transparent";\n'
            "	color: #1e1d23;\n"
            "	background-color: #ffffff;\n"
            "}"
        )
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_14)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName("label_17")
        self.label_17.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_17, 0, 2, 1, 1)

        self.spinBox = QSpinBox(self.frame_14)
        self.spinBox.setObjectName("spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QSize(250, 50))
        self.spinBox.setMaximumSize(QSize(250, 50))
        self.spinBox.setStyleSheet(
            '	font: 12pt "Arabic Transparent Bold";\n'
            "	color: #1e1d23;\n"
            "	background-color: rgb(245, 245, 245);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(245, 245, 245);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;"
        )
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(999999999)

        self.gridLayout_2.addWidget(self.spinBox, 2, 2, 1, 1)

        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName("label_15")
        self.label_15.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n' "color: #1e1d23;\n" ""
        )
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 0, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.frame_14)
        self.spinBox_2.setObjectName("spinBox_2")
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimumSize(QSize(250, 50))
        self.spinBox_2.setMaximumSize(QSize(250, 50))
        self.spinBox_2.setStyleSheet(
            '	font: 12pt "Arabic Transparent Bold";\n'
            "	color: #1e1d23;\n"
            "	background-color: rgb(245, 245, 245);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(245, 245, 245);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;"
        )
        self.spinBox_2.setAlignment(Qt.AlignCenter)
        self.spinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_2.setMaximum(999999999)

        self.gridLayout_2.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.save_s_e = QPushButton(self.frame_14)
        self.save_s_e.setObjectName("save_s_e")
        self.save_s_e.setMinimumSize(QSize(60, 50))
        self.save_s_e.setMaximumSize(QSize(75, 50))
        self.save_s_e.setStyleSheet(
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

        self.gridLayout_2.addWidget(self.save_s_e, 2, 3, 1, 1)

        self.gridLayout.addWidget(self.frame_14, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate(
                "Form",
                "\u062a\u0639\u062f\u064a\u0644 \u0627\u0644\u0628\u062f\u0627\u064a\u0647 \u0648 \u0627\u0644\u0646\u0647\u0627\u064a\u0647",
                None,
            )
        )
        self.label_17.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u0646\u0647\u0627\u064a\u0647", None
            )
        )
        self.label_15.setText(
            QCoreApplication.translate(
                "Form", "\u0627\u0644\u0628\u062f\u0627\u064a\u0647", None
            )
        )
        self.save_s_e.setText(
            QCoreApplication.translate("Form", "\u062d\u0641\u0638", None)
        )

    # retranslateUi
