from datetime import datetime, timedelta


def date_from_webkit(webkit_timestamp):
    '''WEBKit Timestamp -> datetime'''
    epoch_start = datetime(1601,1,1)
    delta = timedelta(microseconds=int(webkit_timestamp))
    return epoch_start + delta


def date_to_webkit(datetime_):
    '''datetime -> WEBKit Timestamp'''
    epoch_start = datetime(1601, 1, 1)
    diff = datetime_ - epoch_start
    seconds_in_day = 60 * 60 * 24
    return (
        diff.days * seconds_in_day + diff.seconds
    ) * 1000000 + diff.microseconds 