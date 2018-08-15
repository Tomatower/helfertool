import logging

# The logging part was inspired by the following blog entries and projects:
#
# https://lincolnloop.com/blog/django-logging-right-way/
# https://lincolnloop.com/blog/logging-systemds-journal-python/
# https://github.com/madzak/python-json-logger
# https://www.caktusgroup.com/blog/2013/09/18/central-logging-django-graylog2-and-graypy/


SKIP_ATTRS = (
    # all default attributes
    'args', 'created', 'exc_info', 'exc_text', 'filename', 'funcName',
    'levelname', 'levelno', 'lineno', 'module', 'msecs', 'msg', 'name',
    'pathname', 'process', 'processName', 'relativeCreated', 'stack_info',
    'thread', 'threadName',

    # custom things
    'event',
)


def get_extra_attrs(record):
    """
    Extracts all extra attributes from the log record and additionally:

    * adds the "levelname" as "level"
    * replaces "event" by "event_url" and "event_pk"
    """
    result = {}

    for k, v in record.__dict__.items():
        if k not in SKIP_ATTRS:
            result[k] = v

    # log level
    result["level"] = record.levelname

    # event
    if hasattr(record, 'event'):
        result["event_url"] = record.event.url_name
        result["event_pk"] = record.event.pk

    return result


class HelfertoolFormatter(logging.Formatter):
    def format(self, record):
        time = self.formatTime(record)

        extras = get_extra_attrs(record)
        extras = ["{}={}".format(k, v) for k, v in extras.items()]
        extras = ', '.join(extras)

        return "{} {} ({})".format(time, record.msg, extras)
