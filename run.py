import sys

import pytest


if __name__ == '__main__':
    pytest_params = [
        '-x',  # first fail
        '--verbose',  # на каждый тест по строке в выводе
    ]

    args = sys.argv
    if args and len(args) >= 2:
        pytest_params.append('koans/about_%s.py' % args[1])

    pytest.main(pytest_params)
