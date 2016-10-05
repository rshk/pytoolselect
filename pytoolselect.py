#!/usr/bin/env python3

import re
import sys
import os

DEFAULT_PYTHON_MAJOR = 3

re_python_runtime = re.compile(r'^python-(?P<major>[0-9]+)(\..*)?$')


class NotFound(Exception):
    pass


def find_file(start_path, file_name, dev_id=None):

    st = os.stat(start_path)
    if dev_id is not None:
        if st.st_dev != dev_id:
            raise NotFound('Stopping at filesystem boundary')

    full_path = os.path.join(start_path, file_name)
    if os.path.exists(full_path):
        return full_path

    parent_dir = os.path.dirname(start_path)
    if parent_dir == start_path:
        raise NotFound('Not found at filesystem root')

    return find_file(parent_dir, file_name, dev_id=st.st_dev)


def get_runtime_name():
    try:
        runtime_file = find_file(os.getcwd(), 'runtime.txt')
    except NotFound:
        return None

    with open(runtime_file, 'r') as fp:
        return fp.read().strip()


def get_python_major_from_runtime_name(runtime_name):
    m = re_python_runtime.match(runtime_name)
    if m is None:
        return None
    return int(m.group('major'))


def get_python_major():
    runtime_name = get_runtime_name()
    if runtime_name is None:
        return DEFAULT_PYTHON_MAJOR
    res = get_python_major_from_runtime_name(runtime_name)
    if res is None:
        return DEFAULT_PYTHON_MAJOR
    return res


if __name__ == '__main__':
    py_version = get_python_major()
    python = 'python{}'.format(py_version)
    module_name = os.path.basename(sys.argv[0])
    command = [python, '-m', module_name] + sys.argv[1:]
    os.execvp(python, command)
