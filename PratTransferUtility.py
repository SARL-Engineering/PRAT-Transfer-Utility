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
import sys
from PyQt4 import QtCore, QtGui, uic
import signal

import logging

# Custom imports
from Framework.LoggerCore import Logger
from Framework.SettingsCore import Settings
from Interface.StatusLoggerCore import StatusLoggerTab
from Interface.SystemSettingsCore import SettingsTab

#####################################
# Global Variables
#####################################
form_class = uic.loadUiType("Interface/PRATTransferGui.ui")[0]  # Load the UI


#####################################
# ProgramWindow Class Definition
#####################################
class ProgramWindow(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # ########## Set up QT Application Window ##########
        self.setupUi(self)  # Has to be first call in class in order to link gui form objects

        # ########## Create the system logger and get an instance of it ##########
        self.logger_core = Logger(self)

        # ########## Setup and get program settings ##########
        self.settings = Settings(self)

        # ########## Instantiations of tab classes ##########
        self.log_viewer_tab = StatusLoggerTab(self)
        self.settings_tab = SettingsTab(self)

        # ########## Creation of the system tray icon ##########
        self.tray_icon = None
        self.tray_menu = None
        self.setup_tray_icon()

        # ########## Setup application taskbar icon ##########
        self.setup_taskbar_icon()

        # ########## Setup of gui elements ##########
        self.main_tab_widget.setCurrentIndex(0)

    def setup_tray_icon(self):
        self.tray_icon = QtGui.QSystemTrayIcon(QtGui.QIcon("Resources/app_icon.png"))
        self.tray_icon.activated.connect(self.on_tray_exit_triggered_slot)

        self.tray_menu = QtGui.QMenu()
        self.tray_menu.addAction("Show")
        self.tray_menu.addAction("Exit")

        self.tray_menu.triggered.connect(self.on_tray_exit_triggered_slot)
        self.tray_icon.setContextMenu(self.tray_menu)

        self.tray_icon.hide()

    def setup_taskbar_icon(self):
        app_icon = QtGui.QIcon()
        app_icon.addFile("Resources/app_icon.png", QtCore.QSize(16, 16))
        app_icon.addFile("Resources/app_icon.png", QtCore.QSize(24, 24))
        app_icon.addFile("Resources/app_icon.png", QtCore.QSize(32, 32))
        app_icon.addFile("Resources/app_icon.png", QtCore.QSize(48, 48))
        app_icon.addFile("Resources/app_icon.png", QtCore.QSize(256, 256))
        self.setWindowIcon(app_icon)

    def closeEvent(self, event):
        if self.isHidden():
            event.accept()
        else:
            message = "Are you sure you want to exit? Press NO to hide instead."
            reply = QtGui.QMessageBox.question(self, "Exit Dialog", message, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                self.hide()
                self.tray_icon.show()
                event.ignore()

    def on_tray_exit_triggered_slot(self, event):
        if event == 1:
            pass
        elif (event == 2) or (event == 3):
            self.show()
            self.tray_icon.hide()
        elif event.text() == "Exit":
            self.close()
        elif event.text() == "Show":
            self.show()
            self.tray_icon.hide()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # This allows the keyboard interrupt kill to work  properly
    app = QtGui.QApplication(sys.argv)  # Create the base qt gui application
    myWindow = ProgramWindow()  # Make a window in this application using the pnp MyWindowClass
    myWindow.setWindowTitle("Transfer Utility")
    myWindow.setWindowFlags(myWindow.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)
    myWindow.setWindowFlags(myWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
    myWindow.resize(1500, 800)
    myWindow.show()  # Show the window in the application
    app.exec_()  # Execute launching of the application