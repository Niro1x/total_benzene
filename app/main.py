from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QApplication, QLabel, QSplashScreen

from components.body import Body as ui
from components.login import Login as login
from components.start_end_yw import Start_End_YW as start_end_yw
import resources

import sys
import os
import datetime
import time
import random

from xlrd import *
from xlsxwriter import *

import mysql.connector


###################################################################################################

current_date = datetime.date.today()
selected_date = current_date
previous_date = selected_date - datetime.timedelta(days=1)
next_date = current_date + datetime.timedelta(days=1)
current_time = datetime.datetime.now().strftime("%H:%M:%S")
current_year, current_month, current_day = str(current_date).split("-")
selected_year, selected_month, selected_day = str(selected_date).split("-")

###################################################################################################

oils_name_list = []
client_name_list = []
emp_list = []
user_list = []
username = ""
usert = ""

###################################################################################################

try:
    myconn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="niro",
        database="tdb",
    )
    mycursor = myconn.cursor(buffered=True)
    print("run")
except:
    print("db error")
    sys.exit()


###################################################################################################
class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Changes()
        self.Handle_buttons()

    def create_waiting_frame(self):
        self.loading_frame = QFrame()
        self.loading_frame.setObjectName("loading_frame")

        geometry = self.geometry()
        self.loading_frame.setGeometry(geometry)

        self.loading_frame.hide()

    def waiting_frame_start(self):
        geometry = self.geometry()
        self.loading_frame.setGeometry(geometry)
        self.loading_frame.show()

    def waiting_frame_end(self):
        self.loading_frame.hide()

    def Message(self, message, redORgreen, sec):
        self.msg.setText(message)
        if redORgreen == True:
            self.notf.setStyleSheet(
                "QFrame{\n" "background-color: rgb(85, 170, 127);\n" "}"
            )
        else:
            self.notf.setStyleSheet(
                "QFrame{\n" "background-color: rgb(255, 44, 17);\n" "}"
            )
        self.notf.show()
        QTimer.singleShot((sec * 1000), self.notf.hide)

    def on_date_changed(self, date):
        global selected_date
        global previous_date
        try:
            self.waiting_frame_start()
            selected_date = date.toString("yyyy-MM-dd")
            previous_date = date.addDays(-1).toString("yyyy-MM-dd")
            self.start()
            current_index = self.tabWidget.currentIndex()
            if current_index == 0:
                self.nzra_ama_clicked()
            elif current_index == 1:
                self.YW_clicked()
            elif current_index == 2:
                self.oils_clicked()
            elif current_index == 3:
                self.masaref_clicked()
            elif current_index == 4:
                self.bons_clicked()
            elif current_index == 5:
                self.omala_clicked()
            elif current_index == 6:
                self.yawmet_al5zena_clicked()
            elif current_index == 8:
                self.Treasury_Movement_clicked()
            elif current_index == 9:
                self.ked_clicked()
            elif current_index == 10:
                self.mwzfen_clicked()
            elif current_index == 11:
                self.System_Move_clicked()
            elif current_index == 12:
                self.add_client_clicked()
            elif current_index == 13:
                self.pushButton_14.setText("الزيوت")
            self.waiting_frame_end()
            self.Message("تم تغير التاريخ بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def UI_Changes(self):
        self.notf.hide()
        self.tabWidget.tabBar().setVisible(False)
        self.create_waiting_frame()
        self.start()
        self.get_total_benzene_consumption()
        self.get_petrolprice()
        self.pushButton_62.setEnabled(False)
        self.pushButton_61.setEnabled(False)
        self.pushButton_55.setEnabled(False)
        self.pushButton_56.setEnabled(False)
        self.pushButton_45.setEnabled(False)
        self.pushButton_40.setEnabled(False)
        self.pushButton_44.setEnabled(False)
        self.pushButton_43.setEnabled(False)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setMaximumDate(QDate.currentDate())
        self.dateEdit.dateChanged.connect(self.on_date_changed)

    def Handle_buttons(self):
        self.pushButton.clicked.connect(self.nzra_ama_clicked)
        self.pushButton_2.clicked.connect(self.YW_clicked)
        self.pushButton_3.clicked.connect(lambda: self.oils_clicked())
        self.pushButton_4.clicked.connect(lambda: self.masaref_clicked())
        self.pushButton_5.clicked.connect(lambda: self.bons_clicked())
        self.pushButton_6.clicked.connect(lambda: self.omala_clicked())
        self.pushButton_8.clicked.connect(lambda: self.yawmet_al5zena_clicked())
        self.pushButton_10.clicked.connect(lambda: self.Treasury_Movement_clicked())
        self.pushButton_11.clicked.connect(self.ked_clicked)
        self.pushButton_32.clicked.connect(lambda: self.mwzfen_clicked())
        self.pushButton_7.clicked.connect(lambda: self.System_Move_clicked())
        self.pushButton_53.clicked.connect(self.update_petrolprice_from_boxes)
        self.pushButton_30.clicked.connect(lambda: self.add_client_clicked())
        self.pushButton_18.clicked.connect(self.add_data_to_msaref)
        self.pushButton_22.clicked.connect(self.add_bons)
        self.pushButton_19.clicked.connect(lambda: self.tabWidget.setCurrentIndex(13))
        self.pushButton_16.clicked.connect(self.add_oil_in_storage)
        self.pushButton_58.clicked.connect(lambda: self.tabWidget.setCurrentIndex(13))
        self.pushButton_60.clicked.connect(self.add_oil)
        self.pushButton_51.clicked.connect(self.search_oil)
        self.pushButton_62.clicked.connect(self.update_oil)
        self.pushButton_61.clicked.connect(self.delete_oil)
        self.pushButton_23.clicked.connect(self.add_oil_in_ward)
        self.pushButton_29.clicked.connect(self.Add_payment_from_client)
        self.pushButton_54.clicked.connect(self.add_client)
        self.pushButton_42.clicked.connect(self.search_client)
        self.pushButton_55.clicked.connect(self.update_client)
        self.pushButton_56.clicked.connect(self.delete_client)
        self.pushButton_46.clicked.connect(self.show_System_Moves_w_user)
        self.pushButton_38.clicked.connect(self.add_emp)
        self.pushButton_36.clicked.connect(self.search_emp)
        self.pushButton_45.clicked.connect(self.update_emp)
        self.pushButton_40.clicked.connect(self.delete_emp)
        self.pushButton_41.clicked.connect(self.add_user)
        self.pushButton_39.clicked.connect(self.search_user)
        self.pushButton_44.clicked.connect(self.update_user)
        self.pushButton_43.clicked.connect(self.delete_user)
        self.pushButton_35.clicked.connect(self.add_mkbodat)
        self.pushButton_37.clicked.connect(self.add_mdfo3at)
        self.pushButton_33.clicked.connect(lambda: self.tabWidget.setCurrentIndex(14))
        self.pushButton_63.clicked.connect(self.add_byan)
        self.pushButton_65.clicked.connect(self.del_byan)
        self.pushButton_75.clicked.connect(lambda: self.show_all_emp_in_table())
        self.pushButton_78.clicked.connect(lambda: self.show_all_user_in_table())
        self.pushButton_73.clicked.connect(lambda: self.show_all_cl_in_table())
        self.pushButton_79.clicked.connect(lambda: self.show_all_oi_in_table())
        self.pushButton_64.clicked.connect(lambda: self.Export_login_h())
        self.pushButton_67.clicked.connect(lambda: self.Export_yw())
        self.pushButton_81.clicked.connect(lambda: self.Export_oils_storage())
        self.pushButton_82.clicked.connect(lambda: self.Export_oils_ward())
        self.pushButton_68.clicked.connect(lambda: self.Export_msaref())
        self.pushButton_69.clicked.connect(lambda: self.Export_bons())
        self.pushButton_83.clicked.connect(lambda: self.Export_solar_matching_bons())
        self.pushButton_84.clicked.connect(lambda: self.Export_p80_matching_bons())
        self.pushButton_87.clicked.connect(lambda: self.Export_p92_matching_bons())
        self.pushButton_88.clicked.connect(lambda: self.Export_p95_matching_bons())
        self.pushButton_89.clicked.connect(lambda: self.Export_police_matching_bons())
        self.pushButton_90.clicked.connect(lambda: self.Export_gm3ya_matching_bons())
        self.pushButton_70.clicked.connect(lambda: self.Export_omala_agla())
        self.pushButton_72.clicked.connect(lambda: self.Export_yawmet_al5zena())
        self.pushButton_91.clicked.connect(lambda: self.Export_mkbodat())
        self.pushButton_92.clicked.connect(lambda: self.Export_mdfo3at())
        self.pushButton_71.clicked.connect(lambda: self.Export_System_Move())
        self.pushButton_94.clicked.connect(lambda: self.Export_ked())
        self.pushButton_13.clicked.connect(
            lambda: self.dateEdit.setDate(QDate.currentDate())
        )
        self.comboBox_6.currentIndexChanged.connect(
            lambda: self.comboBox_in_bons_clicked()
        )
        self.comboBox_15.currentIndexChanged.connect(self.combo_mdfo3at_Changed)
        self.comboBox_12.currentIndexChanged.connect(self.combo_mkbodat_Changed)
        self.comboBox_10.currentIndexChanged.connect(
            lambda: self.get_data_when_compo_change_storage()
        )
        self.comboBox_14.currentIndexChanged.connect(
            lambda: self.get_data_when_compo_change_ward()
        )

    def start(self):
        sql = " SELECT * FROM petrolprice WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        result1 = mycursor.fetchone()
        if result1 == None or result1 == []:
            sql = " SELECT * FROM petrolprice WHERE date=%s "
            data = (previous_date,)
            mycursor.execute(sql, data)
            result = mycursor.fetchone()

            if result == None or result == []:
                sql = "INSERT INTO petrolprice(date,solarprice,petrol80price,petrol92price,petrol95price) VALUES(%s,%s,%s,%s,%s)"
                data = (selected_date, 0, 0, 0, 0)
                mycursor.execute(sql, data)
                myconn.commit()
            else:
                sql = "INSERT INTO petrolprice(date,solarprice,petrol80price,petrol92price,petrol95price) VALUES(%s,%s,%s,%s,%s)"
                data = (
                    selected_date,
                    int(result[1]),
                    int(result[2]),
                    int(result[3]),
                    int(result[4]),
                )
                mycursor.execute(sql, data)
                myconn.commit()

        sql = " SELECT * FROM dailyPumpshift WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        result2 = mycursor.fetchone()
        if result2 == None or result2 == []:
            ##   يوميه الورديه  ##
            n_solar = 6
            n_b80 = 1
            n_b92 = 2
            n_b95 = 2
            # سولار #
            for i in range(1, n_solar + 1):
                sql = "INSERT INTO dailyPumpshift(date,pumpNumber,petrolType,start_code,end_code) VALUES(%s,%s,%s,%s,%s)"
                data = (selected_date, i, "سولار", 0, 0)
                mycursor.execute(sql, data)
                myconn.commit()
            # بنزين 80 #
            for i in range(1, n_b80 + 1):
                sql = "INSERT INTO dailyPumpshift(date,pumpNumber,petrolType,start_code,end_code) VALUES(%s,%s,%s,%s,%s)"
                data = (selected_date, i, "بنزين 80", 0, 0)
                mycursor.execute(sql, data)
                myconn.commit()
            # بنزين 92 #
            for i in range(1, n_b92 + 1):
                sql = "INSERT INTO dailyPumpshift(date,pumpNumber,petrolType,start_code,end_code) VALUES(%s,%s,%s,%s,%s)"
                data = (selected_date, i, "بنزين 92", 0, 0)
                mycursor.execute(sql, data)
                myconn.commit()
            # بنزين 95 #
            for i in range(1, n_b95 + 1):
                sql = "INSERT INTO dailyPumpshift(date,pumpNumber,petrolType,start_code,end_code) VALUES(%s,%s,%s,%s,%s)"
                data = (selected_date, i, "بنزين 95", 0, 0)
                mycursor.execute(sql, data)
                myconn.commit()

        ############الزيوت######
        sql = " SELECT * FROM OilStorage WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        ress = mycursor.fetchall()
        if ress == None or ress == []:
            sql = " SELECT oilName,price FROM oil"
            mycursor.execute(sql)
            oils = mycursor.fetchall()
            for name in oils:
                sql = "INSERT INTO oilshift(date,oilname,StartTermBalance,endTermBalance,sold,price) VALUES(%s,%s,%s,%s,%s,%s)"
                data = (
                    selected_date,
                    str(name[0]),
                    0,
                    0,
                    0,
                    int(name[1]),
                )
                mycursor.execute(sql, data)
                myconn.commit()

                sql = "INSERT INTO OilStorage(date,oilname,beginingBalance,endingBalance,inboundtowarehouse) VALUES(%s,%s,%s,%s,%s)"
                data = (selected_date, str(name[0]), 0, 0, 0)
                mycursor.execute(sql, data)
                myconn.commit()

        """   
        #############القيد نقل و فرق سعر#######
        sql = " SELECT * FROM na2l_fr2_ked WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        rd = mycursor.fetchone()
        if rd == None or rd == []:
            sql = " SELECT name FROM statement"
            mycursor.execute(sql)
            statement_names = mycursor.fetchall()
            for name in statement_names:
                sql = "INSERT INTO na2l_fr2_ked(date,Type,Statement,na2l,fr2s3r) VALUES(%s,%s,%s,%s,%s)"
                data = (selected_date, "مقبوضات", name[0], 0, 0)
                mycursor.execute(sql, data)
                myconn.commit()
            for name in statement_names:
                sql = "INSERT INTO na2l_fr2_ked(date,Type,Statement,na2l,fr2s3r) VALUES(%s,%s,%s,%s,%s)"
                data = (selected_date, "مدفوعات", name[0], 0, 0)
                mycursor.execute(sql, data)
                myconn.commit()
        """

    def start_wi_index_1(self):
        try:
            self.tabWidget.setCurrentIndex(1)
            self.show_data_in_frame_yw()
        except:
            self.Message("يوجد مشكله في الانترنت", False, 3)
            self.waiting_frame_end()

    def move(self, m):
        global username
        global usert
        date = current_date
        ondate = selected_date
        time = current_time
        usern = str(username)
        user_type = str(usert)
        sys_type = "برنامج"
        move = str(m)

        insertsql = "INSERT INTO SystemActivity(date,ModDate,time,Activity,softwareType) VALUES(%s,%s,%s,%s,%s)"
        infodata = (date, ondate,time,move, sys_type)
        mycursor.execute(insertsql, infodata)
        myconn.commit()
                
        id_a = mycursor.lastrowid
                
        insertsql = "INSERT INTO UserA_Has_SActivity(UserName,a_id) VALUES(%s,%s)"
        infodata = (usern,id_a)
        mycursor.execute(insertsql, infodata)
        myconn.commit()

    ## --------------- نظره عامه ---------------##
    def nzra_ama_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("نظره عامه")
        try:
            self.tabWidget.setCurrentIndex(0)
            self.get_total_benzene_consumption()
            self.get_petrolprice()
            self.show_login_history_in_table()
            self.waiting_frame_end()
        except:
            self.Message("يوجد مشكله في الانترنت", False, 3)
            self.waiting_frame_end()

    def get_petrolprice(self):
        sql = " SELECT * FROM petrolprice WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        result = mycursor.fetchone()
        if result == None or result == []:
            return
        else:
            self.show_petrolprice_in_boxes(
                float(result[1]), float(result[2]), float(result[3]), float(result[4])
            )

    def show_petrolprice_in_boxes(self, p_solar, p_80, p_92, p_95):
        self.doubleSpinBox_2.setValue(p_solar)
        self.doubleSpinBox.setValue(p_80)
        self.doubleSpinBox_4.setValue(p_92)
        self.doubleSpinBox_3.setValue(p_95)

    def update_petrolprice_from_boxes(self):
        self.waiting_frame_start()
        try:
            sql = "UPDATE petrolprice SET solarprice =%s WHERE date=%s"
            data = (float(self.doubleSpinBox_2.value()), selected_date)
            mycursor.execute(sql, data)
            myconn.commit()

            sql = "UPDATE petrolprice SET petrol80price =%s WHERE date=%s"
            data = (float(self.doubleSpinBox.value()), selected_date)
            mycursor.execute(sql, data)
            myconn.commit()

            sql = "UPDATE petrolprice SET petrol92price =%s WHERE date=%s"
            data = (float(self.doubleSpinBox_4.value()), selected_date)
            mycursor.execute(sql, data)
            myconn.commit()

            sql = "UPDATE petrolprice SET petrol95price =%s WHERE date=%s"
            data = (float(self.doubleSpinBox_3.value()), selected_date)
            mycursor.execute(sql, data)
            myconn.commit()
            self.Message("تم تعديل الاسعار بنجاح", True, 3)
            self.waiting_frame_end()
        except:
            self.Message("يوجد مشكله في الانترنت", False, 3)
            self.waiting_frame_end()

    def get_total_benzene_consumption(self):
        sql = " SELECT total_liter FROM dailyPumpshift_liter WHERE date=%s AND petrolType = %s"
        data = (selected_date, "سولار")
        mycursor.execute(sql, data)
        total_solar = mycursor.fetchall()
        total_solar = self.sum_of_numbers(total_solar)

        sql = " SELECT total_liter FROM dailyPumpshift_liter WHERE date=%s AND petrolType = %s"
        data = (selected_date, "بنزين 80")
        mycursor.execute(sql, data)
        total_p80 = mycursor.fetchall()
        total_p80 = self.sum_of_numbers(total_p80)

        sql = " SELECT total_liter FROM dailyPumpshift_liter WHERE date=%s AND petrolType = %s"
        data = (selected_date, "بنزين 92")
        mycursor.execute(sql, data)
        total_p92 = mycursor.fetchall()
        total_p92 = self.sum_of_numbers(total_p92)

        sql = " SELECT total_liter FROM dailyPumpshift_liter WHERE date=%s AND petrolType = %s"
        data = (selected_date, "بنزين 95")
        mycursor.execute(sql, data)
        total_p95 = mycursor.fetchall()
        total_p95 = self.sum_of_numbers(total_p95)

        self.show_total_benzene_consumption_in_frames(
            total_solar, total_p80, total_p92, total_p95
        )

    def show_total_benzene_consumption_in_frames(self, t_solar, t_80, t_92, t_95):
        self.label_68.setText(str(t_solar))
        self.label_71.setText(str(t_80))
        self.label_73.setText(str(t_92))
        self.label_75.setText(str(t_95))

    def show_login_history_in_table(self):
        self.delete_login_history_in_table()
        sql = """
                SELECT lh.date, lh.time, lh.softwareType, ua.UserName 
                FROM loginHistory lh
                JOIN userA_has_loginHistory ualh ON lh.id = ualh.h_id
                JOIN UserAccount ua ON ualh.User_Name = ua.UserName
                WHERE lh.date = %s
                """
        data = (selected_date,)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        self.tableWidget_20.setRowCount(0)
        self.tableWidget_20.insertRow(0)
        self.tableWidget_20.setHorizontalHeaderLabels(
            ["التاريخ", "الوقت", "النوع", "اسم المستخدم"]
        )

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_20.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_20.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1

            row_position = self.tableWidget_20.rowCount()
            self.tableWidget_20.insertRow(row_position)

    def delete_login_history_in_table(self):
        self.tableWidget_20.clear()

    def Export_login_h(self):
        self.waiting_frame_start()
        sql = """
                SELECT lh.date, lh.time, lh.softwareType, ua.UserName 
                FROM loginHistory lh
                JOIN userA_has_loginHistory ualh ON lh.id = ualh.h_id
                JOIN UserAccount ua ON ualh.User_Name = ua.UserName
                WHERE lh.date = %s
                """
        data = (selected_date,)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd, "reports", f"{selected_date} تقرير حركه تسجيل الدخول.xlsx"
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "التاريخ")
        sheet.write(0, 1, "الوقت")
        sheet.write(0, 2, "نوع النظام")
        sheet.write(0, 3, "اسم المستخدم")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## --------------- يوميه الورديه ---------------##
    def YW_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("يوميه الورديه")
        try:
            self.tabWidget.setCurrentIndex(1)
            self.show_data_in_frame_yw()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def show_data_in_frame_yw(self):
        self.delete_data_frame_yw()
        sql = " SELECT * FROM dailyPumpshift_liter WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        self.len_data_in_YW = len(result)
        if self.len_data_in_YW == 0:
            return
        else:
            # obj_n, id, N_T, type, start, end, total
            for i in range(0, len(result)):
                self.verticalLayout_2.addWidget(
                    comp().YW_frame(
                        i + 1,
                        result[i][0],
                        result[i][2],
                        result[i][3],
                        result[i][4],
                        result[i][5],
                        result[i][6],
                    )
                )

    def delete_data_frame_yw(self):
        sql = " SELECT * FROM dailyPumpshift_liter WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        self.len_data_in_YW = len(result)
        if self.len_data_in_YW == 0:
            return
        else:
            for i in range(0, self.len_data_in_YW):
                try:
                    obj = self.findChildren(QFrame, str(f"frame_yw_{i+1}"))[0]
                    if obj is not None:
                        obj.deleteLater()
                except:
                    break

    def Export_yw(self):
        self.waiting_frame_start()
        sql = " SELECT pumpNumber,petrolType,start_code,end_code,total_liter FROM dailyPumpshift_liter WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(cwd, "reports", f"{selected_date} تقرير يوميه الورديه.xlsx")
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "رقم الطلمبه")
        sheet.write(0, 1, "نوع الطلمبه")
        sheet.write(0, 2, "البدايه")
        sheet.write(0, 3, "النهايه")
        sheet.write(0, 4, "الاجمالي")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## --------------- الزيوت ---------------##
    def oils_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("الزيوت")
        try:
            self.tabWidget.setCurrentIndex(2)
            self.get_oils()
            self.show_oils_in_table_storage()
            self.show_oils_in_table_ward()
            self.auto_complete_oil()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def get_oils(self):
        sql = " SELECT oilName FROM oil"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.comboBox_10.clear()
        self.comboBox_14.clear()
        for c in range(len(result)):
            self.comboBox_10.addItem(result[c][0])
            self.comboBox_14.addItem(result[c][0])

    def get_data_when_compo_change_storage(self):
        oil_n = str(self.comboBox_10.currentText())
        sql = " SELECT beginingBalance,endingBalance,inboundtowarehouse FROM OilStorage WHERE date=%s AND oilname=%s"
        data = (selected_date, oil_n)
        mycursor.execute(sql, data)
        result = mycursor.fetchone()
        if result != None:
            self.spinBox_17.setValue(int(result[0]))
            self.spinBox_18.setValue(int(result[1]))
            self.spinBox_19.setValue(int(result[2]))

            self.start_oils_storage_s = str(result[0])
            self.end_oils_storage_s = str(result[1])
            self.Treasury_Ward_oils_storage_s = str(result[2])

    def get_data_when_compo_change_ward(self):
        oil_n = str(self.comboBox_14.currentText())
        sql = " SELECT StartTermBalance,endTermBalance,sold FROM oilshift WHERE date=%s AND oilname=%s"
        data = (selected_date, oil_n)
        mycursor.execute(sql, data)
        result = mycursor.fetchone()
        if result != None:
            self.spinBox_6.setValue(int(result[0]))
            self.spinBox_8.setValue(int(result[1]))
            self.spinBox_16.setValue(int(result[2]))

            self.first_term_balance_oils_ward_s = str(result[0])
            self.end_term_balance_oils_ward_s = str(result[1])
            self.saled_Ward_oils_ward_s = str(result[2])

    def add_oil_in_storage(self):
        self.waiting_frame_start()
        oil_name = self.comboBox_10.currentText()
        start = int(self.spinBox_17.value())
        end = int(self.spinBox_18.value())
        Treasury_Ward = int(self.spinBox_19.value())

        if start >= end:
            sql = "UPDATE OilStorage SET beginingBalance = %s , endingBalance = %s, inboundtowarehouse = %s WHERE oilname=%s AND date=%s"
            data = (start, end, Treasury_Ward, oil_name, selected_date)
            mycursor.execute(sql, data)
            myconn.commit()

            self.show_oils_in_table_storage()
            if self.start_oils_storage_s != str(start):
                self.move(
                    f"زيت {str(oil_name)} تم تعديل رصيد البدايه من {self.start_oils_storage_s} الي {str(start)} "
                )
            if self.end_oils_storage_s != str(end):
                self.move(
                    f"زيت {str(oil_name)} تم تعديل رصيد النهايه من {self.end_oils_storage_s} الي {str(end)} "
                )
            if self.Treasury_Ward_oils_storage_s != str(Treasury_Ward):
                self.move(
                    f"زيت {str(oil_name)} تم تعديل وارد مخزن من {self.Treasury_Ward_oils_storage_s} الي {str(Treasury_Ward)} "
                )
            self.waiting_frame_end()
            self.Message("تم التعديل بنجاح", True, 3)
        else:
            self.waiting_frame_end()
            self.Message("يجب ان تكون رصيد البدايه اكبر من رصيد النهايه", False, 3)

    def show_oils_in_table_storage(self):
        self.tableWidget_4.clear()
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        self.tableWidget_4.setHorizontalHeaderLabels(
            ["نوع الزيت", "رصيد البدايه", "رصيد النهايه", "وارد مخزن"]
        )

        sql = " SELECT oilname,beginingBalance,endingBalance,inboundtowarehouse FROM OilStorage WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_4.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1

            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)

    def add_oil_in_ward(self):
        self.waiting_frame_start()
        oil_name = self.comboBox_14.currentText()
        first_term_balance = int(self.spinBox_6.value())
        end_term_balance = int(self.spinBox_8.value())
        saled = first_term_balance - end_term_balance

        sql = " SELECT price FROM oil WHERE oilName=%s "
        data = (str(oil_name),)
        mycursor.execute(sql, data)
        pr = mycursor.fetchone()

        if first_term_balance >= end_term_balance:
            sql1 = "UPDATE oilshift SET StartTermBalance = %s , endTermBalance = %s, sold = %s , price = %s WHERE oilname=%s AND date=%s"
            data1 = (
                first_term_balance,
                end_term_balance,
                saled,
                float(pr[0]),
                str(oil_name),
                selected_date,
            )
            mycursor.execute(sql1, data1)
            myconn.commit()
            self.show_oils_in_table_ward()

            if self.first_term_balance_oils_ward_s != str(first_term_balance):
                self.move(
                    f"زيت {str(oil_name)} تم تعديل رصيد اول المده من {self.first_term_balance_oils_ward_s} الي {str(first_term_balance)} "
                )
            if self.end_term_balance_oils_ward_s != str(end_term_balance):
                self.move(
                    f"زيت {str(oil_name)} تم تعديل رصيد اخر المده من {self.end_term_balance_oils_ward_s} الي {str(end_term_balance)} "
                )

            self.waiting_frame_end()
            self.Message("تم التعديل بنجاح", True, 3)
        else:
            self.waiting_frame_end()
            self.Message("يجب ان يكون رصيد اول المده اكبر من رصيد اخر المده", False, 3)

    def show_oils_in_table_ward(self):
        self.tableWidget_9.clear()
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_9.insertRow(0)
        self.tableWidget_9.setHorizontalHeaderLabels(
            [
                "نوع الزيت",
                "رصيد اول المده",
                "رصيد اخر المده",
                "مباع",
                "سعر",
                "الاجمالي",
            ]
        )

        sql = " SELECT oilname,StartTermBalance,endTermBalance,sold,price,(sold*price) as total FROM oilshift WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_9.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_9.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            row_position = self.tableWidget_9.rowCount()
            self.tableWidget_9.insertRow(row_position)

    def add_oil(self):
        self.waiting_frame_start()
        try:
            oil_name = self.lineEdit_41.text()
            price = float(self.doubleSpinBox_5.value())
            if str(oil_name) == "" or price == "":
                self.waiting_frame_end()
                self.Message("يوجد حقول فارغه", False, 3)
                return
            else:
                sql = " SELECT oilName FROM oil WHERE oilName = %s "
                data = (str(oil_name),)
                mycursor.execute(sql, data)
                result = mycursor.fetchone()
                if result == [] or result == None:
                    sql = "INSERT INTO oil(oilName,price) VALUES(%s,%s)"
                    data = (str(oil_name), price)
                    mycursor.execute(sql, data)
                    myconn.commit()

                    self.move(f"اضافه زيت {str(oil_name)}")

                    self.lineEdit_41.setText("")
                    self.doubleSpinBox_5.setValue(0)
                    self.auto_complete_oil()

                    sql = "INSERT INTO oilshift(date,oilname,StartTermBalance,endTermBalance,sold,price) VALUES(%s,%s,%s,%s,%s,%s)"
                    data = (selected_date, str(oil_name), 0, 0, 0, price)
                    mycursor.execute(sql, data)
                    myconn.commit()

                    sql = "INSERT INTO OilStorage(date,oilname,beginingBalance,endingBalance,inboundtowarehouse) VALUES(%s,%s,%s,%s,%s)"
                    data = (selected_date, str(oil_name), 0, 0, 0)
                    mycursor.execute(sql, data)
                    myconn.commit()

                    self.waiting_frame_end()
                    self.Message("تم الاضافه بنجاح", True, 3)
                else:
                    self.waiting_frame_end()
                    self.Message("هذا الزيت موجود بلفعل", False, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def search_oil(self):
        self.waiting_frame_start()
        self.oil_id = -1
        self.oil_name_in_search = self.lineEdit_35.text()

        sql = " SELECT oilName,price FROM oil WHERE oilName=%s "
        data = (self.oil_name_in_search,)
        mycursor.execute(sql, data)
        result = mycursor.fetchone()
        if result == [] or result == None:
            self.waiting_frame_end()
            return
        else:
            self.lineEdit_46.setText(str(result[0]))
            self.doubleSpinBox_6.setValue(float(result[1]))
            self.pushButton_62.setEnabled(True)
            self.pushButton_61.setEnabled(True)
            self.oil_id = result[0]
            self.waiting_frame_end()

    def update_oil(self):
        self.waiting_frame_start()
        try:
            oil_name = self.lineEdit_46.text()
            price = float(self.doubleSpinBox_6.value())

            if self.oil_id == -1:
                self.waiting_frame_end()
                return
            else:
                sql = " SELECT oilName,price FROM oil WHERE oilName=%s"
                data = (self.oil_id,)
                mycursor.execute(sql, data)
                result = mycursor.fetchone()

                sql = "UPDATE oil SET price = %s , oilName = %s WHERE oilName=%s"
                data = (price, oil_name, self.oil_id)
                mycursor.execute(sql, data)
                myconn.commit()

                if str(result[0]) != str(oil_name):
                    self.move(
                        f"تعديل اسم الزيت من {str(result[0])} الي {str(self.oil_id)}"
                    )
                if str(result[1]) != str(price):
                    self.move(
                        f"تعديل سعر الزيت {str(result[0])} من {str(result[1])} الي {str(price)}"
                    )

                self.lineEdit_35.setText("")
                self.lineEdit_46.setText("")
                self.doubleSpinBox_6.setValue(0)
                self.pushButton_62.setEnabled(False)
                self.pushButton_61.setEnabled(False)
                self.auto_complete_oil()
                self.oil_id = -1
                self.waiting_frame_end()
                self.Message("تم تعديل بنجاح", True, 2)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def delete_oil(self):
        self.waiting_frame_start()
        try:
            oil_name = self.lineEdit_46.text()
            price = float(self.doubleSpinBox_6.value())

            if self.oil_id == -1:
                self.waiting_frame_end()
                return
            else:
                sql = "DELETE FROM oil WHERE oilName=%s"
                data = (self.oil_id,)
                mycursor.execute(sql, data)
                myconn.commit()

                self.lineEdit_35.setText("")
                self.lineEdit_46.setText("")
                self.doubleSpinBox_6.setValue(0)
                self.auto_complete_oil()
                self.pushButton_62.setEnabled(False)
                self.pushButton_61.setEnabled(False)
                self.oil_id = -1
                self.move(f"تم حذف زيت {str(self.oil_id)}")
                self.waiting_frame_end()
                self.Message("تم الحذف بنجاح", True, 2)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def auto_complete_oil(self):
        oils_name_list.clear()
        sql = " SELECT oilName FROM oil"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for names in result:
            oils_name_list.append(names[0])

        lineedit = self.lineEdit_35
        completer = QCompleter()
        lineedit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete(model)

    def Auto_Complete(self, model):
        model.setStringList(oils_name_list)

    def Export_oils_storage(self):
        self.waiting_frame_start()
        sql = " SELECT oilname,beginingBalance,endingBalance,inboundtowarehouse FROM OilStorage WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(cwd, "reports", f"{selected_date} تقرير مخزن الزيوت.xlsx")
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "نوع الزيت")
        sheet.write(0, 1, "رصيد البدايه")
        sheet.write(0, 2, "رصيد النهايه")
        sheet.write(0, 3, "وارد مخزن")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    def Export_oils_ward(self):
        self.waiting_frame_start()
        sql = " SELECT oilname,StartTermBalance,endTermBalance,sold,price,(sold*price) as total FROM oilshift WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(cwd, "reports", f"{selected_date} تقرير ورديه الزيوت.xlsx")
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "نوع الزيت")
        sheet.write(0, 1, "رصيد اول المده")
        sheet.write(0, 2, "رصيد اخر المده")
        sheet.write(0, 3, "مباع")
        sheet.write(0, 4, "سعر")
        sheet.write(0, 5, "الاجمالي")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## --------------- المصاريف ---------------##
    def masaref_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("المصاريف")
        try:
            self.tabWidget.setCurrentIndex(3)
            self.show_data_in_table_msaref()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def show_data_in_table_msaref(self):
        self.delete_data_in_table_msaref()
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)
        self.tableWidget_5.setColumnHidden(0, True)
        self.tableWidget_5.setHorizontalHeaderLabels(["id", "المبلغ", "السند", ""])

        sql = " SELECT id,bond,Amount FROM expenses WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_5.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            self.pushButton = QPushButton(self.tableWidget_5)
            self.pushButton.setObjectName(f"pushButton_del_msaref={row}")
            self.pushButton.setEnabled(True)
            self.pushButton.setMinimumSize(QSize(35, 35))
            self.pushButton.setMaximumSize(QSize(35, 35))
            self.pushButton.clicked.connect(lambda: self.delete_msaref())
            self.pushButton.setText("×")
            self.tableWidget_5.setCellWidget(row, column, self.pushButton)

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

    def delete_data_in_table_msaref(self):
        self.tableWidget_5.clear()

    def delete_msaref(self):
        self.waiting_frame_start()
        try:
            clicked_row = self.tableWidget_5.currentRow()
            if clicked_row == -1:
                return
            msrof_id = int(self.tableWidget_5.item(clicked_row, 0).text())

            sql = " SELECT bond,Amount FROM expenses WHERE id=%s "
            data = (msrof_id,)
            mycursor.execute(sql, data)
            s_m = mycursor.fetchone()
            s = str(s_m[0])
            m = str(s_m[1])

            sql = "DELETE FROM expenses WHERE id=%s "
            data = (msrof_id,)
            mycursor.execute(sql, data)
            myconn.commit()

            self.move(f'حذف سند "{s}" و مبلغ {m} من المصاريف')
            self.show_data_in_table_msaref()
            self.waiting_frame_end()
            self.Message("تم الحذف بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def add_data_to_msaref(self):
        self.waiting_frame_start()
        try:
            sand = self.lineEdit_25.text()
            mony = self.spinBox.value()

            sql = "INSERT INTO expenses(date,bond,Amount) VALUES(%s,%s,%s)"
            data = (selected_date, str(sand), float(mony))
            mycursor.execute(sql, data)
            myconn.commit()

            self.show_data_in_table_msaref()
            self.lineEdit_25.setText("")
            self.spinBox.setValue(0)
            self.waiting_frame_end()
            self.Message("تم الاضافه بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def Export_msaref(self):
        self.waiting_frame_start()
        sql = " SELECT bond,Amount FROM expenses WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(cwd, "reports", f"{selected_date} تقرير المصاريف.xlsx")
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "السند")
        sheet.write(0, 1, "المبلغ")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## --------------- البونات ---------------##
    def bons_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("البونات")
        try:
            self.tabWidget.setCurrentIndex(4)
            self.show_data_in_table_bons("سولار")
            self.show_matching_bons()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def comboBox_in_bons_clicked(self):
        self.show_data_in_table_bons(str(self.comboBox_6.currentText()))

    def add_bons(self):
        self.waiting_frame_start()
        try:
            benz_type = self.comboBox_6.currentText()
            side = self.comboBox_7.currentText()
            category = int(self.spinBox_20.value())
            if benz_type == "سولار":
                sql = " SELECT solarprice FROM petrolprice WHERE date=%s "
                data = (selected_date,)
                mycursor.execute(sql, data)
                price = mycursor.fetchone()
            elif benz_type == "بنزين 80":
                sql = " SELECT petrol80price FROM petrolprice WHERE date=%s "
                data = (selected_date,)
                mycursor.execute(sql, data)
                price = mycursor.fetchone()
            elif benz_type == "بنزين 92":
                sql = " SELECT petrol92price FROM petrolprice WHERE date=%s "
                data = (selected_date,)
                mycursor.execute(sql, data)
                price = mycursor.fetchone()
            else:
                sql = " SELECT petrol95price FROM petrolprice WHERE date=%s "
                data = (selected_date,)
                mycursor.execute(sql, data)
                price = mycursor.fetchone()

            if self.lineEdit_7.text().isdigit():
                bon_serial = int(self.lineEdit_7.text())
                sql = "INSERT INTO coupons(date,petrolType,Issuer,price,category,total,couponserial) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                data = (
                    selected_date,
                    str(benz_type),
                    str(side),
                    float(price[0]),
                    int(category),
                    (float(float(price[0]) * int(category))),
                    str(bon_serial),
                )
                mycursor.execute(sql, data)
                myconn.commit()

                ## مطابقت البونات
                sql = " SELECT * FROM matchingcoupons WHERE date=%s AND category=%s AND petrolType=%s AND issuer=%s"
                data = (selected_date, int(category), str(benz_type), str(side))
                mycursor.execute(sql, data)
                re = mycursor.fetchone()
                if re == None or re == []:
                    sql = "INSERT INTO matchingcoupons(date,Quantity,category,petrolType,issuer,total) VALUES(%s,%s,%s,%s,%s,%s)"
                    data = (
                        selected_date,
                        1,
                        int(category),
                        str(benz_type),
                        str(side),
                        float(int(category) * 1 * float(price[0])),
                    )
                    mycursor.execute(sql, data)
                    myconn.commit()
                else:
                    sql = "UPDATE matchingcoupons SET Quantity = %s, total = %s WHERE date = %s AND category = %s AND petrolType = %s AND issuer = %s"
                    data = (
                        re[1] + 1,
                        float(float((re[1] + 1) * (int(category)) * (float(price[0])))),
                        selected_date,
                        int(category),
                        str(benz_type),
                        str(side),
                    )
                    mycursor.execute(sql, data)
                    myconn.commit()

                self.lineEdit_7.setText("")
                self.spinBox_20.setValue(0)
                self.show_data_in_table_bons(benz_type)
                self.show_matching_bons()
                self.waiting_frame_end()
                self.Message("تم الاضافه بنجاح", True, 3)
            else:
                self.waiting_frame_end()
                self.Message("يرجا ادخال سريال بون صحيح", False, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def show_data_in_table_bons(self, benz_type):
        self.delete_data_in_table_bons()
        self.label_21.setText(str(benz_type))
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        self.tableWidget_6.setColumnHidden(0, True)
        self.tableWidget_6.setHorizontalHeaderLabels(
            ["id", "السعر", "الفئه", "الاجمالي", "سريال البون", "الجهة", ""]
        )

        sql = " SELECT id,price,category,total,couponserial,Issuer FROM coupons WHERE date=%s AND petrolType=%s"
        data = (selected_date, benz_type)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_6.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            self.pushButton = QPushButton(self.tableWidget_6)
            self.pushButton.setObjectName(f"pushButton_del_bons={row}")
            self.pushButton.setEnabled(True)
            self.pushButton.setMinimumSize(QSize(35, 35))
            self.pushButton.setMaximumSize(QSize(35, 35))
            self.pushButton.clicked.connect(lambda: self.delete_bons())
            self.pushButton.setText("×")
            self.tableWidget_6.setCellWidget(row, column, self.pushButton)

            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)

    def delete_data_in_table_bons(self):
        self.tableWidget_6.clear()

    def delete_bons(self):
        self.waiting_frame_start()
        try:
            clicked_row = self.tableWidget_6.currentRow()
            if clicked_row == -1:
                self.waiting_frame_end()
                return
            bon_id = int(self.tableWidget_6.item(clicked_row, 0).text())
            sql = " SELECT * FROM coupons WHERE id=%s"
            data = (bon_id,)
            mycursor.execute(sql, data)
            data = mycursor.fetchone()

            price = data[5]
            category = data[4]
            benz_type = data[2]
            side = data[3]
            sryal = data[7]

            self.move(
                f"حذف بون من النوع {str(benz_type)} و الجهه {str(side)} فئه {str(category)} و سريال البون {str(sryal)}"
            )

            ## مطابقت البونات
            sql = " SELECT Quantity FROM matchingcoupons WHERE date=%s AND category=%s AND petrolType=%s AND issuer=%s"
            data = (selected_date, int(category), str(benz_type), str(side))
            mycursor.execute(sql, data)
            re = mycursor.fetchone()

            newq = re[0] - 1
            sql = "UPDATE matchingcoupons SET Quantity = %s, total = %s WHERE date = %s AND category = %s AND petrolType = %s AND issuer = %s"
            data = (
                newq,
                float((newq) * (category) * (price)),
                selected_date,
                int(category),
                str(benz_type),
                str(side),
            )
            mycursor.execute(sql, data)
            myconn.commit()

            sql = "DELETE FROM coupons WHERE id=%s"
            data = (bon_id,)
            mycursor.execute(sql, data)
            myconn.commit()

            self.show_data_in_table_bons(str(self.comboBox_6.currentText()))
            self.show_matching_bons()
            self.waiting_frame_end()
            self.Message("تم الحذف بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)
        self.waiting_frame_end()

    def delete_tuples_with_zero(self, list_of_tuples):
        new_list = []
        for tuplee in list_of_tuples:
            if tuplee[0] != 0.0:
                new_list.append(tuplee)
        return new_list

    def final_tuples_in_m_bons(self, list_of_tuples):
        new_list = []
        i = 0
        while i < len(list_of_tuples):
            if i == len(list_of_tuples) - 1:
                new_list.append(list_of_tuples[i])
                break
            if list_of_tuples[i][1] == list_of_tuples[i + 1][1]:
                new_list.append(
                    (
                        int(list_of_tuples[i][0] + list_of_tuples[i + 1][0]),
                        list_of_tuples[i][1],
                        str(
                            float(
                                float(list_of_tuples[i][2])
                                + float(list_of_tuples[i + 1][2])
                            )
                        ),
                    )
                )
                i = i + 2
            else:
                new_list.append(list_of_tuples[i])
                i = i + 1
        return new_list

    def show_matching_bons(self):
        self.tableWidget_21.clear()
        self.tableWidget_23.clear()
        self.tableWidget_24.clear()
        self.tableWidget_25.clear()
        self.tableWidget_26.clear()
        self.tableWidget_27.clear()
        self.show_solar_matching_bons()
        self.show_p80_matching_bons()
        self.show_p92_matching_bons()
        self.show_95_matching_bons()
        self.show_police_matching_bons()
        self.show_gm3ya_matching_bons()

    def show_solar_matching_bons(self):
        self.tableWidget_21.clear()
        self.tableWidget_21.setHorizontalHeaderLabels(["العدد", "الفئه", "الاجمالي"])
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND petrolType=%s ORDER BY category"
        data = (selected_date, "سولار")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        result = self.final_tuples_in_m_bons(result)

        total = 0
        if result != [] or result != None:
            for row, form in enumerate(result):
                for column, item in enumerate(form):
                    if column == 2:
                        total = total + float(item)
                    self.tableWidget_21.setItem(
                        row, column, QTableWidgetItem(str(item))
                    )
                    item = self.tableWidget_21.item(row, column)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)
                    column += 1

                row_position = self.tableWidget_21.rowCount()
                self.tableWidget_21.insertRow(row_position)

            self.spinBox_9.setValue(int(total))

    def show_p80_matching_bons(self):
        self.tableWidget_23.clear()
        self.tableWidget_23.setHorizontalHeaderLabels(["العدد", "الفئه", "الاجمالي"])
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND petrolType=%s ORDER BY category"
        data = (selected_date, "بنزين 80")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        result = self.final_tuples_in_m_bons(result)

        total = 0
        if result != [] or result != None:
            for row, form in enumerate(result):
                for column, item in enumerate(form):
                    if column == 2:
                        total = total + float(item)
                    self.tableWidget_23.setItem(
                        row, column, QTableWidgetItem(str(item))
                    )
                    item = self.tableWidget_23.item(row, column)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)
                    column += 1

                row_position = self.tableWidget_23.rowCount()
                self.tableWidget_23.insertRow(row_position)

        self.spinBox_11.setValue(int(total))

    def show_p92_matching_bons(self):
        self.tableWidget_24.clear()
        self.tableWidget_24.setHorizontalHeaderLabels(["العدد", "الفئه", "الاجمالي"])
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND petrolType=%s ORDER BY category"
        data = (selected_date, "بنزين 92")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        result = self.final_tuples_in_m_bons(result)

        total = 0
        if result != [] or result != None:
            for row, form in enumerate(result):
                for column, item in enumerate(form):
                    if column == 2:
                        total = total + float(item)
                    self.tableWidget_24.setItem(
                        row, column, QTableWidgetItem(str(item))
                    )
                    item = self.tableWidget_24.item(row, column)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)
                    column += 1

                row_position = self.tableWidget_24.rowCount()
                self.tableWidget_24.insertRow(row_position)

            self.spinBox_12.setValue(int(total))

    def show_95_matching_bons(self):
        self.tableWidget_25.clear()
        self.tableWidget_25.setHorizontalHeaderLabels(["العدد", "الفئه", "الاجمالي"])
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND petrolType=%s ORDER BY category"
        data = (selected_date, "بنزين 95")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        result = self.final_tuples_in_m_bons(result)

        total = 0
        if result != [] or result != None:
            for row, form in enumerate(result):
                for column, item in enumerate(form):
                    if column == 2:
                        total = total + float(item)
                    self.tableWidget_25.setItem(
                        row, column, QTableWidgetItem(str(item))
                    )
                    item = self.tableWidget_25.item(row, column)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)
                    column += 1

                row_position = self.tableWidget_25.rowCount()
                self.tableWidget_25.insertRow(row_position)

            self.spinBox_13.setValue(int(total))

    def show_police_matching_bons(self):
        self.tableWidget_26.clear()
        self.tableWidget_26.setHorizontalHeaderLabels(["العدد", "الفئه", "الاجمالي"])
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND issuer=%s ORDER BY category"
        data = (selected_date, "شرطه")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        result = self.final_tuples_in_m_bons(result)
        result = self.final_tuples_in_m_bons(result)
        result = self.final_tuples_in_m_bons(result)

        total = 0
        if result != [] or result != None:
            for row, form in enumerate(result):
                for column, item in enumerate(form):
                    if column == 2:
                        total = total + float(item)
                    self.tableWidget_26.setItem(
                        row, column, QTableWidgetItem(str(item))
                    )
                    item = self.tableWidget_26.item(row, column)
                    if item is not None:
                        item.setTextAlignment(Qt.AlignCenter)
                    column += 1

                row_position = self.tableWidget_26.rowCount()
                self.tableWidget_26.insertRow(row_position)

            self.spinBox_14.setValue(int(total))

    def show_gm3ya_matching_bons(self):
        self.tableWidget_27.clear()
        self.tableWidget_27.setHorizontalHeaderLabels(["العدد", "الفئه", "الاجمالي"])
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND issuer=%s ORDER BY category"
        data = (selected_date, "جمعية")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        result = self.final_tuples_in_m_bons(result)
        result = self.final_tuples_in_m_bons(result)
        result = self.final_tuples_in_m_bons(result)

        total = 0

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                if column == 2:
                    total = total + float(item)
                self.tableWidget_27.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_27.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)
                column += 1

            row_position = self.tableWidget_27.rowCount()
            self.tableWidget_27.insertRow(row_position)

        self.spinBox_15.setValue(int(total))

    def Export_bons(self):
        self.waiting_frame_start()
        sql = " SELECT petrolType,Issuer,price,category,total,couponserial FROM coupons WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(cwd, "reports", f"{selected_date} تقرير البونات.xlsx")
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "نوع البنزين")
        sheet.write(0, 1, "الجهة")
        sheet.write(0, 2, "السعر")
        sheet.write(0, 3, "الفئه")
        sheet.write(0, 4, "الاجمالي")
        sheet.write(0, 5, "سريال البون")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    def Export_solar_matching_bons(self):
        self.waiting_frame_start()
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND petrolType=%s ORDER BY category"
        data = (selected_date, "سولار")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        data = self.final_tuples_in_m_bons(result)

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd, "reports", f"{selected_date} تقرير مطابقه بونات السولار.xlsx"
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "العدد")
        sheet.write(0, 1, "الفئه")
        sheet.write(0, 2, "الاجمالي")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    def Export_p80_matching_bons(self):
        self.waiting_frame_start()
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND petrolType=%s ORDER BY category"
        data = (selected_date, "بنزين 80")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        data = self.final_tuples_in_m_bons(result)

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd, "reports", f"{selected_date} تقرير مطابقه بونات بنزين 80.xlsx"
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "العدد")
        sheet.write(0, 1, "الفئه")
        sheet.write(0, 2, "الاجمالي")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    def Export_p92_matching_bons(self):
        self.waiting_frame_start()
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND petrolType=%s ORDER BY category"
        data = (selected_date, "بنزين 92")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        data = self.final_tuples_in_m_bons(result)

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd, "reports", f"{selected_date} تقرير مطابقه بونات بنزين 92.xlsx"
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "العدد")
        sheet.write(0, 1, "الفئه")
        sheet.write(0, 2, "الاجمالي")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    def Export_p95_matching_bons(self):
        self.waiting_frame_start()
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND petrolType=%s ORDER BY category"
        data = (selected_date, "بنزين 95")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        data = self.final_tuples_in_m_bons(result)

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd, "reports", f"{selected_date} تقرير مطابقه بونات بنزين 95.xlsx"
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "العدد")
        sheet.write(0, 1, "الفئه")
        sheet.write(0, 2, "الاجمالي")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    def Export_police_matching_bons(self):
        self.waiting_frame_start()
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND issuer=%s ORDER BY category"
        data = (selected_date, "شرطه")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        result = self.final_tuples_in_m_bons(result)
        result = self.final_tuples_in_m_bons(result)
        data = self.final_tuples_in_m_bons(result)

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd, "reports", f"{selected_date} تقرير مطابقه بونات شرطه.xlsx"
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "العدد")
        sheet.write(0, 1, "الفئه")
        sheet.write(0, 2, "الاجمالي")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    def Export_gm3ya_matching_bons(self):
        self.waiting_frame_start()
        sql = " SELECT Quantity,category,total FROM matchingcoupons WHERE date=%s AND issuer=%s ORDER BY category"
        data = (selected_date, "جمعية")
        mycursor.execute(sql, data)
        result = mycursor.fetchall()
        result = self.delete_tuples_with_zero(result)
        result = self.final_tuples_in_m_bons(result)
        result = self.final_tuples_in_m_bons(result)
        data = self.final_tuples_in_m_bons(result)

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd, "reports", f"{selected_date} تقرير مطابقه بونات جمعيه.xlsx"
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "العدد")
        sheet.write(0, 1, "الفئه")
        sheet.write(0, 2, "الاجمالي")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## --------------- عملاء آجله ---------------##
    def omala_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("عملاء آجله")
        try:
            self.tabWidget.setCurrentIndex(5)
            self.get_clients()
            self.Show_clients_payments()
            self.Show_total_payments()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def get_clients(self):
        sql = " SELECT national_ID FROM customer"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.comboBox_17.clear()
        for c in range(len(result)):
            self.comboBox_17.addItem(result[c][0])

    def Add_payment_from_client(self):
        self.waiting_frame_start()
        try:
            client_name = self.comboBox_17.currentText()
            sand = self.lineEdit_10.text()
            mony = self.spinBox_2.value()

            sql = "INSERT INTO creditCustomer(date,customer_NID,bond,Amount) VALUES(%s,%s,%s,%s)"
            data = (selected_date, str(client_name), str(sand), int(mony))
            mycursor.execute(sql, data)
            myconn.commit()

            self.Show_clients_payments()
            self.Show_total_payments()
            self.lineEdit_10.setText("")
            self.spinBox_2.setValue(0)
            self.waiting_frame_end()
            self.Message("تم الاضافه بنجاح", True, 2)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def Show_clients_payments(self):
        self.Delete_payments_from_table()
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.insertRow(0)
        self.tableWidget_7.setColumnHidden(0, True)
        self.tableWidget_7.setHorizontalHeaderLabels(
            ["id", "العميل", "المبلغ", "السند", ""]
        )

        sql = " SELECT id,customer_NID,Amount,bond FROM creditCustomer WHERE date=%s ORDER BY customer_NID"
        data = (selected_date,)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_7.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_7.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            self.pushButton = QPushButton(self.tableWidget_7)
            self.pushButton.setObjectName(f"pushButton_del_payments={row}")
            self.pushButton.setEnabled(True)
            self.pushButton.setMinimumSize(QSize(35, 35))
            self.pushButton.setMaximumSize(QSize(35, 35))
            self.pushButton.clicked.connect(lambda: self.delete_payments())
            self.pushButton.setText("×")
            self.tableWidget_7.setCellWidget(row, column, self.pushButton)

            row_position = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(row_position)

    def Delete_payments_from_table(self):
        self.tableWidget_7.clear()

    def delete_payments(self):
        self.waiting_frame_start()
        try:
            clicked_row = self.tableWidget_7.currentRow()
            if clicked_row == -1:
                self.waiting_frame_end()
                return
            payment_id = int(self.tableWidget_7.item(clicked_row, 0).text())
            sql = " SELECT customer_NID,bond,Amount FROM creditCustomer WHERE id=%s"
            data = (payment_id,)
            mycursor.execute(sql, data)
            dat = mycursor.fetchone()
            c_n = str(dat[0])
            s = str(dat[1])
            m = str(dat[2])

            sql = "DELETE FROM creditCustomer WHERE id=%s "
            data = (payment_id,)
            mycursor.execute(sql, data)
            myconn.commit()

            self.move(f'حذف سند "{s}" و مبلغ {m} من العميل {c_n}')
            self.Show_clients_payments()
            self.Show_total_payments()
            self.waiting_frame_end()
            self.Message("تم الحذف بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def Show_total_payments(self):
        sql = " SELECT Amount FROM creditCustomer WHERE date=%s"
        data = (selected_date,)
        mycursor.execute(sql, data)
        total_Term_Clients = mycursor.fetchall()
        total_Term_Clients = self.sum_of_numbers(total_Term_Clients)
        self.spinBox_3.setValue(int(total_Term_Clients))

    def add_client_clicked(self):
        self.waiting_frame_start()
        try:
            self.pushButton_14.setText("عملاء")
            self.tabWidget.setCurrentIndex(12)
            self.auto_complete_client()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def add_client(self):
        self.waiting_frame_start()
        try:
            if self.lineEdit_31.text().isdigit() and self.lineEdit_32.text().isdigit():
                client_name = str(self.lineEdit_30.text())
                Nid = str(self.lineEdit_31.text())
                mobile_num = str(self.lineEdit_32.text())
                if client_name == "" or str(Nid) == "" or str(mobile_num) == "":
                    self.waiting_frame_end()
                    self.Message("يوجد حقول فارغه", False, 3)
                    return
                else:
                    if len(Nid) == 14:
                        sql = " SELECT * FROM customer WHERE national_ID = %s "
                        data = (Nid,)
                        mycursor.execute(sql, data)
                        result = mycursor.fetchone()
                        if result == [] or result == None:
                            sql = "INSERT INTO customer(name,national_ID,phone_number) VALUES(%s,%s,%s)"
                            data = (client_name, Nid, mobile_num)
                            mycursor.execute(sql, data)
                            myconn.commit()

                            self.lineEdit_30.setText("")
                            self.lineEdit_31.setText("")
                            self.lineEdit_32.setText("")
                            self.auto_complete_client()
                            self.waiting_frame_end()
                            self.Message("تم الاضافه بنجاح", True, 3)
                        else:
                            self.waiting_frame_end()
                            self.Message("هذا العميل موجود بلفعل", False, 3)
                    else:
                        self.waiting_frame_end()
                        self.Message("يرجي ادخال الرقم القومي صحيحه", False, 3)
                        return
            else:
                self.waiting_frame_end()
                self.Message("يرجي ادخال بيانات صحيحه", False, 3)
                return
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def search_client(self):
        self.waiting_frame_start()
        self.client_id = -1
        self.client_name = self.lineEdit_28.text()
        sql = " SELECT * FROM customer WHERE name=%s "
        data = (self.client_name,)
        mycursor.execute(sql, data)
        result = mycursor.fetchone()
        if result == [] or result == None:
            self.waiting_frame_end()
            return
        else:
            self.lineEdit_37.setText(str(result[0]))
            self.lineEdit_40.setText(str(result[1]))
            self.lineEdit_38.setText(str(result[2]))
            self.pushButton_55.setEnabled(True)
            self.pushButton_56.setEnabled(True)
            self.client_id = result[1]
            self.waiting_frame_end()

    def update_client(self):
        self.waiting_frame_start()
        try:
            client_name = str(self.lineEdit_37.text())
            Nid = int(self.lineEdit_40.text())
            mobile_num = int(self.lineEdit_38.text())

            if self.client_id == -1:
                self.waiting_frame_end()
                return
            else:
                sql = " SELECT name,national_ID,phone_number FROM customer WHERE national_ID=%s "
                data = (self.client_id,)
                mycursor.execute(sql, data)
                result = mycursor.fetchone()
                n = str(result[0])
                nid = str(result[1])
                mn = str(result[2])

                sql = "UPDATE customer SET name = %s , national_ID = %s, phone_number  = %s WHERE national_ID=%s"
                data = (
                    client_name,
                    Nid,
                    mobile_num,
                    self.client_id,
                )
                mycursor.execute(sql, data)
                myconn.commit()

                if n != client_name:
                    self.move(f"تعديل اسم العميل من {n} الي {client_name}")
                if nid != str(Nid):
                    self.move(f"تعديل الرقم القومي من {nid} الي {str(Nid)} للعميل {n}")
                if mn != str(mobile_num):
                    self.move(
                        f"تعديل رقم الهاتف من {mn} الي {str(mobile_num)} للعميل {n}"
                    )

                self.lineEdit_37.setText("")
                self.lineEdit_40.setText("")
                self.lineEdit_38.setText("")
                self.auto_complete_client()
                self.pushButton_55.setEnabled(False)
                self.pushButton_56.setEnabled(False)
                self.client_id = -1
                self.waiting_frame_end()
                self.Message("تم تعديل بنجاح", True, 2)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def delete_client(self):
        self.waiting_frame_start()
        try:
            if self.client_id == -1:
                self.waiting_frame_end()
                return
            else:
                sql = " SELECT name FROM customer WHERE national_ID=%s "
                data = (self.client_id,)
                mycursor.execute(sql, data)
                result = mycursor.fetchone()
                naa = str(result[0])

                sql = "DELETE FROM customer WHERE national_ID=%s"
                data = (self.client_id,)
                mycursor.execute(sql, data)
                myconn.commit()

                self.lineEdit_37.setText("")
                self.lineEdit_40.setText("")
                self.lineEdit_38.setText("")
                self.auto_complete_client()
                self.pushButton_55.setEnabled(False)
                self.pushButton_56.setEnabled(False)
                self.client_id = -1
                self.move(f"تم حذف العميل {naa}")
                self.waiting_frame_end()
                self.Message("تم الحذف بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def auto_complete_client(self):
        client_name_list.clear()
        sql = " SELECT name FROM customer"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for names in result:
            client_name_list.append(names[0])

        lineedit = self.lineEdit_28
        completer = QCompleter()
        lineedit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete_cl(model)

    def Auto_Complete_cl(self, model):
        model.setStringList(client_name_list)

    def Export_omala_agla(self):
        self.waiting_frame_start()
        sql = " SELECT customer_NID,Amount,bond FROM creditCustomer WHERE date=%s ORDER BY customer_NID"
        data = (selected_date,)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(cwd, "reports", f"{selected_date} تقرير العملا الاجله.xlsx")
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "العميل")
        sheet.write(0, 1, "المبلغ")
        sheet.write(0, 2, "السند")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## --------------- يومية الخزينه  ---------------##
    def yawmet_al5zena_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("يومية الخزينه")
        try:
            self.tabWidget.setCurrentIndex(6)
            self.get_and_show_data_yawmet_al5zena()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def sum_of_numbers(self, tuples_list):
        total_sum = float(0.0)
        for tup in tuples_list:
            total_sum += float(tup[0])
        return float(total_sum)

    def get_and_show_data_yawmet_al5zena(self):
        sql = " SELECT * FROM petrolprice WHERE date=%s "
        data = (selected_date,)
        mycursor.execute(sql, data)
        petrolprice = mycursor.fetchone()
        self.solar_price = float(petrolprice[1])
        self.p80_price = float(petrolprice[2])
        self.p92_price = float(petrolprice[3])
        self.p95_price = float(petrolprice[4])

        sql = " SELECT (start_code - end_code) AS total_liter FROM dailyPumpshift WHERE date=%s AND petrolType = %s"
        data = (selected_date, "سولار")
        mycursor.execute(sql, data)
        total_solar = mycursor.fetchall()
        self.total_solar = self.sum_of_numbers(total_solar)

        sql = " SELECT (start_code - end_code) AS total_liter FROM dailyPumpshift WHERE date=%s AND petrolType = %s"
        data = (selected_date, "بنزين 80")
        mycursor.execute(sql, data)
        total_p80 = mycursor.fetchall()
        self.total_p80 = self.sum_of_numbers(total_p80)

        sql = " SELECT (start_code - end_code) AS total_liter FROM dailyPumpshift WHERE date=%s AND petrolType = %s"
        data = (selected_date, "بنزين 92")
        mycursor.execute(sql, data)
        total_p92 = mycursor.fetchall()
        self.total_p92 = self.sum_of_numbers(total_p92)

        sql = " SELECT (start_code - end_code) AS total_liter FROM dailyPumpshift WHERE date=%s AND petrolType = %s"
        data = (selected_date, "بنزين 95")
        mycursor.execute(sql, data)
        total_p95 = mycursor.fetchall()
        self.total_p95 = self.sum_of_numbers(total_p95)

        sql = " SELECT sold FROM oilshift WHERE date=%s"
        data = (selected_date,)
        mycursor.execute(sql, data)
        total_oils = mycursor.fetchall()
        self.total_oils = self.sum_of_numbers(total_oils)

        sql = " SELECT (StartTermBalance - endTermBalance) AS total_profit FROM oilshift WHERE date=%s"
        data = (selected_date,)
        mycursor.execute(sql, data)
        total_oils_money = mycursor.fetchall()
        self.total_oils_money = self.sum_of_numbers(total_oils_money)

        self.label_186.setText(str(self.total_solar))
        self.label_246.setText(str(self.total_p80))
        self.label_250.setText(str(self.total_p92))
        self.label_254.setText(str(self.total_p95))
        self.label_294.setText(str(self.total_oils))

        self.label_185.setText(str(self.solar_price))
        self.label_247.setText(str(self.p80_price))
        self.label_251.setText(str(self.p92_price))
        self.label_255.setText(str(self.p95_price))

        self.label_184.setText(str(self.solar_price * self.total_solar))
        self.label_244.setText(str(self.p80_price * self.total_p80))
        self.label_248.setText(str(self.p92_price * self.total_p92))
        self.label_252.setText(str(self.p95_price * self.total_p95))

        self.label_292.setText(str(self.total_oils_money))

        self.total1 = (
            (self.solar_price * self.total_solar)
            + (self.p80_price * self.total_p80)
            + (self.p92_price * self.total_p92)
            + (self.p95_price * self.total_p95)
            + self.total_oils_money
        )
        self.label_288.setText(str(self.total1))

        sql = " SELECT total FROM coupons WHERE date=%s"
        data = (selected_date,)
        mycursor.execute(sql, data)
        total_bons = mycursor.fetchall()
        self.bons_Quantity = len(total_bons)
        self.total_bons = self.sum_of_numbers(total_bons)

        sql = " SELECT Amount FROM expenses WHERE date=%s"
        data = (selected_date,)
        mycursor.execute(sql, data)
        total_Expenses = mycursor.fetchall()
        self.Expenses_Quantity = len(total_Expenses)
        self.total_Expenses = self.sum_of_numbers(total_Expenses)

        sql = " SELECT Amount FROM creditCustomer WHERE date=%s"
        data = (selected_date,)
        mycursor.execute(sql, data)
        total_Term_Clients = mycursor.fetchall()
        self.Term_Clients_Quantity = len(total_Term_Clients)
        self.total_Term_Clients = self.sum_of_numbers(total_Term_Clients)

        self.label_286.setText(str(self.bons_Quantity))
        self.label_282.setText(str(self.Term_Clients_Quantity))
        self.label_258.setText(str(self.Expenses_Quantity))

        self.label_284.setText(str(self.total_bons))
        self.label_280.setText(str(self.total_Term_Clients))
        self.label_256.setText(str(self.total_Expenses))

        self.total2 = self.total_bons + self.total_Expenses + self.total_Term_Clients
        self.label_276.setText(str(self.total2))

        self.safe = self.total1 - self.total2
        self.label_272.setText(str(self.safe))

        self.last_safe = (self.safe)
        self.label_260.setText(str(self.last_safe))

    def Export_yawmet_al5zena(self):
        self.waiting_frame_start()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        self.wb_export_yawmet_al5zena = Workbook(
            os.path.join(cwd, "reports", f"{selected_date} تقرير يوميه الخزينه.xlsx")
        )
        self.export_yawmet_al5zena_sheet = self.wb_export_yawmet_al5zena.add_worksheet()

        self.export_yawmet_al5zena_sheet.write(0, 0, "البيان")
        self.export_yawmet_al5zena_sheet.write(0, 1, "الكميه")
        self.export_yawmet_al5zena_sheet.write(0, 2, "السعر")
        self.export_yawmet_al5zena_sheet.write(0, 3, "المبلغ")

        # export
        self.export_yawmet_al5zena_sheet.write(1, 0, "سولار")
        self.export_yawmet_al5zena_sheet.write(1, 1, str(self.total_solar))
        self.export_yawmet_al5zena_sheet.write(1, 2, str(self.solar_price))
        self.export_yawmet_al5zena_sheet.write(
            1, 3, str(self.solar_price * self.total_solar)
        )

        self.export_yawmet_al5zena_sheet.write(2, 0, "بنزين 80")
        self.export_yawmet_al5zena_sheet.write(2, 1, str(self.total_p80))
        self.export_yawmet_al5zena_sheet.write(2, 2, str(self.p80_price))
        self.export_yawmet_al5zena_sheet.write(
            2, 3, str(self.p80_price * self.total_p80)
        )

        self.export_yawmet_al5zena_sheet.write(3, 0, "بنزين 92")
        self.export_yawmet_al5zena_sheet.write(3, 1, str(self.total_p92))
        self.export_yawmet_al5zena_sheet.write(3, 2, str(self.p92_price))
        self.export_yawmet_al5zena_sheet.write(
            3, 3, str(self.p92_price * self.total_p92)
        )

        self.export_yawmet_al5zena_sheet.write(4, 0, "بنزين 95")
        self.export_yawmet_al5zena_sheet.write(4, 1, str(self.total_p95))
        self.export_yawmet_al5zena_sheet.write(4, 2, str(self.p95_price))
        self.export_yawmet_al5zena_sheet.write(
            4, 3, str(self.p95_price * self.total_p95)
        )

        self.export_yawmet_al5zena_sheet.write(5, 0, "زيوت")
        self.export_yawmet_al5zena_sheet.write(5, 1, str(self.total_oils))
        self.export_yawmet_al5zena_sheet.write(5, 2, "-")
        self.export_yawmet_al5zena_sheet.write(5, 3, str(self.total_oils_money))

        self.export_yawmet_al5zena_sheet.write(6, 0, "الاجمالي")
        self.export_yawmet_al5zena_sheet.write(6, 1, "-")
        self.export_yawmet_al5zena_sheet.write(6, 2, "-")
        self.export_yawmet_al5zena_sheet.write(6, 3, str(self.total1))

        self.export_yawmet_al5zena_sheet.write(7, 0, "بونات")
        self.export_yawmet_al5zena_sheet.write(7, 1, str(self.bons_Quantity))
        self.export_yawmet_al5zena_sheet.write(7, 2, "-")
        self.export_yawmet_al5zena_sheet.write(7, 3, str(self.total_bons))

        self.export_yawmet_al5zena_sheet.write(8, 0, "عملاء اجله")
        self.export_yawmet_al5zena_sheet.write(8, 1, str(self.Term_Clients_Quantity))
        self.export_yawmet_al5zena_sheet.write(8, 2, "-")
        self.export_yawmet_al5zena_sheet.write(8, 3, str(self.total_Term_Clients))

        self.export_yawmet_al5zena_sheet.write(9, 0, "المصاريف")
        self.export_yawmet_al5zena_sheet.write(9, 1, str(self.Expenses_Quantity))
        self.export_yawmet_al5zena_sheet.write(9, 2, "-")
        self.export_yawmet_al5zena_sheet.write(9, 3, str(self.total_Expenses))

        self.export_yawmet_al5zena_sheet.write(10, 0, "الاجمالي")
        self.export_yawmet_al5zena_sheet.write(10, 1, "-")
        self.export_yawmet_al5zena_sheet.write(10, 2, "-")
        self.export_yawmet_al5zena_sheet.write(10, 3, str(self.total2))

        self.export_yawmet_al5zena_sheet.write(11, 0, "الصافي")
        self.export_yawmet_al5zena_sheet.write(11, 1, "-")
        self.export_yawmet_al5zena_sheet.write(11, 2, "-")
        self.export_yawmet_al5zena_sheet.write(11, 3, str(self.safe))


        self.wb_export_yawmet_al5zena.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## --------------- حركةالخزينة ---------------##
    def Treasury_Movement_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("حركةالخزينة")
        try:
            self.tabWidget.setCurrentIndex(8)
            self.get_byan()
            self.show_data_mkbodat(str(self.comboBox_12.currentText()))
            self.show_data_mdfo3at(str(self.comboBox_15.currentText()))
            self.get_data_byan()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def combo_mdfo3at_Changed(self):
        self.show_data_mdfo3at(str(self.comboBox_15.currentText()))

    def combo_mkbodat_Changed(self):
        self.show_data_mkbodat(str(self.comboBox_12.currentText()))

    def get_byan(self):
        sql = " SELECT name FROM statement"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.comboBox_12.clear()
        self.comboBox_15.clear()
        for c in range(len(result)):
            self.comboBox_12.addItem(result[c][0])
            self.comboBox_15.addItem(result[c][0])

    def add_mkbodat(self):
        self.waiting_frame_start()
        try:
            Statement = str(self.comboBox_12.currentText())
            sand = str(self.lineEdit_34.text())
            money = float(self.doubleSpinBox_7.value())
            Type = "مقبوضات"

            sql = "INSERT INTO CashMovement(date,type,bond,Amount) VALUES(%s,%s,%s,%s)"
            data = (selected_date, Type, sand, money)
            mycursor.execute(sql, data)
            myconn.commit()
            
            id_cm = mycursor.lastrowid
            
            sql = "INSERT INTO CM_has_S(id_cm,name_S) VALUES(%s,%s)"
            data = (id_cm, Statement)
            mycursor.execute(sql, data)
            myconn.commit()

            self.show_data_mkbodat(Statement)
            self.lineEdit_34.setText("")
            self.doubleSpinBox_7.setValue(0)
            self.waiting_frame_end()
            self.Message("تم الاضافه بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def add_mdfo3at(self):
        self.waiting_frame_start()
        try:
            Statement = str(self.comboBox_15.currentText())
            sand = str(self.lineEdit_36.text())
            money = float(self.doubleSpinBox_8.value())
            Type = "مدفوعات"

            sql = "INSERT INTO CashMovement(date,type,bond,Amount) VALUES(%s,%s,%s,%s)"
            data = (selected_date, Type, sand, money)
            mycursor.execute(sql, data)
            myconn.commit()
            
            id_cm = mycursor.lastrowid
            
            sql = "INSERT INTO CM_has_S(id_cm,name_S) VALUES(%s,%s)"
            data = (id_cm, Statement)
            mycursor.execute(sql, data)
            myconn.commit()

            self.show_data_mdfo3at(Statement)
            self.lineEdit_36.setText("")
            self.doubleSpinBox_8.setValue(0)
            self.waiting_frame_end()
            self.Message("تم الاضافه بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def show_data_mkbodat(self, Statement):
        self.tableWidget_3.clear()
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        self.tableWidget_3.setColumnHidden(0, True)
        self.tableWidget_3.setHorizontalHeaderLabels(
            ["id", "البيان", "السند", "المبلغ", ""]
        )
        Type = "مقبوضات"

        sql = """
                SELECT 
                    cm.id,
                    s.name,
                    cm.bond,
                    cm.Amount
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.date = %s
                    AND cm.type = %s
                    AND s.name = %s;
                """
        data = (selected_date, Type, Statement)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_3.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            self.pushButton = QPushButton(self.tableWidget_3)
            self.pushButton.setObjectName(f"pushButton_del_mkbodat={row}")
            self.pushButton.setEnabled(True)
            self.pushButton.setMinimumSize(QSize(35, 35))
            self.pushButton.setMaximumSize(QSize(35, 35))
            self.pushButton.clicked.connect(lambda: self.delete_mkbodat())
            self.pushButton.setText("×")
            self.tableWidget_3.setCellWidget(row, column, self.pushButton)

            row_position = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_position)
        self.show_total_mkbodat(Statement)

    def delete_mkbodat(self):
        self.waiting_frame_start()
        try:
            clicked_row = self.tableWidget_3.currentRow()
            if clicked_row == -1:
                return
            cm_id = int(self.tableWidget_3.item(clicked_row, 0).text())
            
            sql = """
                SELECT 
                    cm.bond as bond,
                    cm.Amount as amount,
                    s.name as name
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.id = %s;
                """
            data = (cm_id,)
            mycursor.execute(sql, data)
            result = mycursor.fetchone()
            
            sql_delete_cm_has_s = "DELETE FROM CM_has_S WHERE id_cm = %s"
            data = (cm_id,)
            mycursor.execute(sql_delete_cm_has_s, data)
            myconn.commit()

            sql_delete_cash_movement = "DELETE FROM CashMovement WHERE id = %s"
            data = (cm_id,)
            mycursor.execute(sql_delete_cash_movement, data)
            myconn.commit()
            
            ss = result[0]
            s = result[2]
            m = result[1]
            
            self.move(
                f'حذف سند "{s}" الذي مبلغه {m} من البيان {ss} في مقبوضات حركه الخزينه'
            )

            self.show_data_mkbodat(str(self.comboBox_12.currentText()))
            self.waiting_frame_end()
            self.Message("تم الحذف بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def show_data_mdfo3at(self, Statement):
        self.tableWidget_846.clear()
        self.tableWidget_846.setRowCount(0)
        self.tableWidget_846.insertRow(0)
        self.tableWidget_846.setColumnHidden(0, True)
        self.tableWidget_846.setHorizontalHeaderLabels(
            ["id", "البيان", "السند", "المبلغ", ""]
        )
        Type = "مدفوعات"

        sql = """
                SELECT 
                    cm.id,
                    s.name,
                    cm.bond,
                    cm.Amount
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.date = %s
                    AND cm.type = %s
                    AND s.name = %s;
                """
        data = (selected_date, Type, Statement)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_846.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_846.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            self.pushButton = QPushButton(self.tableWidget_846)
            self.pushButton.setObjectName(f"pushButton_del_mdfo3at={row}")
            self.pushButton.setEnabled(True)
            self.pushButton.setMinimumSize(QSize(35, 35))
            self.pushButton.setMaximumSize(QSize(35, 35))
            self.pushButton.clicked.connect(lambda: self.delete_mdfo3at())
            self.pushButton.setText("×")
            self.tableWidget_846.setCellWidget(row, column, self.pushButton)

            row_position = self.tableWidget_846.rowCount()
            self.tableWidget_846.insertRow(row_position)
        self.show_total_mdfo3at(Statement)

    def delete_mdfo3at(self):
        self.waiting_frame_start()
        try:
            clicked_row = self.tableWidget_846.currentRow()
            if clicked_row == -1:
                return
            cm_id = int(self.tableWidget_846.item(clicked_row, 0).text())

            sql = """
                SELECT 
                    cm.bond as bond,
                    cm.Amount as amount,
                    s.name as name
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.id = %s;
                """
            data = (cm_id,)
            mycursor.execute(sql, data)
            result = mycursor.fetchone()
            
            sql_delete_cm_has_s = "DELETE FROM CM_has_S WHERE id_cm = %s"
            data = (cm_id,)
            mycursor.execute(sql_delete_cm_has_s, data)
            myconn.commit()

            sql_delete_cash_movement = "DELETE FROM CashMovement WHERE id = %s"
            data = (cm_id,)
            mycursor.execute(sql_delete_cash_movement, data)
            myconn.commit()
            
            ss = str(result[0])
            s = str(result[2])
            m = str(result[1])
            self.move(
                f'حذف سند "{s}" الذي مبلغه {m} من البيان {ss} في مدفوعات حركه الخزينه'
            )

            self.show_data_mdfo3at(str(self.comboBox_15.currentText()))
            self.waiting_frame_end()
            self.Message("تم الحذف بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def show_total_mkbodat(self, Statement):
        sql = """
                SELECT 
                    cm.Amount
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.date = %s
                    AND cm.type = %s
                    AND s.name = %s;
                """
        data = (selected_date, "مقبوضات", Statement)
        mycursor.execute(sql, data)
        tmoney = mycursor.fetchall()
        tmoney = self.sum_of_numbers(tmoney)
        self.doubleSpinBox_9.setValue(tmoney)

    def show_total_mdfo3at(self, Statement):
        sql = """
                SELECT 
                    cm.Amount
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.date = %s
                    AND cm.type = %s
                    AND s.name = %s;
                """
        data = (selected_date, "مدفوعات", Statement)
        mycursor.execute(sql, data)
        tmoney = mycursor.fetchall()
        tmoney = self.sum_of_numbers(tmoney)
        self.doubleSpinBox_10.setValue(tmoney)

    def add_byan(self):
        self.waiting_frame_start()
        try:
            statement = str(self.lineEdit_43.text())
            if statement == "":
                self.waiting_frame_end()
                self.Message("يوجد حقول فارغه", False, 3)
                return
            else:
                sql = " SELECT * FROM statement WHERE name=%s "
                data = (statement,)
                mycursor.execute(sql, data)
                result = mycursor.fetchone()
                if result == [] or result == None:
                    sql = "INSERT INTO statement (name) VALUES(%s)"
                    data = (statement,)
                    mycursor.execute(sql, data)
                    myconn.commit()
                    self.get_data_byan()
                    self.lineEdit_43.setText("")

                    self.waiting_frame_end()
                    self.Message("تم الاضافه بنجاح", True, 3)
                else:
                    self.waiting_frame_end()
                    self.Message("هذا البيان موجود بلفعل", False, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def get_data_byan(self):
        sql = " SELECT name FROM statement"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.comboBox_18.clear()
        for c in range(len(result)):
            self.comboBox_18.addItem(result[c][0])

    def del_byan(self):
        self.waiting_frame_start()
        try:
            name = str(self.comboBox_18.currentText())

            sql = "DELETE FROM statement WHERE name=%s"
            data = (name,)
            mycursor.execute(sql, data)
            myconn.commit()

            self.get_data_byan()
            self.move(f"حذف البيان {name}")
            self.waiting_frame_end()
            self.Message("تم الحذف بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def Export_mkbodat(self):
        self.waiting_frame_start()
        Type = "مقبوضات"
        sql = """
            SELECT 
                cm.id,
                s.name AS statement,
                cm.bond,
                cm.Amount
            FROM 
                CashMovement cm
            JOIN 
                CM_has_S chs ON cm.id = chs.id_cm
            JOIN 
                statement s ON chs.name_S = s.name
            WHERE 
                cm.date = %s
                AND cm.type = %s
            ORDER BY 
                s.name;
            """
        data = (selected_date, Type)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd,
                "reports",
                f"{selected_date} تقرير مقبوضات حركه الخزينه .xlsx",
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "البيان")
        sheet.write(0, 1, "المبلغ")
        sheet.write(0, 2, "السند")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    def Export_mdfo3at(self):
        self.waiting_frame_start()
        Type = "مدفوعات"
        sql = """
            SELECT 
                cm.id,
                s.name AS statement,
                cm.bond,
                cm.Amount
            FROM 
                CashMovement cm
            JOIN 
                CM_has_S chs ON cm.id = chs.id_cm
            JOIN 
                statement s ON chs.name_S = s.name
            WHERE 
                cm.date = %s
                AND cm.type = %s
            ORDER BY 
                s.name;
            """
        data = (selected_date, Type)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd,
                "reports",
                f"{selected_date} تقرير مدفوعات حركه الخزينه .xlsx",
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "البيان")
        sheet.write(0, 1, "المبلغ")
        sheet.write(0, 2, "السند")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## --------------  القيد ----------------##
    def ked_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("قيد يومي")
        try:
            self.tabWidget.setCurrentIndex(9)

            sql = " SELECT name FROM statement"
            mycursor.execute(sql)
            statement_names = mycursor.fetchall()
            self.len_data_in_ked = len(statement_names)

            self.clear_layout(self.verticalLayout_11)
            self.clear_layout(self.verticalLayout_12)

            c = 0
            for name in statement_names:
                sql = """
                SELECT 
                    cm.bond,
                    cm.Amount
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.date = %s
                    AND cm.type = %s
                    AND s.name = %s;
                """
                data = (selected_date, "مقبوضات", name[0])
                mycursor.execute(sql, data)
                result = mycursor.fetchall()
                self.verticalLayout_11.addWidget(
                    comp().main_frame_kad(
                        selected_date, c, str(name[0]), "مقبوضات", result
                    )
                )
                c = c + 1

            for name in statement_names:
                sql = """
                SELECT 
                    cm.bond,
                    cm.Amount
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.date = %s
                    AND cm.type = %s
                    AND s.name = %s;
                """
                data = (selected_date, "مدفوعات", name[0])
                mycursor.execute(sql, data)
                result = mycursor.fetchall()
                self.verticalLayout_12.addWidget(
                    comp().main_frame_kad(
                        selected_date, c, str(name[0]), "مدفوعات", result
                    )
                )
                c = c + 1
            self.waiting_frame_end()
        except :
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                clear_layout(item.layout())

    def Export_ked(self):
        self.waiting_frame_start()
        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd,
                "reports",
                f"{selected_date} تقرير القيد .xlsx",
            )
        )
        sheet = wb.add_worksheet()

        sql = " SELECT name FROM statement"
        mycursor.execute(sql)
        statement_names = mycursor.fetchall()

        sheet.write(1, 0, "من مذكورين")

        row_number = 2
        for name in statement_names:
            sql = """
                SELECT 
                    cm.bond,
                    cm.Amount
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.date = %s
                    AND cm.type = %s
                    AND s.name = %s;
                """
            data = (selected_date, "مقبوضات", name[0])
            mycursor.execute(sql, data)
            data = mycursor.fetchall()
            sheet.write(row_number, 0, str(name[0]))
            row_number += 1
            for row in data:
                column_number = 0
                for item in row:
                    sheet.write(row_number, column_number, str(item))
                    column_number += 1
                row_number += 1

        row_number += 1
        sheet.write(row_number, 0, "الي مذكورين")
        row_number += 1

        for name in statement_names:
            sql = """
                SELECT 
                    cm.bond,
                    cm.Amount
                FROM 
                    CashMovement cm
                JOIN 
                    CM_has_S chs ON cm.id = chs.id_cm
                JOIN 
                    statement s ON chs.name_S = s.name
                WHERE 
                    cm.date = %s
                    AND cm.type = %s
                    AND s.name = %s;
                """
            data = (selected_date, "مدفوعات", name[0])
            mycursor.execute(sql, data)
            data = mycursor.fetchall()
            sheet.write(row_number, 0, str(name[0]))
            row_number += 1
            for row in data:
                column_number = 0
                for item in row:
                    sheet.write(row_number, column_number, str(item))
                    column_number += 1
                row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## ---------------  الموظفين ---------------##
    ## العمال
    def mwzfen_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("الموظفين")
        try:
            self.tabWidget.setCurrentIndex(10)
            self.auto_complete_emp()
            self.auto_complete_user()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def add_emp(self):
        self.waiting_frame_start()
        try:
            if (
                self.lineEdit_13.text().isdigit()
                and self.lineEdit_14.text().isdigit()
                and self.lineEdit_22.text().isdigit()
            ):
                name = str(self.lineEdit_12.text())
                Nid = str(self.lineEdit_13.text())
                mobile_num = str(self.lineEdit_14.text())
                job = str(self.lineEdit_15.text())
                salary = str(self.lineEdit_22.text())
                if (
                    name == ""
                    or Nid == ""
                    or mobile_num == ""
                    or job == ""
                    or str(salary) == ""
                ):
                    self.waiting_frame_end()
                    self.Message("يوجد حقول فارغه", False, 3)
                    return
                else:
                    if len(Nid) == 14:
                        sql = " SELECT * FROM Employee WHERE nationalID = %s "
                        data = (Nid,)
                        mycursor.execute(sql, data)
                        result = mycursor.fetchone()
                        if result == [] or result == None:
                            sql = "INSERT INTO Employee(name,nationalID,phoneNumber,job,salary) VALUES(%s,%s,%s,%s,%s)"
                            data = (name, Nid, mobile_num, job, salary)
                            mycursor.execute(sql, data)
                            myconn.commit()

                            self.lineEdit_12.setText("")
                            self.lineEdit_13.setText("")
                            self.lineEdit_14.setText("")
                            self.lineEdit_15.setText("")
                            self.lineEdit_22.setText("")
                            self.auto_complete_emp()
                            self.waiting_frame_end()
                            self.Message("تم الاضافه بنجاح", True, 3)
                        else:
                            self.waiting_frame_end()
                            self.Message("هذا العامل موجود بلفعل", False, 3)
                    else:
                        self.waiting_frame_end()
                        self.Message("يرجي ادخال الرقم القومي صحيحه", False, 3)
                        return
            else:
                self.waiting_frame_end()
                self.Message("يرجي ادخال بيانات صحيحه", False, 3)
                return
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def search_emp(self):
        self.waiting_frame_start()
        self.emp_id = -1
        self.emp_name = self.lineEdit_16.text()

        sql = " SELECT id,name,nationalID,phoneNumber,job,salary FROM Employee WHERE name=%s "
        data = (self.emp_name,)
        mycursor.execute(sql, data)
        result = mycursor.fetchone()
        if result == [] or result == None:
            self.waiting_frame_end()
            return
        else:
            self.lineEdit_17.setText(str(result[1]))
            self.lineEdit_18.setText(str(result[2]))
            self.lineEdit_19.setText(str(result[3]))
            self.lineEdit_20.setText(str(result[4]))
            self.lineEdit_21.setText(str(result[5]))
            self.emp_id = result[0]
            self.pushButton_45.setEnabled(True)
            self.pushButton_40.setEnabled(True)
            self.waiting_frame_end()

    def update_emp(self):
        self.waiting_frame_start()
        try:
            name = str(self.lineEdit_17.text())
            Nid = str(self.lineEdit_18.text())
            mobile_num = str(self.lineEdit_19.text())
            job = str(self.lineEdit_20.text())
            salary = int(self.lineEdit_21.text())

            sql = "UPDATE Employee SET name = %s , nationalID = %s, phoneNumber  = %s, job  = %s,salary  = %s WHERE id=%s"
            data = (name, Nid, mobile_num, job, salary, self.emp_id)
            mycursor.execute(sql, data)
            myconn.commit()

            self.lineEdit_17.setText("")
            self.lineEdit_18.setText("")
            self.lineEdit_19.setText("")
            self.lineEdit_20.setText("")
            self.lineEdit_21.setText("")
            self.auto_complete_emp()
            self.pushButton_45.setEnabled(False)
            self.pushButton_40.setEnabled(False)
            self.emp_id = -1
            self.waiting_frame_end()
            self.Message("تم تعديل بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def delete_emp(self):
        self.waiting_frame_start()
        try:
            sql = "DELETE FROM Employee WHERE id=%s"
            data = (self.emp_id,)
            mycursor.execute(sql, data)
            myconn.commit()

            self.lineEdit_17.setText("")
            self.lineEdit_18.setText("")
            self.lineEdit_19.setText("")
            self.lineEdit_20.setText("")
            self.lineEdit_21.setText("")
            self.auto_complete_emp()
            self.pushButton_45.setEnabled(False)
            self.pushButton_40.setEnabled(False)
            self.emp_id = -1
            self.waiting_frame_end()
            self.Message("تم الحذف بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def auto_complete_emp(self):
        emp_list.clear()
        sql = " SELECT name FROM Employee"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for names in result:
            emp_list.append(names[0])

        lineedit = self.lineEdit_16
        completer = QCompleter()
        lineedit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete_em(model)

    def Auto_Complete_em(self, model):
        model.setStringList(emp_list)

    ## المستخدمين
    def add_user(self):
        self.waiting_frame_start()
        try:
            username = str(self.lineEdit_26.text())
            pas = str(self.lineEdit_27.text())
            user_type = str(self.comboBox_11.currentText())
            if username == "" or pas == "":
                self.waiting_frame_end()
                self.Message("يوجد حقول فارغه", False, 3)
                return
            else:
                sql = " SELECT * FROM UserAccount WHERE UserName = %s "
                data = (username,)
                mycursor.execute(sql, data)
                result = mycursor.fetchone()
                if result == [] or result == None:
                    sql = "INSERT INTO UserAccount(UserName,Password,Role) VALUES(%s,%s,%s)"
                    data = (username, pas, user_type)
                    mycursor.execute(sql, data)
                    myconn.commit()

                    self.lineEdit_26.setText("")
                    self.lineEdit_27.setText("")
                    self.auto_complete_user()
                    self.waiting_frame_end()
                    self.Message("تم الاضافه بنجاح", True, 3)
                else:
                    self.waiting_frame_end()
                    self.Message(" اسم المستخدم موجود بلفعل", False, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def search_user(self):
        self.waiting_frame_start()
        self.user_name = self.lineEdit_23.text()
        self.user_id = -1

        sql = (
            " SELECT UserName,Password,Role FROM UserAccount WHERE UserName=%s "
        )
        data = (self.user_name,)
        mycursor.execute(sql, data)
        result = mycursor.fetchone()
        if result == [] or result == None:
            self.waiting_frame_end()
            return
        else:
            self.lineEdit_29.setText(str(result[0]))
            self.lineEdit_33.setText(str(result[1]))
            self.user_id = result[0]
            if str(result[2]) == "ادمن":
                self.comboBox_13.setCurrentIndex(0)
            if str(result[2]) == "محاسب":
                self.comboBox_13.setCurrentIndex(1)
            if str(result[2]) == "عامل":
                self.comboBox_13.setCurrentIndex(2)
            self.pushButton_44.setEnabled(True)
            self.pushButton_43.setEnabled(True)
            self.waiting_frame_end()

    def update_user(self):
        self.waiting_frame_start()
        try:
            username = str(self.lineEdit_29.text())
            pas = str(self.lineEdit_33.text())
            user_type = str(self.comboBox_13.currentText())

            sql = "UPDATE UserAccount SET Password  = %s, Role  = %s WHERE UserName=%s"
            data = (username, pas, user_type, self.user_id)
            mycursor.execute(sql, data)
            myconn.commit()

            self.lineEdit_29.setText("")
            self.lineEdit_33.setText("")
            self.user_id = -1
            self.auto_complete_user()
            self.pushButton_44.setEnabled(False)
            self.pushButton_43.setEnabled(False)
            self.waiting_frame_end()
            self.Message("تم تعديل بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def delete_user(self):
        self.waiting_frame_start()
        try:
            sql = "DELETE FROM UserAccount WHERE UserName=%s"
            data = (self.user_id,)
            mycursor.execute(sql, data)
            myconn.commit()

            self.lineEdit_29.setText("")
            self.lineEdit_33.setText("")
            self.auto_complete_user()
            self.pushButton_44.setEnabled(False)
            self.pushButton_43.setEnabled(False)
            self.user_id = -1
            self.waiting_frame_end()
            self.Message("تم الحذف بنجاح", True, 3)
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def auto_complete_user(self):
        user_list.clear()
        sql = " SELECT UserName FROM UserAccount"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for names in result:
            user_list.append(names[0])

        lineedit = self.lineEdit_23
        completer = QCompleter()
        lineedit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete_user(model)

    def Auto_Complete_user(self, model):
        model.setStringList(user_list)

    ## ---------------  حركه النظام  ---------------##
    def System_Move_clicked(self):
        self.waiting_frame_start()
        self.pushButton_14.setText("حركه النظام")
        try:
            self.tabWidget.setCurrentIndex(11)
            self.get_all_users()
            self.show_System_Moves()
            self.waiting_frame_end()
        except:
            self.waiting_frame_end()
            self.Message("يوجد مشكله في الانترنت", False, 3)

    def get_all_users(self):
        sql = " SELECT UserName FROM UserAccount"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.comboBox_19.clear()
        for c in range(len(result)):
            self.comboBox_19.addItem(result[c][0])


    def show_System_Moves(self):
        self.tableWidget_19.clear()
        self.tableWidget_19.setRowCount(0)
        self.tableWidget_19.insertRow(0)
        self.tableWidget_19.setHorizontalHeaderLabels(
            ["في تاريخ", "الوقت", "اسم المستخدم", "النوع", "النظام", "الحركه"]
        )

        sql = """
            SELECT sa.modDate, sa.time, ua.userName, ua.role AS user_type, sa.softwareType AS sys_type, sa.activity AS move
            FROM SystemActivity sa
            JOIN UserA_Has_SActivity uas ON sa.id = uas.a_id
            JOIN UserAccount ua ON uas.UserName = ua.userName
            WHERE sa.date = %s
            """
        data = (selected_date,)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_19.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_19.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            row_position = self.tableWidget_19.rowCount()
            self.tableWidget_19.insertRow(row_position)

    def show_System_Moves_w_user(self):
        user = str(self.comboBox_19.currentText())

        self.tableWidget_19.clear()
        self.tableWidget_19.setRowCount(0)
        self.tableWidget_19.insertRow(0)
        self.tableWidget_19.setHorizontalHeaderLabels(
            ["في تاريخ", "الوقت", "اسم المستخدم", "النوع", "النظام", "الحركه"]
        )

        sql =  """
        SELECT sa.modDate AS ondate, sa.time, ua.userName AS username, ua.role AS user_type, sa.softwareType AS sys_type, sa.activity AS move
        FROM SystemActivity sa
        JOIN UserA_Has_SActivity uas ON sa.id = uas.a_id
        JOIN UserAccount ua ON uas.UserName = ua.userName
        WHERE sa.date = %s AND ua.userName = %s
        """
        data = (selected_date, user)
        mycursor.execute(sql, data)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_19.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_19.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            row_position = self.tableWidget_19.rowCount()
            self.tableWidget_19.insertRow(row_position)

    def Export_System_Move(self):
        self.waiting_frame_start()
        sql = """
                SELECT sa.modDate AS ondate, sa.time, ua.userName AS username, ua.role AS user_type, sa.softwareType AS sys_type, sa.activity AS move
                FROM SystemActivity sa
                JOIN UserA_Has_SActivity uas ON sa.id = uas.a_id
                JOIN UserAccount ua ON uas.UserName = ua.userName
                WHERE sa.date = %s
                ORDER BY ua.userName
                """
        data = (selected_date,)
        mycursor.execute(sql, data)
        data = mycursor.fetchall()

        py_file_path = sys.argv[0]
        cwd = os.path.dirname(py_file_path)

        if not os.path.exists(os.path.join(cwd, "reports")):
            os.makedirs(os.path.join(cwd, "reports"))

        wb = Workbook(
            os.path.join(
                cwd,
                "reports",
                f"{selected_date} تقرير حركه النظام .xlsx",
            )
        )
        sheet = wb.add_worksheet()

        sheet.write(0, 0, "في تاريخ")
        sheet.write(0, 1, "الوقت")
        sheet.write(0, 2, "اسم المستخدم")
        sheet.write(0, 3, "نوع المستخدم")
        sheet.write(0, 4, "نوع النظام")
        sheet.write(0, 5, "الحركه")

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.waiting_frame_end()
        self.Message("تم حفظ التقرير بنجاح", True, 3)

    ## --------------- all data ---------------##
    def show_all_emp_in_table(self):
        self.tabWidget.setCurrentIndex(15)
        self.tableWidget_22.clear()
        self.tableWidget_22.setRowCount(0)
        self.tableWidget_22.insertRow(0)
        self.tableWidget_22.setColumnHidden(0, True)
        self.tableWidget_22.setHorizontalHeaderLabels(
            ["id", "الاسم", "الرقم القومي", "رقم الهاتف", "الوظيفه", "المرتب"]
        )

        sql = " SELECT * FROM Employee"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_22.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_22.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            row_position = self.tableWidget_22.rowCount()
            self.tableWidget_22.insertRow(row_position)

    def show_all_user_in_table(self):
        self.tabWidget.setCurrentIndex(16)
        self.tableWidget_28.clear()
        self.tableWidget_28.setRowCount(0)
        self.tableWidget_28.insertRow(0)
        self.tableWidget_28.setColumnHidden(0, True)
        self.tableWidget_28.setHorizontalHeaderLabels(
            ["id", "اسم المستخدم", "كلمه السر", "النوع"]
        )

        sql = " SELECT UserName,UserName,Password,Role FROM UserAccount"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_28.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_28.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            row_position = self.tableWidget_28.rowCount()
            self.tableWidget_28.insertRow(row_position)

    def show_all_cl_in_table(self):
        self.tabWidget.setCurrentIndex(17)
        self.tableWidget_29.clear()
        self.tableWidget_29.setRowCount(0)
        self.tableWidget_29.insertRow(0)
        self.tableWidget_29.setColumnHidden(0, True)
        self.tableWidget_29.setHorizontalHeaderLabels(
            ["id", "الاسم", "الرقم القومي", "رقم الهاتف"]
        )

        sql = " SELECT national_ID,name,national_ID,phone_number FROM customer"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_29.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_29.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            row_position = self.tableWidget_29.rowCount()
            self.tableWidget_29.insertRow(row_position)

    def show_all_oi_in_table(self):
        self.tabWidget.setCurrentIndex(18)
        self.tableWidget_30.clear()
        self.tableWidget_30.setRowCount(0)
        self.tableWidget_30.insertRow(0)
        self.tableWidget_30.setColumnHidden(0, True)
        self.tableWidget_30.setHorizontalHeaderLabels(["id", "الاسم", "السعر"])

        sql = " SELECT oilName,oilName,price FROM oil"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for row, form in enumerate(result):
            for column, item in enumerate(form):
                self.tableWidget_30.setItem(row, column, QTableWidgetItem(str(item)))
                item = self.tableWidget_30.item(row, column)
                item.setTextAlignment(Qt.AlignCenter)
                column += 1
            row_position = self.tableWidget_30.rowCount()
            self.tableWidget_30.insertRow(row_position)


###################################################################################################

###################################################################################################
row_id = -1


class Start_End_YW(QWidget, start_end_yw):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.save_s_e.clicked.connect(self.Handel_save)

    def get_benzen_prices(self):
        try:
            if row_id != -1:
                sql = " SELECT pumpNumber,petrolType,start_code,end_code FROM dailyPumpshift WHERE id=%s"
                data = (row_id,)
                mycursor.execute(sql, data)
                result = mycursor.fetchone()
                self.spinBox_2.setValue(int(result[2]))
                self.spinBox.setValue(int(result[3]))
                self.trumba_number = str(result[0])
                self.trumba_type = str(result[1])
                self.startyw = str(result[2])
                self.endyw = str(result[3])
        except:
            return

    def Handel_save(self):
        window.waiting_frame_start()
        if row_id == -1:
            window.waiting_frame_end()
            return
        else:
            if int(self.spinBox_2.value()) >= int(self.spinBox.value()):
                sql = "UPDATE dailyPumpshift SET start_code =%s WHERE id=%s"
                data = (int(self.spinBox_2.value()), row_id)
                mycursor.execute(sql, data)
                myconn.commit()

                sql = "UPDATE dailyPumpshift SET end_code =%s WHERE id=%s"
                data = (int(self.spinBox.value()), row_id)
                mycursor.execute(sql, data)
                myconn.commit()

                if self.startyw != str(self.spinBox_2.value()):
                    window.move(
                        f"طلمبه رقم {self.trumba_number} {self.trumba_type} تم التعديل البدايه من {self.startyw} الي {str(self.spinBox_2.value())}"
                    )
                if self.endyw != str(self.spinBox.value()):
                    window.move(
                        f"طلمبه رقم {self.trumba_number} {self.trumba_type} تم التعديل النهايه من {self.endyw} الي {str(self.spinBox.value())}"
                    )

                window2.close()
                window.show_data_in_frame_yw()
                window.waiting_frame_end()
                window.Message("تم التعديل بنجاح", True, 3)

            else:
                window.waiting_frame_end()
                window.Message("يجب ان تكون البدايه اكبر من النهايه", False, 3)


###################################################################################################
###################################################################################################
class comp:
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

        self.na2l.setValue(0)
        self.fr2s3r.setValue(0)

        return self.frame

    def sand_and_m_frame_ked(self, n, s, m):
        self.frame = QFrame()
        self.frame.setObjectName(f"frame_sand_m_{n}")
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
            f"gridLayout_sand_m_{n}-{m}-{str(random.random())}"
        )
        self.mbl8 = QLabel(self.frame)
        self.mbl8.setObjectName(f"mbl8_sand_m_{n}-{m}-{str(random.random())}")
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
        self.sand.setObjectName(f"sand_sand_m_{n}-{m}-{str(random.random())}")
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


###################################################################################################


###################################################################################################
class Login(QMainWindow, login):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.login_btn.clicked.connect(self.Handel_Login)

    def Handel_Login(self):
        global username
        global usert
        username = str(self.username.text())
        password = str(self.passw.text())

        sql = " SELECT * FROM userAccount WHERE UserName=%s"
        data = (username,)
        mycursor.execute(sql, data)
        result = mycursor.fetchone()
        if result == None or result == []:
            QMessageBox.information(
                self, "خطاء", "اسم المستخدم او كلمه المرور غير صحيحه"
            )
            return
        else:
            if username == result[0] and password == result[1]:

                
                insertsql = "INSERT INTO loginHistory(date,time,softwareType) VALUES(%s,%s,%s)"
                infodata = (current_date, current_time, "برنامج")
                mycursor.execute(insertsql, infodata)
                myconn.commit()
                
                id_h = mycursor.lastrowid
                
                insertsql = "INSERT INTO userA_has_loginHistory(User_Name,h_id) VALUES(%s,%s)"
                infodata = (username,id_h)
                mycursor.execute(insertsql, infodata)
                myconn.commit()
                

                usert = str(result[2])

                if usert == "محاسب":
                    window.pushButton.setEnabled(False)
                    window.pushButton.hide()
                    window.pushButton_32.setEnabled(False)
                    window.pushButton_32.hide()
                    window.pushButton_7.setEnabled(False)
                    window.pushButton_7.hide()
                    window.start_wi_index_1()
                elif usert == "عامل":
                    window.pushButton_19.setEnabled(False)
                    window.pushButton_19.hide()
                    window.pushButton_58.setEnabled(False)
                    window.pushButton_58.hide()
                    window.pushButton_30.setEnabled(False)
                    window.pushButton_30.hide()
                    window.pushButton.setEnabled(False)
                    window.pushButton.hide()
                    window.pushButton_8.setEnabled(False)
                    window.pushButton_8.hide()
                    window.pushButton_10.setEnabled(False)
                    window.pushButton_10.hide()
                    window.pushButton_11.setEnabled(False)
                    window.pushButton_11.hide()
                    window.pushButton_32.setEnabled(False)
                    window.pushButton_32.hide()
                    window.pushButton_7.setEnabled(False)
                    window.pushButton_7.hide()
                    window.start_wi_index_1()

                self.close()
                window.show()
                window.show_login_history_in_table()
                window.showMaximized()
            else:
                QMessageBox.information(
                    self, "خطاء", "اسم المستخدم او كلمه المرور غير صحيحه"
                )
                return


###################################################################################################


def main():
    global window

    app = QApplication(sys.argv)

    window = MainApp()

    mainwindow = Login()
    mainwindow.show()

    app.exec_()


if __name__ == "__main__":
    main()
