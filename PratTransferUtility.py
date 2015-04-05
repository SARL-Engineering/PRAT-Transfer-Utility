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

# Custom importss

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
        #TODO: Repurpose logger from pickandplate
        #self.logger_core = PickAndPlateLogger(console_output=True)
        #self.logger = logging.getLogger("PickAndPlate")

        # ########## Setup and get program settings ##########
        #TODO: Repurpose settings from pickandplate
        #self.settings = PickAndPlateSettings(self)

        self.cleanup_table_widget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.cleanup_table_widget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.cleanup_table_widget.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        self.cleanup_table_widget.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)

        self.transfer_table_widget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.transfer_table_widget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.transfer_table_widget.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        self.transfer_table_widget.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        self.transfer_table_widget.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.ResizeToContents)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # This allows the keyboard interrupt kill to work  properly
    app = QtGui.QApplication(sys.argv)  # Create the base qt gui application
    myWindow = ProgramWindow()  # Make a window in this application using the pnp MyWindowClass
    myWindow.setWindowTitle("PRAT Transfer Utility")
    myWindow.resize(1500, 800)
    myWindow.show()  # Show the window in the application

    app.exec_()  # Execute launching of the application