from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *

import resources

from start_end_yw import Start_End_YW as start_end_yw


class Frame:
    def YW_frame(self, obj_n, id, N_T, type, start, end, total):
        self.frame = QFrame()
        self.frame.setObjectName(f"frame_yw_{obj_n}")
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setMinimumSize(QSize(260, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(
            "QFrame{\n"
            'font: 9pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "background-color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 5px;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            'font: 11pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            'font: 10pt "Arabic Transparent Bold";\n'
            "background-color: #00a94f;\n"
            "border: none;\n"
            "border-radius: 5px;\n"
            "}"
            "\n"
            "QPushButton:pressed{\n"
            "background-color: rgb(0, 170, 255);\n"
            "}"
        )

        self.frame.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(f"gridLayout_yw_{obj_n}")

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(f"pushButton_yw_id={id}")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(35, 35))
        self.pushButton.setMaximumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(":/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.clicked.connect(lambda: self.button_clicked_yw())

        self.gridLayout.addWidget(self.pushButton, 1, 6, 2, 1)

        self.total_le = QLabel(self.frame)
        self.total_le.setObjectName(f"total_yw_le_{obj_n}")
        self.total_le.setText(f"{str(total)}")
        self.total_le.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.total_le, 1, 5, 2, 1)

        self.end_yw_le = QLabel(self.frame)
        self.end_yw_le.setObjectName(f"end_yw_le_{obj_n}")
        self.end_yw_le.setText(f"{str(end)}")
        self.end_yw_le.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.end_yw_le, 1, 4, 2, 1)

        self.start_yw_le = QLabel(self.frame)
        self.start_yw_le.setObjectName(f"start_yw_le_{obj_n}")
        self.start_yw_le.setText(f"{str(start)}")
        self.start_yw_le.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.start_yw_le, 1, 3, 2, 1)

        self.T_Number = QLabel(self.frame)
        self.T_Number.setObjectName(f"T_Number_yw_{obj_n}")
        self.T_Number.setText(f"{str(N_T)}")
        self.T_Number.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_Number, 1, 1, 2, 1)

        self.T_type = QLabel(self.frame)
        self.T_type.setObjectName(f"T_type_yw_{obj_n}")
        self.T_type.setText(f"{str(type)}")
        self.T_type.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_type, 1, 2, 2, 1)

        # self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        return self.frame

    def button_clicked_yw(self):
        global window2
        global row_id
        obj_name = self.pushButton.objectName()
        row_id = int(obj_name[17:])
        window2 = Start_End_YW()
        window2.get_benzen_prices()
        window2.show()

    def daftr_tmwen_fram(self, obj_n, Date, Start, Ward, Monsrf, End, M3yar):
        self.frame = QFrame()
        self.frame.setObjectName(f"frame_daftrt_{obj_n}")
        self.frame.setGeometry(QRect(100, 170, 1106, 62))
        self.frame.setMinimumSize(QSize(260, 62))
        self.frame.setMaximumSize(QSize(16777215, 62))
        self.frame.setStyleSheet(
            "QFrame{\n"
            'font: 9pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "background-color: #ffffff;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 15px;\n"
            "}"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_63 = QGridLayout(self.frame)
        self.gridLayout_63.setObjectName(f"gridLayout_daftrt_{obj_n}")

        self.ward = QLabel(self.frame)
        self.ward.setObjectName("ward_daftrt_{obj_n}")
        self.ward.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.ward.setAlignment(Qt.AlignCenter)
        self.ward.setText(str(Ward))

        self.gridLayout_63.addWidget(self.ward, 0, 6, 3, 1)

        self.start = QLabel(self.frame)
        self.start.setObjectName(f"start_daftrt_{obj_n}")
        self.start.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.start.setAlignment(Qt.AlignCenter)
        self.start.setText(str(Start))

        self.gridLayout_63.addWidget(self.start, 0, 4, 3, 1)

        self.m3yar = QLabel(self.frame)
        self.m3yar.setObjectName(f"m3yar_daftrt_{obj_n}")
        self.m3yar.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.m3yar.setAlignment(Qt.AlignCenter)
        self.m3yar.setText(str(M3yar))

        self.gridLayout_63.addWidget(self.m3yar, 0, 14, 3, 1)

        self.monsrf = QLabel(self.frame)
        self.monsrf.setObjectName(f"monsrf_daftrt_{obj_n}")
        self.monsrf.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.monsrf.setAlignment(Qt.AlignCenter)
        self.monsrf.setText(str(Monsrf))

        self.gridLayout_63.addWidget(self.monsrf, 0, 8, 3, 1)

        self.date = QLabel(self.frame)
        self.date.setObjectName(f"date_daftrt_{obj_n}")
        self.date.setMinimumSize(QSize(125, 0))
        self.date.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.date.setAlignment(Qt.AlignCenter)
        self.date.setText(str(Date))

        self.gridLayout_63.addWidget(self.date, 0, 2, 3, 1)

        self.end = QLabel(self.frame)
        self.end.setObjectName(f"end_daftrt_{obj_n}")
        self.end.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #1e1d23;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 0px;"
        )
        self.end.setAlignment(Qt.AlignCenter)
        self.end.setText(str(End))

        self.gridLayout_63.addWidget(self.end, 0, 12, 3, 1)

        self.tlomba = QPushButton(self.frame)
        self.tlomba.setObjectName(f"tlomba_daftrt_{Date}")
        self.tlomba.setEnabled(True)
        self.tlomba.setMinimumSize(QSize(50, 50))
        self.tlomba.setMaximumSize(QSize(50, 50))
        self.tlomba.clicked.connect(lambda: self.show_tlombat())
        self.tlomba.setStyleSheet(
            "background-color: #00a94f;\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            "border-radius: 20px;"
        )
        icon = QIcon()
        icon.addFile(":/images/icons/cil-door.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tlomba.setIcon(icon)

        self.gridLayout_63.addWidget(self.tlomba, 0, 10, 3, 1)
        return self.frame

    def show_tlombat(self):
        obj_name = self.tlomba.objectName()
        date = obj_name[14:]
        benz_type = str(window.comboBox_9.currentText())
        tlomba_windw.show_data(date, benz_type)
        tlomba_windw.show()

    def main_frame_kad(self, date, n, s, t, data):
        self.gridLayout_main = QGridLayout()
        self.gridLayout_main.setObjectName(f"gridLayout_main_kad_{n}")
        self.frame = QFrame()
        self.frame.setObjectName(f"frame_116_main_kad_{n}")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(
            "	border-radius: 5px;\n"
            "	border: 1;\n"
            '	font: 11pt "Arabic Transparent";\n'
            "background-color: rgb(255, 255, 255);"
        )
        self.frame.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(f"gridLayout_main_kad_{n}")
        self.mden = QLabel(self.frame)
        self.mden.setObjectName(f"mden_main_kad_{n}")
        self.mden.setMinimumSize(QSize(150, 0))
        self.mden.setStyleSheet(
            '	font: 12pt "Arabic Transparent Bold";\n'
            "	color: #1e1d23;\n"
            "	background-color: rgb(245, 245, 245);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(245, 245, 245);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;"
        )
        self.mden.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mden, 0, 0, 1, 1)

        self.da2n = QLabel(self.frame)
        self.da2n.setObjectName(f"da2n_main_kad_{n}")
        self.da2n.setMinimumSize(QSize(150, 0))
        self.da2n.setStyleSheet(
            '	font: 12pt "Arabic Transparent Bold";\n'
            "	color: #1e1d23;\n"
            "	background-color: rgb(245, 245, 245);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(245, 245, 245);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;"
        )
        self.da2n.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.da2n, 0, 1, 1, 1)

        self.label_297 = QLabel(self.frame)
        self.label_297.setObjectName(f"label_297_main_kad_{n}")
        self.label_297.setMinimumSize(QSize(400, 0))
        self.label_297.setMaximumSize(QSize(16777215, 16777215))
        self.label_297.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 1px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: rgb(0, 0, 0);"
        )
        self.label_297.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_297, 0, 2, 1, 1)

        self.na2l = QSpinBox(self.frame)
        self.na2l.setObjectName(f"na2l_main_kad_{n}")
        self.na2l.setMinimumSize(QSize(45, 0))
        self.na2l.setStyleSheet(
            '	font: 12pt "Arabic Transparent Bold";\n'
            "	color: #1e1d23;\n"
            "	background-color: rgb(245, 245, 245);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(245, 245, 245);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;"
        )
        self.na2l.setAlignment(Qt.AlignCenter)
        self.na2l.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.na2l.setMaximum(999999999)

        self.gridLayout.addWidget(self.na2l, 0, 3, 1, 1)

        self.fr2s3r = QSpinBox(self.frame)
        self.fr2s3r.setObjectName(f"fr2s3r_main_kad_{n}")
        self.fr2s3r.setMinimumSize(QSize(45, 0))
        self.fr2s3r.setStyleSheet(
            '	font: 12pt "Arabic Transparent Bold";\n'
            "	color: #1e1d23;\n"
            "	background-color: rgb(245, 245, 245);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(245, 245, 245);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;"
        )
        self.fr2s3r.setAlignment(Qt.AlignCenter)
        self.fr2s3r.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.fr2s3r.setMaximum(999999999)

        self.gridLayout.addWidget(self.fr2s3r, 0, 4, 1, 1)

        self.save = QPushButton(self.frame)
        self.save.setObjectName(f"pushButton_34_main_kad_{n}")
        self.save.setMinimumSize(QSize(40, 40))
        self.save.setMaximumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(":/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save.setIcon(icon)
        self.save.setStyleSheet(
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
        v1 = int(self.na2l.value())
        v2 = int(self.fr2s3r.value())
        self.save.clicked.connect(lambda: self.edit_na2l_w_fr2(date, s, t))

        self.gridLayout.addWidget(self.save, 0, 5, 1, 1)

        self.verticalLayout_ = QVBoxLayout()
        self.verticalLayout_.setObjectName(f"verticalLayout__main_kad_{n}")
        self.verticalLayout_.setSizeConstraint(QLayout.SetMinimumSize)

        self.gridLayout.addLayout(self.verticalLayout_, 1, 2, 1, 1)

        self.gridLayout_main.addWidget(self.frame, 0, 0, 1, 1)
        c = 0
        summ = 0
        n = 0
        for d in data:
            sand = d[0]
            money = d[1]
            summ = summ + money
            c = c + money
            n = n + 1
            frame_s_m = comp().sand_and_m_frame_ked(c, str(sand), str(money))
            self.verticalLayout_.addWidget(frame_s_m)
        self.frame.setMinimumSize(QSize(0, int((n * 60) + 100)))
        if t == "مقبوضات":
            self.mden.setText(str(summ))
            self.da2n.setText("0")
        else:
            self.da2n.setText(str(summ))
            self.mden.setText("0")
        self.label_297.setText(s)

        sql = " SELECT na2l,fr2s3r FROM na2l_fr2_ked WHERE date=%s AND Type=%s AND Statement=%s"
        data = (date, t, s)
        mycursor.execute(sql, data)
        res = mycursor.fetchone()
        if res != None:
            self.na2l.setValue(int(res[0]))
            self.fr2s3r.setValue(int(res[1]))

        return self.frame

    def edit_na2l_w_fr2(self, date, s, t):
        v1 = int(self.na2l.value())
        v2 = int(self.fr2s3r.value())
        sql = "UPDATE na2l_fr2_ked SET na2l =%s,fr2s3r=%s WHERE date=%s AND Type=%s AND Statement=%s"
        data = (v1, v2, date, t, s)
        mycursor.execute(sql, data)
        myconn.commit()

    def sand_and_m_frame_ked(self, n, s, m):
        self.frame = QFrame()
        self.frame.setObjectName(f"frame_sand_m_{(n + int(m) * 50 )+15048}")
        self.frame.setGeometry(QRect(0, 100, 400, 60))
        self.frame.setMinimumSize(QSize(400, 60))
        self.frame.setMaximumSize(QSize(400, 60))
        self.frame.setStyleSheet(
            "	border-radius: 10px;\n"
            '	font: 11pt "Arabic Transparent";\n'
            "	background-color: rgb(245, 245, 245);"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_162 = QGridLayout(self.frame)
        self.gridLayout_162.setObjectName(
            f"gridLayout_sand_m_{(n + int(m) * 50 )+15048}"
        )
        self.mbl8 = QLabel(self.frame)
        self.mbl8.setObjectName(f"mbl8_sand_m_{(n + int(m) * 50 )+15048}")
        self.mbl8.setMinimumSize(QSize(45, 0))
        self.mbl8.setStyleSheet(
            'font: 12pt "Arabic Transparent Bold";\n'
            "color: #ffffff;\n"
            "border-width: 1px;\n"
            "border-style: solid;\n"
            "border-radius: 10px;\n"
            "background-color: rgb(0, 0, 0);"
        )
        self.mbl8.setAlignment(Qt.AlignCenter)
        self.mbl8.setText(m)

        self.gridLayout_162.addWidget(self.mbl8, 0, 0, 1, 1)

        self.sand = QLabel(self.frame)
        self.sand.setObjectName(f"sand_sand_m_{(n + int(m) * 50 )+15048}")
        self.sand.setMinimumSize(QSize(150, 0))
        self.sand.setStyleSheet(
            "	border-radius: 15px;\n"
            "	border: 1;\n"
            '	font: 11pt "Arabic Transparent";\n'
            "	color: #1e1d23;\n"
            "	background-color: rgb(245, 245, 245);"
        )
        self.sand.setAlignment(Qt.AlignCenter)
        self.sand.setText(s)

        self.gridLayout_162.addWidget(self.sand, 0, 1, 1, 1)

        return self.frame
