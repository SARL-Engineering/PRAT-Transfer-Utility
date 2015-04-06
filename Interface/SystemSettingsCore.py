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
# SettingsTab Class Definition
#####################################
class SettingsTab(QtCore.QObject):
    def __init__(self, main_window):
        QtCore.QObject.__init__(self)

        # ########## Reference to top level window ##########
        self.main_window = main_window

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
        self.cleanup_source = self.main_window.cleanup_source_line_edit
        self.cleanup_source_browse = self.main_window.cleanup_source_browse_button
        self.check_path = self.main_window.check_path_line_edit
        self.check_path_browse = self.main_window.check_path_browse_button
        self.cleanup_schedule_time = self.main_window.cleanup_schedule_time_edit
        self.cleanup_verify_exist = self.main_window.cleanup_verify_exist_check_box
        self.cleanup_age = self.main_window.cleanup_only_age_spin_box
        self.cleanup_enabled = self.main_window.cleanup_enabled_check_box
        self.cleanup_add_update = self.main_window.cleanup_add_update_button
        self.cleanup_remove = self.main_window.cleanup_remove_button