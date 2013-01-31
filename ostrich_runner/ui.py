from functools import partial

from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtGui

from ostrich_runner.record_tools import *
from ostrich_runner.actions import *

display_error = partial(QMessageBox.critical, u'error')


class RecordNameInput(QLineEdit, object):

    def __init__(self, *args, **kwargs):
        super(RecordNameInput, self).__init__(*args, **kwargs)
        record_names = get_record_names()
        self.set_tips(record_names)
        self.setWindowTitle(u'OstrichRunner')

    def set_tips(self, record_names):
        self.setCompleter(QCompleter(record_names))

    @property
    def record_name(self):
        return self.text().strip()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            try_run_application_and_quit_if_valid_record_name(self.record_name)
        elif event.key() == Qt.Key_Escape:
            QtGui.qApp.quit()
        else:
            super(RecordNameInput, self).keyPressEvent(event)


def on_desktop_center(window):
    frame = window.frameGeometry()
    center = QDesktopWidget().availableGeometry().center()
    frame.moveCenter(center)
    window.move(frame.topLeft())
