from io import TextIOWrapper

from .errors import BadDelimiterException

DEFAULT_DICT_DELIMITER = ':'
DEFAULT_KEY_DELIMITER = '.'


def load(fp, key_delimiter=DEFAULT_KEY_DELIMITER, dict_delimiter=DEFAULT_DICT_DELIMITER):
    """ Load dictionary from FDF file in file-like object

    :param TextIOWrapper fp: the file-like object to open
    :param str key_delimiter: the delimiter between the key and value
    :param str dict_delimiter: the delimiter between nested dictionary entries
    :return:
    :rtype: dict
    """
    return loads(fp.read(), key_delimiter, dict_delimiter)


def loads(s, key_delimiter=DEFAULT_KEY_DELIMITER, dict_delimiter=DEFAULT_DICT_DELIMITER):
    """ Load dictionary from FDF file stored in string variable

    :param str s: the string to load a dictionary from
    :param str key_delimiter: the delimiter between the key and value
    :param str dict_delimiter: the delimiter between nested dictionary entries
    :return:
    :rtype: dict
    """
    return decode(s.splitlines(), key_delimiter, dict_delimiter)


def decode(lines, key_delimiter, dict_delimiter):
    """ Extract dictionary FDF from iterable of lines.

    :param iter lines: lines to decode
    :param str key_delimiter: the delimiter between the key and value
    :param str dict_delimiter: the delimiter between nested dictionary entries
    :return:
    :rtype: dict
    """
    result = {}
    for i, line in enumerate(lines):
        if len(line.strip()) == 0:  # ignore empty lines
            continue

        try:
            keys, value = line.split(dict_delimiter, 1)
        except ValueError:
            raise BadDelimiterException('No delimiter %s exists in line %s' % (dict_delimiter, i))

        value = value.strip()
        keys = keys.strip().split(key_delimiter)
        tail = keys.pop()
        node = result
        for k in keys:
            node = node.setdefault(k, {})
        node[tail] = value

    return result
