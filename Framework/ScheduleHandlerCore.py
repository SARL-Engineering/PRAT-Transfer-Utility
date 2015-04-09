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
# QueueProcessor Class Definition
#####################################
class QueueProcessor(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)


#####################################
# ScheduleHandler Class Definition
#####################################
class ScheduleHandler(QtCore.QThread):
    def __init__(self, main_window):
        QtCore.QThread.__init__(self)

        # ########## Reference to top level window ##########
        self.main_window = main_window

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the instances of the loggers ##########
        self.transfer_logger = logging.getLogger("TRANSFER_PRAT")
        self.cleanup_logger = logging.getLogger("CLEANUP_PRAT")

        # ########## Thread flags ##########
        self.not_abort_flag = True

        # ########## Thread Variables ##########
        # Form of {{a, b, a_to_b, c_a_if_in_b, c_b_and_a, cleanup_age},
        # {a, b, a_to_b, c_a_if_in_b, c_b_and_a, cleanup_age}}
        self.process_queue = {}

        # ########## Make signal/slot connections ##########
        self.connect_signals_to_slots()

        # ########## Start timer ##########
        self.start()

    def connect_signals_to_slots(self):
        pass

    def run(self):
        while self.not_abort_flag:
            self.check_schedules_and_add_to_queue()
            self.process_queue_to_threads()
            self.msleep(100)

    def check_schedules_and_add_to_queue(self):
        current_time = QtCore.QTime.currentTime()

        self.settings.beginGroup("TransferTable")
        for i in range(self.settings.childGroups().count()):
            self.settings.beginGroup(str(i))

            if self.settings.value("enabled").toString() == "True":
                sched_time = QtCore.QTime.fromString(self.settings.value("schedule").toString(), "h:mm AP")
                if (sched_time.hour() == current_time.hour()) and (sched_time.minute() == current_time.minute()):
                    print "It's working!!!!"

            else:
                pass

            self.settings.endGroup()
        self.settings.endGroup()

        self.settings.beginGroup("CleanupTable")
        for i in range(self.settings.childGroups().count()):
            self.settings.beginGroup(str(i))

            self.settings.endGroup()
        self.settings.endGroup()

    def process_queue_to_threads(self):
        for task in self.process_queue:
            #TODO: Have it spin off sub-threads for each task so they run concurrently
            pass

    def on_kill_threads_slot(self):
        self.not_abort_flag = False