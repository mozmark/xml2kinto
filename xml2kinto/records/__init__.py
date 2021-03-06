from .base import Records
from .xml import XMLRecords
from .kinto import KintoRecords

__all__ = ('same_record', 'Records', 'XMLRecords', 'KintoRecords')


def same_record(fields, one, two):
    for key in fields:
        if one.get(key) != two.get(key):
            return False
    return True
