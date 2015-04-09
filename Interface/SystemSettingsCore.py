"""
    Main file used to launch the prat transfer gui.
    No other files should be used for launching this application.
"""

__author__ = "Corwin Perren"
__copyright__ = "None"
__credits__ = [""]
__license__ = "GPL (GNU General Public License)"
__version__ = "0.1 Alpha"
__maintainer__ = "Corwin Perren"
__email__ = "caperren@caperren.com"
__status__ = "Development"

# This file is part of "PRAT Transfer Utility".
#
# "Pick And Plate" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "Pick And Plate" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "PRAT Transfer Utility".  If not, see <http://www.gnu.org/licenses/>.

#####################################
# Imports
#####################################
# Python native imports
from PyQt4 import QtCore, QtGui

# Custom imports

#####################################
# Global Variables
#####################################


#####################################
# SettingsTab Class Definition
#####################################
class SettingsTab(QtCore.QObject):
    def __init__(self, main_window):
        QtCore.QObject.__init__(self)

        # ########## Reference to top level window ##########
        self.main_window = main_window

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Reference to main_window gui elements ##########
        self.transfer_table = self.main_window.transfer_table_widget
        self.transfer_source = self.main_window.transfer_source_line_edit
        self.transfer_source_browse = self.main_window.transfer_source_browse_button
        self.transfer_destination = self.main_window.transfer_destination_line_edit
        self.transfer_destination_browse = self.main_window.transfer_destination_browse_button
        self.transfer_schedule_time = self.main_window.transfer_schedule_time_edit
        self.transfer_clean_source_checkbox = self.main_window.transfer_clean_source_check_box
        self.transfer_cleanup_age = self.main_window.transfer_cleanup_age_spin_box
        self.transfer_enabled = self.main_window.transfer_enabled_check_box
        self.transfer_add_update = self.main_window.transfer_add_update_button
        self.transfer_remove = self.main_window.transfer_remove_button

        self.cleanup_table = self.main_window.cleanup_table_widget
        self.cleanup_a_path = self.main_window.cleanup_a_path_line_edit
        self.cleanup_a_browse = self.main_window.cleanup_a_path_browse_button
        self.cleanup_b_path = self.main_window.cleanup_b_path_line_edit
        self.cleanup_b_browse = self.main_window.cleanup_b_path_browse_button
        self.cleanup_schedule_time = self.main_window.cleanup_schedule_time_edit
        self.cleanup_a_if_in_b = self.main_window.cleanup_clean_a_if_in_b_check_box
        self.cleanup_clean_b = self.main_window.cleanup_clean_b_also_check_box
        self.cleanup_age = self.main_window.cleanup_only_age_spin_box
        self.cleanup_enabled = self.main_window.cleanup_enabled_check_box
        self.cleanup_add_update = self.main_window.cleanup_add_update_button
        self.cleanup_remove = self.main_window.cleanup_remove_button

        # ########## Load all saved schedules ##########
        self.load_saved_settings()

        # ########## Fit column widths to contents and disable editing ##########
        self.fix_table_column_headers()
        self.transfer_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.cleanup_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        # ########## Connect buttons to methods ##########
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.transfer_table.cellClicked.connect(self.on_transfer_table_cell_clicked_slot)
        self.transfer_add_update.clicked.connect(self.on_transfer_add_updated_clicked_slot)
        self.transfer_remove.clicked.connect(self.on_transfer_remove_clicked_slot)
        self.transfer_source_browse.clicked.connect(self.on_transfer_source_browse_clicked_slot)
        self.transfer_destination_browse.clicked.connect(self.on_transfer_dest_browse_clicked_slot)

        self.cleanup_table.cellClicked.connect(self.on_cleanup_table_cell_clicked_slot)
        self.cleanup_add_update.clicked.connect(self.on_cleanup_add_updated_clicked_slot)
        self.cleanup_remove.clicked.connect(self.on_cleanup_remove_clicked_slot)
        self.cleanup_a_browse.clicked.connect(self.on_a_path_browse_clicked_slot)
        self.cleanup_b_browse.clicked.connect(self.on_b_path_browse_clicked_slot)

    def load_saved_settings(self):
        tt = self.transfer_table
        ct = self.cleanup_table

        tt.clearContents()
        tt.removeRow(0)

        ct.clearContents()
        ct.removeRow(0)

        self.settings.beginGroup("TransferTable")
        for i in range(self.settings.childGroups().count()):
            self.settings.beginGroup(str(i))
            tt.insertRow(int(i))
            tt.setItem(int(i), 0, QtGui.QTableWidgetItem(str(self.settings.value("source").toString())))
            tt.setItem(int(i), 1, QtGui.QTableWidgetItem(str(self.settings.value("destination").toString())))
            tt.setItem(int(i), 2, QtGui.QTableWidgetItem(str(self.settings.value("schedule").toString())))
            tt.setItem(int(i), 3, QtGui.QTableWidgetItem(str(self.settings.value("cleanup").toString())))
            tt.setItem(int(i), 4, QtGui.QTableWidgetItem(str(self.settings.value("cleanup_age").toString())))
            tt.setItem(int(i), 5, QtGui.QTableWidgetItem(str(self.settings.value("enabled").toString())))
            self.settings.endGroup()
        self.settings.endGroup()

        self.settings.beginGroup("CleanupTable")
        for i in range(self.settings.childGroups().count()):
            self.settings.beginGroup(str(i))
            ct.insertRow(int(i))
            ct.setItem(int(i), 0, QtGui.QTableWidgetItem(str(self.settings.value("a_path").toString())))
            ct.setItem(int(i), 1, QtGui.QTableWidgetItem(str(self.settings.value("b_path").toString())))
            ct.setItem(int(i), 2, QtGui.QTableWidgetItem(str(self.settings.value("schedule").toString())))
            ct.setItem(int(i), 3, QtGui.QTableWidgetItem(str(self.settings.value("a_if_in_b").toString())))
            ct.setItem(int(i), 4, QtGui.QTableWidgetItem(str(self.settings.value("b_and_a").toString())))
            ct.setItem(int(i), 5, QtGui.QTableWidgetItem(str(self.settings.value("cleanup_age").toString())))
            ct.setItem(int(i), 6, QtGui.QTableWidgetItem(str(self.settings.value("enabled").toString())))
            self.settings.endGroup()
        self.settings.endGroup()

    def fix_table_column_headers(self):
        header = self.transfer_table.horizontalHeader()
        for section in range(header.count()):
            header.setResizeMode(section, QtGui.QHeaderView.ResizeToContents)

        header = self.cleanup_table.horizontalHeader()
        for section in range(header.count()):
            header.setResizeMode(section, QtGui.QHeaderView.ResizeToContents)

    def show_missing_path_messagebox(self):
        message = "Please enter the missing path and try again."
        QtGui.QMessageBox.question(self.main_window, "Missing Path", message, QtGui.QMessageBox.Ok)

    def on_transfer_add_updated_clicked_slot(self):
        table = self.transfer_table

        source_path = self.transfer_source.text()
        dest_path = self.transfer_destination.text()
        time = self.transfer_schedule_time.time()
        clean_source = self.transfer_clean_source_checkbox.isChecked()
        cleanup_age = self.transfer_cleanup_age.value()
        transfer_enabled = self.transfer_enabled.isChecked()

        if (source_path == "") or (dest_path == ""):
            self.show_missing_path_messagebox()
            return

        elif self.is_in_table(table, source_path, dest_path, int(0)) != -1:
            row = self.is_in_table(table, source_path, dest_path, int(0))
            table.setItem(row, 2, QtGui.QTableWidgetItem(str(time.toString('h:mm AP'))))
            table.setItem(row, 3, QtGui.QTableWidgetItem(str(clean_source)))
            table.setItem(row, 4, QtGui.QTableWidgetItem(str(cleanup_age) + " Days"))
            table.setItem(row, 5, QtGui.QTableWidgetItem(str(transfer_enabled)))
        else:
            table.insertRow(0)
            table.setItem(0, 0, QtGui.QTableWidgetItem(str(source_path)))
            table.setItem(0, 1, QtGui.QTableWidgetItem(str(dest_path)))
            table.setItem(0, 2, QtGui.QTableWidgetItem(str(time.toString('h:mm AP'))))
            table.setItem(0, 3, QtGui.QTableWidgetItem(str(clean_source)))
            table.setItem(0, 4, QtGui.QTableWidgetItem(str(cleanup_age) + " Days"))
            table.setItem(0, 5, QtGui.QTableWidgetItem(str(transfer_enabled)))

        self.save_tables_to_settings()

    def on_transfer_remove_clicked_slot(self, event):
        table = self.transfer_table
        source_path = self.transfer_source.text()
        dest_path = self.transfer_destination.text()

        if self.is_in_table(table, source_path, dest_path, 0) != -1:
            row = self.is_in_table(table, source_path, dest_path, 0)
            table.removeRow(row)

        self.save_tables_to_settings()

    def on_transfer_source_browse_clicked_slot(self):
        file_dialog = QtGui.QFileDialog(self.main_window)
        file_dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        file_dialog.exec_()
        self.transfer_source.setText(file_dialog.selectedFiles()[0])

    def on_transfer_dest_browse_clicked_slot(self):
        file_dialog = QtGui.QFileDialog(self.main_window)
        file_dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        file_dialog.exec_()
        self.transfer_destination.setText(file_dialog.selectedFiles()[0])

    def on_transfer_table_cell_clicked_slot(self, row):
        self.transfer_source.setText(self.transfer_table.item(row, 0).text())
        self.transfer_destination.setText(self.transfer_table.item(row, 1).text())

        self.transfer_schedule_time.setTime(QtCore.QTime.fromString(self.transfer_table.item(row, 2).text(), "h:mm AP"))

        if self.transfer_table.item(row, 3).text() == "True":
            self.transfer_clean_source_checkbox.setChecked(True)
        else:
            self.transfer_clean_source_checkbox.setChecked(False)

        self.transfer_cleanup_age.setValue(int(self.transfer_table.item(row, 4).text()[:-5]))

        if self.transfer_table.item(row, 5).text() == "True":
            self.transfer_enabled.setChecked(True)
        else:
            self.transfer_enabled.setChecked(False)

    def on_cleanup_add_updated_clicked_slot(self):
        table = self.cleanup_table

        a_path = self.cleanup_a_path.text()
        b_path = self.cleanup_b_path.text()
        time = self.cleanup_schedule_time.time()
        a_if_in_b = self.cleanup_a_if_in_b.isChecked()
        b_and_a = self.cleanup_clean_b.isChecked()
        cleanup_age = self.cleanup_age.value()
        cleanup_enabled = self.cleanup_enabled.isChecked()

        if a_path == "":
            self.show_missing_path_messagebox()
            return

        elif self.is_in_table(table, a_path, b_path, 0) != -1:
            row = self.is_in_table(table, a_path, b_path, 0)
            table.setItem(row, 2, QtGui.QTableWidgetItem(str(time.toString('h:mm AP'))))
            table.setItem(row, 3, QtGui.QTableWidgetItem(str(a_if_in_b)))
            table.setItem(row, 4, QtGui.QTableWidgetItem(str(b_and_a)))
            table.setItem(row, 5, QtGui.QTableWidgetItem(str(cleanup_age) + " Days"))
            table.setItem(row, 6, QtGui.QTableWidgetItem(str(cleanup_enabled)))
        else:
            table.insertRow(0)
            table.setItem(0, 0, QtGui.QTableWidgetItem(str(a_path)))
            table.setItem(0, 1, QtGui.QTableWidgetItem(str(b_path)))
            table.setItem(0, 2, QtGui.QTableWidgetItem(str(time.toString('h:mm AP'))))
            table.setItem(0, 3, QtGui.QTableWidgetItem(str(a_if_in_b)))
            table.setItem(0, 4, QtGui.QTableWidgetItem(str(b_and_a)))
            table.setItem(0, 5, QtGui.QTableWidgetItem(str(cleanup_age) + " Days"))
            table.setItem(0, 6, QtGui.QTableWidgetItem(str(cleanup_enabled)))

        self.save_tables_to_settings()

    def on_cleanup_remove_clicked_slot(self):
        table = self.cleanup_table
        source_path = self.cleanup_a_path.text()
        dest_path = self.cleanup_b_path.text()

        if self.is_in_table(table, source_path, dest_path, 0) != -1:
            row = self.is_in_table(table, source_path, dest_path, 0)
            table.removeRow(row)

        self.save_tables_to_settings()

    def on_a_path_browse_clicked_slot(self):
        file_dialog = QtGui.QFileDialog(self.main_window)
        file_dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        file_dialog.exec_()
        self.cleanup_a_path.setText(file_dialog.selectedFiles()[0])

    def on_b_path_browse_clicked_slot(self):
        file_dialog = QtGui.QFileDialog(self.main_window)
        file_dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        file_dialog.exec_()
        self.cleanup_b_path.setText(file_dialog.selectedFiles()[0])

    def on_cleanup_table_cell_clicked_slot(self, row):
        self.cleanup_a_path.setText(self.cleanup_table.item(row, 0).text())
        self.cleanup_b_path.setText(self.cleanup_table.item(row, 1).text())

        self.cleanup_schedule_time.setTime(QtCore.QTime.fromString(self.cleanup_table.item(row, 2).text(), "h:mm AP"))

        if self.cleanup_table.item(row, 3).text() == "True":
            self.cleanup_a_if_in_b.setChecked(True)
        else:
            self.cleanup_a_if_in_b.setChecked(False)

        if self.cleanup_table.item(row, 4).text() == "True":
            self.cleanup_clean_b.setChecked(True)
        else:
            self.cleanup_clean_b.setChecked(False)

        self.cleanup_age.setValue(int(self.cleanup_table.item(row, 5).text()[:-5]))

        if self.cleanup_table.item(row, 6).text() == "True":
            self.cleanup_enabled.setChecked(True)
        else:
            self.cleanup_enabled.setChecked(False)

    def save_tables_to_settings(self):
        tt = self.transfer_table
        ct = self.cleanup_table

        self.settings.clear()

        self.settings.beginGroup("TransferTable")
        for i in range(tt.rowCount()):
            self.settings.beginGroup(str(i))
            self.settings.setValue("source", tt.item(int(i), 0).text())
            self.settings.setValue("destination", tt.item(int(i), 1).text())
            self.settings.setValue("schedule", tt.item(int(i), 2).text())
            self.settings.setValue("cleanup", tt.item(int(i), 3).text())
            self.settings.setValue("cleanup_age", tt.item(int(i), 4).text())
            self.settings.setValue("enabled", tt.item(int(i), 5).text())
            self.settings.endGroup()
        self.settings.endGroup()

        self.settings.beginGroup("CleanupTable")
        for i in range(ct.rowCount()):
            self.settings.beginGroup(str(i))
            self.settings.setValue("a_path", ct.item(int(i), 0).text())
            self.settings.setValue("b_path", ct.item(int(i), 1).text())
            self.settings.setValue("schedule", ct.item(int(i), 2).text())
            self.settings.setValue("a_if_in_b", ct.item(int(i), 3).text())
            self.settings.setValue("b_and_a", ct.item(int(i), 4).text())
            self.settings.setValue("cleanup_age", ct.item(int(i), 5).text())
            self.settings.setValue("enabled", ct.item(int(i), 6).text())
            self.settings.endGroup()
        self.settings.endGroup()

    @staticmethod
    def is_in_table(check_table, a_path, b_path, col):
        if b_path == "":
            for row in range(check_table.rowCount()):
                item = check_table.item(int(row), col)
                if a_path == item.text():
                    return int(row)
            return -1
        else:
            for row in range(check_table.rowCount()):
                item_a = check_table.item(int(row), 0)
                item_b = check_table.item(int(row), 1)
                if (a_path == item_a.text()) and (b_path == item_b.text()):
                    return int(row)
            return -1

