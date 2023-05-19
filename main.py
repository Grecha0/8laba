import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QDialogButtonBox,
                             QTabWidget, QAbstractScrollArea, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QLineEdit,
                             QTableWidget, QGroupBox, QDialog, QLabel,
                             QTableWidgetItem, QPushButton, QMessageBox)

class ChangeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Record")
        layout = QGridLayout()
        self.text_fields = []
        field_labels = ["time:", "teacher:", "lesson:", "auditorium:", "id(0-5)(6-10)(11-15)(16-20)(21-25)(26-30):"]

        for row, label_text in enumerate(field_labels):
            label = QLabel(label_text)
            line_edit = QLineEdit()
            layout.addWidget(label, row, 0)
            layout.addWidget(line_edit, row, 1)
            self.text_fields.append(line_edit)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons, len(field_labels), 0, 1, 2)
        self.setLayout(layout)

    def get_values(self):
        return [field.text() for field in self.text_fields]

class ChangeDialog2(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change Record2")
        layout2 = QGridLayout()
        self.text_fields2 = []
        field_labels2 = ["Введите id (0-5)(6-10)(11-15)(16-20)(21-25)(26-30) удаляемой строки:"]

        for row, label_text in enumerate(field_labels2):
            label2 = QLabel(label_text)
            line_edit2 = QLineEdit()
            layout2.addWidget(label2, row, 0)
            layout2.addWidget(line_edit2, row, 1)
            self.text_fields2.append(line_edit2)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout2.addWidget(self.buttons, len(field_labels2), 0, 1, 2)
        self.setLayout(layout2)

    def get_values2(self):
        return [field.text2() for field in self.text_fields2]


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Shedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()
        self._create_shedule_tab2()

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
        self.table_gbox4 = QGroupBox("Thursday")
        self.table_gbox5 = QGroupBox("Friday")
        self.table_gbox6 = QGroupBox("Saturday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()
        self.shbox5 = QHBoxLayout()
        self.shbox6 = QHBoxLayout()
        self.shbox7 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)
        self.svbox.addLayout(self.shbox5)
        self.svbox.addLayout(self.shbox6)
        self.svbox.addLayout(self.shbox7)

        self.shbox1.addWidget(self.table_gbox1)
        self.shbox1.addWidget(self.table_gbox2)
        self.shbox3.addWidget(self.table_gbox3)
        self.shbox3.addWidget(self.table_gbox4)
        self.shbox5.addWidget(self.table_gbox5)
        self.shbox5.addWidget(self.table_gbox6)

        self._create_monday_table()
        self._create_tuesday_table()
        self._create_wednesday_table()
        self._create_thursday_table()
        self._create_friday_table()
        self._create_saturday_table()


        self.update_shedule_button = QPushButton("Update")
        self.shbox7.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule_1)

        self.shedule_tab.setLayout(self.svbox)

    def _create_shedule_tab2(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Нечетная неделя")

        self.table_gbox1 = QGroupBox("Monday")
        self.table_gbox2 = QGroupBox("Tuesday")
        self.table_gbox3 = QGroupBox("Wednesday")
        self.table_gbox4 = QGroupBox("Thursday")
        self.table_gbox5 = QGroupBox("Friday")
        self.table_gbox6 = QGroupBox("Saturday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()
        self.shbox4 = QHBoxLayout()
        self.shbox5 = QHBoxLayout()
        self.shbox6 = QHBoxLayout()
        self.shbox7 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox4)
        self.svbox.addLayout(self.shbox5)
        self.svbox.addLayout(self.shbox6)
        self.svbox.addLayout(self.shbox7)

        self.shbox1.addWidget(self.table_gbox1)
        self.shbox1.addWidget(self.table_gbox2)
        self.shbox3.addWidget(self.table_gbox3)
        self.shbox3.addWidget(self.table_gbox4)
        self.shbox5.addWidget(self.table_gbox5)
        self.shbox5.addWidget(self.table_gbox6)

        self._create_monday_table2()
        self._create_tuesday_table2()
        self._create_wednesday_table2()
        self._create_thursday_table2()
        self._create_friday_table2()
        self._create_saturday_table2()

        self.update_shedule_button = QPushButton("Update")
        self.shbox7.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule_2)

        self.shedule_tab.setLayout(self.svbox)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(6)
        self.monday_table.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "",""])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.table_gbox1.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record)

    def _add_record(self):
        row_count = self.monday_table.rowCount()

        self.monday_table.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.monday_table.setItem(row_count, 0, subject_item)
        self.monday_table.setItem(row_count, 1, time_item)
        self.monday_table.setItem(row_count, 2, teacher_item)
        self.monday_table.setItem(row_count, 3, auditorium_item)

        self.monday_table.resizeRowsToContents()

    def _create_monday_table2(self):
        self.monday_table2 = QTableWidget()
        self.monday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table2.setColumnCount(6)
        self.monday_table2.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "",""])

        self._update_monday_table2()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table2)
        self.table_gbox1.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record2)

    def _add_record2(self):
        row_count = self.monday_table2.rowCount()

        self.monday_table2.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.monday_table2.setItem(row_count, 0, subject_item)
        self.monday_table2.setItem(row_count, 1, time_item)
        self.monday_table2.setItem(row_count, 2, teacher_item)
        self.monday_table2.setItem(row_count, 3, auditorium_item)

        self.monday_table2.resizeRowsToContents()



    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(6)
        self.tuesday_table.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "",""])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.table_gbox2.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record3)

    def _add_record3(self):
        row_count = self.tuesday_table.rowCount()

        self.tuesday_table.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.tuesday_table.setItem(row_count, 0, subject_item)
        self.tuesday_table.setItem(row_count, 1, time_item)
        self.tuesday_table.setItem(row_count, 2, teacher_item)
        self.tuesday_table.setItem(row_count, 3, auditorium_item)

        self.tuesday_table.resizeRowsToContents()

    def _create_tuesday_table2(self):
        self.tuesday_table2 = QTableWidget()
        self.tuesday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table2.setColumnCount(6)
        self.tuesday_table2.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "",""])

        self._update_tuesday_table2()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table2)
        self.table_gbox2.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record4)

    def _add_record4(self):
        row_count = self.tuesday_table2.rowCount()

        self.tuesday_table2.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.tuesday_table2.setItem(row_count, 0, subject_item)
        self.tuesday_table2.setItem(row_count, 1, time_item)
        self.tuesday_table2.setItem(row_count, 2, teacher_item)
        self.tuesday_table2.setItem(row_count, 3, auditorium_item)

        self.tuesday_table2.resizeRowsToContents()

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()
        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(6)
        self.wednesday_table.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "",""])

        self._update_wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)
        self.table_gbox3.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record5)

    def _add_record5(self):
        row_count = self.wednesday_table.rowCount()

        self.wednesday_table.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.wednesday_table.setItem(row_count, 0, subject_item)
        self.wednesday_table.setItem(row_count, 1, time_item)
        self.wednesday_table.setItem(row_count, 2, teacher_item)
        self.wednesday_table.setItem(row_count, 3, auditorium_item)

        self.wednesday_table.resizeRowsToContents()

    def _create_wednesday_table2(self):
        self.wednesday_table2 = QTableWidget()
        self.wednesday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table2.setColumnCount(6)
        self.wednesday_table2.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "",""])

        self._update_wednesday_table2()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table2)
        self.table_gbox3.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record6)

    def _add_record6(self):
        row_count = self.wednesday_table2.rowCount()

        self.wednesday_table2.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.wednesday_table2.setItem(row_count, 0, subject_item)
        self.wednesday_table2.setItem(row_count, 1, time_item)
        self.wednesday_table2.setItem(row_count, 2, teacher_item)
        self.wednesday_table2.setItem(row_count, 3, auditorium_item)

        self.wednesday_table2.resizeRowsToContents()

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(6)
        self.thursday_table.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "", ""])

        self._update_thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)
        self.table_gbox4.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record7)

    def _add_record7(self):
        row_count = self.thursday_table.rowCount()

        self.thursday_table.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.thursday_table.setItem(row_count, 0, subject_item)
        self.thursday_table.setItem(row_count, 1, time_item)
        self.thursday_table.setItem(row_count, 2, teacher_item)
        self.thursday_table.setItem(row_count, 3, auditorium_item)

        self.thursday_table.resizeRowsToContents()

    def _create_thursday_table2(self):
        self.thursday_table2 = QTableWidget()
        self.thursday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table2.setColumnCount(6)
        self.thursday_table2.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "" ,""])

        self._update_thursday_table2()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table2)
        self.table_gbox4.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record8)

    def _add_record8(self):
        row_count = self.thursday_table2.rowCount()

        self.thursday_table2.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.thursday_table2.setItem(row_count, 0, subject_item)
        self.thursday_table2.setItem(row_count, 1, time_item)
        self.thursday_table2.setItem(row_count, 2, teacher_item)
        self.thursday_table2.setItem(row_count, 3, auditorium_item)

        self.thursday_table2.resizeRowsToContents()

    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(6)
        self.friday_table.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "", ""])

        self._update_friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)
        self.table_gbox5.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record9)

    def _add_record9(self):
        row_count = self.friday_table.rowCount()

        self.friday_table.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.friday_table.setItem(row_count, 0, subject_item)
        self.friday_table.setItem(row_count, 1, time_item)
        self.friday_table.setItem(row_count, 2, teacher_item)
        self.friday_table.setItem(row_count, 3, auditorium_item)

        self.friday_table.resizeRowsToContents()

    def _create_friday_table2(self):
        self.friday_table2 = QTableWidget()
        self.friday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table2.setColumnCount(6)
        self.friday_table2.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "" ,""])

        self._update_friday_table2()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table2)
        self.table_gbox5.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record10)

    def _add_record10(self):
        row_count = self.friday_table2.rowCount()

        self.friday_table2.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.friday_table2.setItem(row_count, 0, subject_item)
        self.friday_table2.setItem(row_count, 1, time_item)
        self.friday_table2.setItem(row_count, 2, teacher_item)
        self.friday_table2.setItem(row_count, 3, auditorium_item)

        self.friday_table2.resizeRowsToContents()

    def _create_saturday_table(self):
        self.saturday_table = QTableWidget()
        self.saturday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday_table.setColumnCount(6)
        self.saturday_table.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "",""])

        self._update_saturday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.saturday_table)
        self.table_gbox6.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record11)

    def _add_record11(self):
        row_count = self.saturday_table.rowCount()

        self.saturday_table.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.saturday_table.setItem(row_count, 0, subject_item)
        self.saturday_table.setItem(row_count, 1, time_item)
        self.saturday_table.setItem(row_count, 2, teacher_item)
        self.saturday_table.setItem(row_count, 3, auditorium_item)

        self.saturday_table.resizeRowsToContents()

    def _create_saturday_table2(self):
        self.saturday_table2 = QTableWidget()
        self.saturday_table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday_table2.setColumnCount(6)
        self.saturday_table2.setHorizontalHeaderLabels(["Time", "Subject", "Teacher", "Auditorium", "", ""])

        self._update_saturday_table2()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.saturday_table2)
        self.table_gbox6.setLayout(self.mvbox)

        self.add_record_button = QPushButton("Add Record")
        self.mvbox.addWidget(self.add_record_button)
        self.add_record_button.clicked.connect(self._add_record12)

    def _add_record12(self):
        row_count = self.saturday_table2.rowCount()

        self.saturday_table2.insertRow(row_count)

        time_item = QTableWidgetItem("")
        subject_item = QTableWidgetItem("")
        teacher_item = QTableWidgetItem("")
        auditorium_item = QTableWidgetItem("")

        self.saturday_table2.setItem(row_count, 0, subject_item)
        self.saturday_table2.setItem(row_count, 1, time_item)
        self.saturday_table2.setItem(row_count, 2, teacher_item)
        self.saturday_table2.setItem(row_count, 3, auditorium_item)

        self.saturday_table2.resizeRowsToContents()


    def _update_monday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Monday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.monday_table.setCellWidget(i, 4, updateButton)
            self.monday_table.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Monday': self._change_table(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Monday': self._delete_table(num, day))

        self.monday_table.resizeRowsToContents()

    def _update_monday_table2(self):
        self.cursor.execute("SELECT * FROM timetable2 WHERE day='Monday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.monday_table2.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.monday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.monday_table2.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.monday_table2.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.monday_table2.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.monday_table2.setCellWidget(i, 4, updateButton)
            self.monday_table2.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Monday': self._change_table2(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Monday': self._delete_table2(num, day))

        self.monday_table2.resizeRowsToContents()

    def _update_tuesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day = 'Tuesday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.tuesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.tuesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.tuesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.tuesday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.tuesday_table.setCellWidget(i, 4, updateButton)
            self.tuesday_table.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Tuesday': self._change_table3(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Tuesday': self._delete_table3(num, day))

        self.tuesday_table.resizeRowsToContents()

    def _update_tuesday_table2(self):
        self.cursor.execute("SELECT * FROM timetable2 WHERE day = 'Tuesday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.tuesday_table2.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.tuesday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.tuesday_table2.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.tuesday_table2.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.tuesday_table2.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.tuesday_table2.setCellWidget(i, 4, updateButton)
            self.tuesday_table2.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Tuesday': self._change_table4(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Tuesday': self._delete_table4(num, day))

        self.tuesday_table2.resizeRowsToContents()

    def _update_wednesday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day = 'Wednesday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.wednesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.wednesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.wednesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.wednesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.wednesday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.wednesday_table.setCellWidget(i, 4, updateButton)
            self.wednesday_table.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Wednesday': self._change_table5(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Wednesday': self._delete_table5(num, day))

        self.wednesday_table.resizeRowsToContents()

    def _update_wednesday_table2(self):
        self.cursor.execute("SELECT * FROM timetable2 WHERE day = 'Wednesday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.wednesday_table2.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.wednesday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.wednesday_table2.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.wednesday_table2.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.wednesday_table2.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.wednesday_table2.setCellWidget(i, 4, updateButton)
            self.wednesday_table2.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Wednesday': self._change_table6(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Wednesday': self._delete_table6(num, day))

        self.wednesday_table2.resizeRowsToContents()

    def _update_thursday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day = 'Thursday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.thursday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.thursday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.thursday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.thursday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.thursday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.thursday_table.setCellWidget(i, 4, updateButton)
            self.thursday_table.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Thursday': self._change_table7(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Thursday': self._delete_table7(num, day))

        self.thursday_table.resizeRowsToContents()

    def _update_thursday_table2(self):
        self.cursor.execute("SELECT * FROM timetable2 WHERE day = 'Thursday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.thursday_table2.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.thursday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.thursday_table2.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.thursday_table2.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.thursday_table2.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.thursday_table2.setCellWidget(i, 4, updateButton)
            self.thursday_table2.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Thursday': self._change_table8(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Thursday': self._delete_table8(num, day))

        self.thursday_table2.resizeRowsToContents()

    def _update_friday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day = 'Friday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.friday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.friday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.friday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.friday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.friday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.friday_table.setCellWidget(i, 4, updateButton)
            self.friday_table.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Friday': self._change_table9(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Friday': self._delete_table9(num, day))

        self.friday_table.resizeRowsToContents()

    def _update_friday_table2(self):
        self.cursor.execute("SELECT * FROM timetable2 WHERE day = 'Friday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.friday_table2.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.friday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.friday_table2.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.friday_table2.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.friday_table2.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.friday_table2.setCellWidget(i, 4, updateButton)
            self.friday_table2.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Friday': self._change_table10(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Friday': self._delete_table10(num, day))

        self.friday_table2.resizeRowsToContents()

    def _update_saturday_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day = 'Saturday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.saturday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.saturday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.saturday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.saturday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.saturday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.saturday_table.setCellWidget(i, 4, updateButton)
            self.saturday_table.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Saturday': self._change_table11(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Saturday': self._delete_table11(num, day))

        self.saturday_table.resizeRowsToContents()

    def _update_saturday_table2(self):
        self.cursor.execute("SELECT * FROM timetable2 WHERE day = 'Saturday' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.saturday_table2.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            updateButton = QPushButton("Update")
            deleteButton = QPushButton("Delete")

            self.saturday_table2.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.saturday_table2.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.saturday_table2.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.saturday_table2.setItem(i, 3,
                                      QTableWidgetItem(str(r[5])))
            self.saturday_table2.setCellWidget(i, 4, updateButton)
            self.saturday_table2.setCellWidget(i, 5, deleteButton)

            updateButton.clicked.connect(lambda ch, num=i, day='Saturday': self._change_table12(num, day))
            deleteButton.clicked.connect(lambda ch, num=i, day='Saturday': self._delete_table12(num, day))

        self.saturday_table2.resizeRowsToContents()

    def _change_table(self, rowNum, day):
        row = list()
        for i in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table2(self, rowNum, day):
        row = list()
        for i in range(self.monday_table2.columnCount()):
            try:
                row.append(self.monday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table3(self, rowNum, day):
        row = list()
        for i in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table4(self, rowNum, day):
        row = list()
        for i in range(self.tuesday_table2.columnCount()):
            try:
                row.append(self.thursday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table5(self, rowNum, day):
        row = list()
        for i in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table6(self, rowNum, day):
        row = list()
        for i in range(self.wednesday_table2.columnCount()):
            try:
                row.append(self.wednesday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table7(self, rowNum, day):
        row = list()
        for i in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table8(self, rowNum, day):
        row = list()
        for i in range(self.thursday_table2.columnCount()):
            try:
                row.append(self.thursday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table9(self, rowNum, day):
        row = list()
        for i in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table10(self, rowNum, day):
        row = list()
        for i in range(self.friday_table2.columnCount()):
            try:
                row.append(self.friday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table11(self, rowNum, day):
        row = list()
        for i in range(self.saturday_table.columnCount()):
            try:
                row.append(self.saturday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _change_table12(self, rowNum, day):
        row = list()
        for i in range(self.saturday_table2.columnCount()):
            try:
                row.append(self.saturday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()

            if all(values):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time=%s, teacher=%s, lesson=%s, auditorium=%s WHERE id=%s",
                        tuple(values))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table(self, rowNum, day):
        row = list()
        for i in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table2(self, rowNum, day):
        row = list()
        for i in range(self.monday_table2.columnCount()):
            try:
                row.append(self.monday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table3(self, rowNum, day):
        row = list()
        for i in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.tuesday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table4(self, rowNum, day):
        row = list()
        for i in range(self.tuesday_table2.columnCount()):
            try:
                row.append(self.tuesday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table5(self, rowNum, day):
        row = list()
        for i in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table6(self, rowNum, day):
        row = list()
        for i in range(self.wednesday_table2.columnCount()):
            try:
                row.append(self.wednesday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table7(self, rowNum, day):
        row = list()
        for i in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table8(self, rowNum, day):
        row = list()
        for i in range(self.thursday_table2.columnCount()):
            try:
                row.append(self.thursday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table9(self, rowNum, day):
        row = list()
        for i in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table10(self, rowNum, day):
        row = list()
        for i in range(self.friday_table2.columnCount()):
            try:
                row.append(self.friday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table11(self, rowNum, day):
        row = list()
        for i in range(self.saturday_table.columnCount()):
            try:
                row.append(self.saturday_table.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _delete_table12(self, rowNum, day):
        row = list()
        for i in range(self.saturday_table2.columnCount()):
            try:
                row.append(self.saturday_table2.item(rowNum, i).text())
            except:
                row.append(None)

        dialog = ChangeDialog2()
        if dialog.exec_() == QDialog.Accepted:
            values2 = dialog.get_values2()

            if all(values2):
                try:
                    self.cursor.execute(
                        "UPDATE timetable2 SET time= ' ', teacher=' ', lesson=' ', auditorium=' ' WHERE id=%s",
                        tuple(values2))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Failed to update the record")
            else:
                QMessageBox.about(self, "Error", "Enter all fields")


    def _update_shedule_1(self):
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()
        self._update_saturday_table()

    def _update_shedule_2(self):
        self._update_monday_table2()
        self._update_tuesday_table2()
        self._update_wednesday_table2()
        self._update_thursday_table2()
        self._update_friday_table2()
        self._update_saturday_table2()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
