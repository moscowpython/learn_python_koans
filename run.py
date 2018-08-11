import pytest


if __name__ == '__main__':
    pytest.main([
        '-x',  # first fail
        '--verbose',  # на каждый тест по строке в выводе
    ])
