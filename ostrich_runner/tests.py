import pytest
from mock import patch

from PySide.QtCore import QProcess

import records as _records
from records import Record

from ostrich_runner.record_tools import *
from ostrich_runner.actions import *


@patch.object(_records, 'RECORDS', [])
def test_get_record_names__empty():
    assert [] == get_record_names()


RECORDS = [
    Record(name='b', app='chromium-browser', args=None),
    Record(name='l', app='leafpad', args=None),
    Record(name='i', app='dolphin', args=['/home/pk/'])
]


@patch.object(_records, 'RECORDS', RECORDS)
def test_get_record_names__not_empty():
    assert ['b', 'l', 'i'] == get_record_names()


@patch.object(_records, 'RECORDS', RECORDS)
def test_get_record__exists():
    expected_record = Record(name='i', app='dolphin', args=['/home/pk/'])
    assert expected_record == get_record('i')


@patch.object(_records, 'RECORDS', RECORDS)
def test_get_record__not_exists():
    with pytest.raises(RecordDoesNotExists):
        get_record('gg')


@patch.object(_records, 'RECORDS', RECORDS)
@patch.object(QProcess, 'startDetached', return_value=True)
def test_run_application__correct(startDetached):
    run_application('i')
    startDetached.assert_called_once_with('dolphin', ['/home/pk/'])


@patch.object(_records, 'RECORDS', RECORDS)
@patch.object(QProcess, 'startDetached', return_value=False)
def test_run_application__cannot_run_application(startDetached):
    with pytest.raises(CannotRunApplication):
        run_application('i')
