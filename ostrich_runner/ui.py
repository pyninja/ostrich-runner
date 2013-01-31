from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtGui


class RecordNameInput(QLineEdit, object):

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
