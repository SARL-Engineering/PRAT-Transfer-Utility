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
from os.path import exists, getsize
import logging

# Custom imports
import Framework.LoggerCore as LC

#####################################
# Global Variables
#####################################


#####################################
# StatusLoggerTab Class Definition
#####################################
class StatusLoggerTab(QtCore.QThread):

    transfer_log_needs_visual_update = QtCore.pyqtSignal()
    cleanup_log_needs_visual_update = QtCore.pyqtSignal()

    def __init__(self, main_window):
        QtCore.QThread.__init__(self)

        # ########## Reference to top level window ##########
        self.main_window = main_window

        # ########## Reference to main_window gui elements ##########
        self.file_text_browser = self.main_window.file_transfer_text_browser
        self.cleanup_text_browser = self.main_window.cleanup_text_browser

        # ########## Get the instances of the loggers ##########
        self.trans_lp = LC.application_transfer_log_path
        self.clean_lp = LC.application_cleanup_log_path

        self.transfer_logger_file = open(self.trans_lp, 'r')
        self.cleanup_logger_file = open(self.clean_lp, 'r')

        # ########## Thread flags ##########
        self.not_abort_flag = True

        # ########## Class Variables ##########
        self.transfer_prev_size = None
        self.cleanup_prev_size = None

        self.transfer_raw_text = None
        self.cleanup_raw_text = None

        # ########## Make signal/slot connections ##########
        self.connect_signals_to_slots()

        # ########## Start thread ##########
        self.start()

    def connect_signals_to_slots(self):
        self.transfer_log_needs_visual_update.connect(self.update_transfer_log_visuals)
        self.cleanup_log_needs_visual_update.connect(self.update_cleanup_log_visuals)

    def run(self):
        while self.not_abort_flag:
            if self.transfer_log_size_changed():
                self.transfer_logger_file.seek(0)
                self.transfer_raw_text = self.transfer_logger_file.readlines()
                self.transfer_log_needs_visual_update.emit()

            if self.cleanup_log_size_changed():
                self.cleanup_logger_file.seek(0)
                self.cleanup_raw_text = self.cleanup_logger_file.readlines()
                self.cleanup_log_needs_visual_update.emit()

            self.msleep(100)

    def transfer_log_size_changed(self):
        if not exists(self.trans_lp):
            return False
        elif getsize(self.trans_lp) != self.transfer_prev_size:
            self.transfer_prev_size = getsize(self.trans_lp)
            return True
        return False

    def cleanup_log_size_changed(self):
        if not exists(self.clean_lp):
            return False
        elif getsize(self.clean_lp) != self.cleanup_prev_size:
            self.cleanup_prev_size = getsize(self.clean_lp)
            return True
        return False

    def update_transfer_log_visuals(self):
        self.file_text_browser.setText("\n".join(self.transfer_raw_text))
        self.file_text_browser.verticalScrollBar().setValue(self.file_text_browser.verticalScrollBar().maximum())

    def update_cleanup_log_visuals(self):
        self.cleanup_text_browser.setText("\n".join(self.cleanup_raw_text))
        self.cleanup_text_browser.verticalScrollBar().setValue(self.cleanup_text_browser.verticalScrollBar().maximum())

    def on_kill_threads_slot(self):
        self.not_abort_flag = False