from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtGui

from ostrich_runner.record_tools import *


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
            print 'run application', self.record_name
        elif event.key() == Qt.Key_Escape:
            QtGui.qApp.quit()
        else:
            super(RecordNameInput, self).keyPressEvent(event)


def on_desktop_center(window):
    frame = window.frameGeometry()
    center = QDesktopWidget().availableGeometry().center()
    frame.moveCenter(center)
    window.move(frame.topLeft())
