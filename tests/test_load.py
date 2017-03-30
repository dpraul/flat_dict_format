import os

import pytest

import fdf

sample_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample.fdf')
sample_file_result = {
    'top': {
        'first': {'deeper': 'deepest'},
        'second': '2',
        'third': '3'
    },
    'also_top': 't',
    'here': {'are': {'more': 'nodes'}}
}


def test_load():
    fd = open(sample_filename)
    r = fdf.load(fd)
    assert r == sample_file_result


def test_loads():
    r = fdf.loads('a.b: c')
    assert r == {'a': {'b': 'c'}}


def test_padding_removal():
    r = fdf.loads('    a:     b   ')
    assert r == {'a': 'b'}


def test_empty_line_ignore():
    r = fdf.loads('a:b\n\n\nc:d')
    assert r == {'a': 'b', 'c': 'd'}


def test_alt_delimiter():
    r = fdf.loads("question, who is the best: you", dict_delimiter=',')
    assert r == {'question': 'who is the best: you'}


def test_alt_key_delimiter():
    r = fdf.loads('a_b_c:d', key_delimiter='_')
    assert r == {'a': {'b': {'c': 'd'}}}


def test_empty_decode():
    r = fdf.loads('')
    assert r == {}


def test_missing_delimiter():
    with pytest.raises(fdf.errors.BadDelimiterException):
        fdf.loads('aaaa')
