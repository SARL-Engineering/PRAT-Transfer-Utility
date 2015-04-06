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

import logging

# Custom imports

#####################################
# Global Variables
#####################################


#####################################
# StatusLoggerTab Class Definition
#####################################
class StatusLoggerTab(QtCore.QObject):
    def __init__(self, main_window):
        QtCore.QObject.__init__(self)

        # ########## Reference to top level window ##########
        self.main_window = main_window

        # ########## Reference to main_window gui elements ##########
        self.file_text_browser = self.main_window.file_transfer_text_browser
        self.cleanup_text_browser = self.main_window.cleanup_text_browser