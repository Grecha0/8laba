import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Shedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="8laba",
                                     user="postgres",
                                     password="grecha99",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Четная неделя")

        self.table_gbox1 = QGroupBox("Monday")
        self.table_gbox2 = QGroupBox("Tuesday")
        self.table_gbox3 = QGroupBox("Wednesday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)

        self.shbox1.addWidget(self.table_gbox1)
        self.shbox2.addWidget(self.table_gbox2)
        self.shbox3.addWidget(self.table_gbox3)

        self._create_monday_table()
        self._create_tuesday_table()
        self._create_wednesday_table()


        self.update_shedule_button = QPushButton("Update")
        self.shbox4.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(5)
        self.monday_table.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", ""])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.table_gbox1.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(5)
        self.tuesday_table.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", ""])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.table_gbox2.setLayout(self.mvbox)

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(5)
        self.wednesday_table.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", ""])

        self._update_wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)
        self.table_gbox3.setLayout(self.mvbox)



    def _update_monday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Monday'")
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.monday_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

        self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day = 'Tuesday'")
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.tuesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.tuesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.tuesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.tuesday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.tuesday_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

        self.tuesday_table.resizeRowsToContents()

    def _update_wednesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day = 'Wednesday'")
        records = list(self.cursor.fetchall())

        self.wednesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")

            self.wednesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.wednesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.wednesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.wednesday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.wednesday_table.setCellWidget(i, 4, joinButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

        self.wednesday_table.resizeRowsToContents()

    def _change_day_from_table(self, rowNum, day):
        row = list()
        for i in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, i).text())
            except:
                row.append(None)

        try:
            self.cursor.execute("UPDATE SQL запрос на изменение одной строки в базе данных", (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

    def _update_shedule(self):
        self._update_monday_table()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())

