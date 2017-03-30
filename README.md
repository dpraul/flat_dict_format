# FDF: Flat Dictionary Format [![Build Status](https://travis-ci.org/dpraul/flat_dict_format.svg?branch=master)](https://travis-ci.org/dpraul/flat_dict_format)

A simple file format for when mature serialization formats (YAML, JSON, XML, etc.) are too
restrictive and all you need is dictionaries of strings.

In hindsight I have built a feature-sparse version of the INI format, so I may never come back to this.


## Usage
Similar format to the JSON package.

### Load a string
```python
import fdf

r = fdf.loads('a.b.c: nested')  # r = {'a': {'b': {'c': 'nested'}}}
```

### Load from file
```python
import fdf

with open('artists.fdf') as f:
    r = fdf.load(f)
```

## Motivation

A piece of software I use dumps MP3 information from a playlist in a format I can control,
but won't do any sort of escaping on the data. Since ID3 tags can contain almost any character,
I needed a parser that had no character restrictions on the values in key: value pairs.
I settled on hoping no MP3's entered the system tagged with `\r\n`. 