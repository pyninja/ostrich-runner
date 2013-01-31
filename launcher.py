import sys

from PySide.QtGui import QApplication

from ostrich_runner.ui import *

if __name__ == '__main__':
    application = QApplication(sys.argv)
    input = RecordNameInput()
    input.show()
    on_desktop_center(input)
    application.exec_()
