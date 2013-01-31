# -*- coding: utf-8 -*-
from functools import partial

from PySide.QtCore import *
from PySide.QtGui import *

from ostrich_runner.record_tools import *


display_error = partial(QMessageBox.critical, None, u'error')


class CannotRunApplication(Exception):
    pass


def try_run_application_and_quit_if_valid_record_name(record_name):
    if record_name:
        try_run_application_and_quit(record_name)


def try_run_application_and_quit(record_name):
    try:
        run_application(record_name)
    except RecordDoesNotExists:
        display_error(u'Podany wpis nie istnieje w records.py')
    except CannotRunApplication:
        display_error(u'Błąd podczas uruchamiania aplikacji.')
    else:
        qApp.quit()


def run_application(record_name):
    record = get_record(record_name)
    done = QProcess.startDetached(record.app, record.args)
    if not done:
        raise CannotRunApplication()
