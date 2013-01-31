import records


class RecordDoesNotExists(Exception):
    pass


def get_record_names():
    return [record.name for record in records.RECORDS]


def get_record(name):
    for record in records.RECORDS:
        if record.name == name:
            return record
    raise RecordDoesNotExists()
