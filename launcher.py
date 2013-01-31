import sys

from PySide.QtGui import QApplication

from ostrich_runner.ui import RecordNameInput

if __name__ == '__main__':
    application = QApplication(sys.argv)
    input = RecordNameInput()
    input.show()
    application.exec_()
