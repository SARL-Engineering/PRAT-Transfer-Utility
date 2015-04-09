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
from os import getenv, makedirs
from os.path import exists
import logging

# Custom imports

#####################################
# Global Variables
#####################################
application_hidden_path_root = getenv('APPDATA') + "\\TransferUtility"
application_transfer_log_path = application_hidden_path_root + "\\transfer_log.txt"
application_cleanup_log_path = application_hidden_path_root + "\\cleanup_log.txt"


#####################################
# Logger Class Definition
#####################################
class Logger(QtCore.QObject):
    def __init__(self, main_window):
        QtCore.QObject.__init__(self)
        # ########## Reference to top level window ##########
        self.main_window = main_window

        # ########## Get the instances of the loggers ##########
        self.transfer_logger = logging.getLogger("TRANSFER_PRAT")
        self.transfer_logger_file = open(application_transfer_log_path, 'a')

        self.cleanup_logger = logging.getLogger("CLEANUP_PRAT")
        self.cleanup_logger_file = open(application_cleanup_log_path, 'a')

        # ########## Set up logger with desired settings ##########
        self.setup_logger()

        # ########## Place divider in log file to see new program launch ##########
        self.add_startup_log_buffer_text()

    def setup_logger(self):
        # fmt='%(levelname)s : %(asctime)s :  %(message)s'  In case this needs to be fixed later
        formatter = logging.Formatter(fmt='%(asctime)s :  %(message)s', datefmt='%m/%d/%y %H:%M:%S')

        if not exists(application_hidden_path_root):
            makedirs(application_hidden_path_root)

        self.transfer_logger.setLevel(logging.DEBUG)
        transfer_file_handler = logging.FileHandler(filename=application_transfer_log_path)
        transfer_file_handler.setFormatter(formatter)
        transfer_file_handler.setLevel(logging.DEBUG)
        self.transfer_logger.addHandler(transfer_file_handler)

        self.cleanup_logger.setLevel(logging.DEBUG)
        cleanup_file_handler = logging.FileHandler(filename=application_cleanup_log_path)
        cleanup_file_handler.setFormatter(formatter)
        cleanup_file_handler.setLevel(logging.DEBUG)
        self.cleanup_logger.addHandler(cleanup_file_handler)

    def add_startup_log_buffer_text(self):
        self.transfer_logger_file.write("\n########## New Instance of Application Started ##########\n\n")
        self.transfer_logger_file.close()

        self.cleanup_logger_file.write("\n########## New Instance of Application Started ##########\n\n")
        self.cleanup_logger_file.close()
