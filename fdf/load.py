from io import TextIOWrapper

from .errors import BadDelimiterException

DEFAULT_DICT_DELIMITER = ':'
DEFAULT_KEY_DELIMITER = '.'


def load(fp: TextIOWrapper, key_delimiter: str = DEFAULT_KEY_DELIMITER,
         dict_delimiter: str = DEFAULT_DICT_DELIMITER) -> dict:
    return loads(fp.read(), key_delimiter, dict_delimiter)


def loads(s: str, key_delimiter: str = DEFAULT_KEY_DELIMITER,
          dict_delimiter: str = DEFAULT_DICT_DELIMITER) -> dict:
    return decode(s.splitlines(), key_delimiter, dict_delimiter)


def decode(lines: iter, key_delimiter: str, dict_delimiter: str) -> dict:
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
