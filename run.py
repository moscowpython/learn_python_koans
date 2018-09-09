import sys

import pytest


if __name__ == '__main__':
    print('''     _                                     _   _                   _
    | | ___  __ _ _ __ _ __    _ __  _   _| |_| |__   ___  _ __   | | _____   __ _ _ __  ___
    | |/ _ \/ _` | '__| '_ \  | '_ \| | | | __| '_ \ / _ \| '_ \  | |/ / _ \ / _` | '_ \/ __|
    | |  __/ (_| | |  | | | |_| |_) | |_| | |_| | | | (_) | | | |_|   < (_) | (_| | | | \__ \\
    |_|\___|\__,_|_|  |_| |_(_) .__/ \__, |\__|_| |_|\___/|_| |_(_)_|\_\___/ \__,_|_| |_|___/
                              |_|    |___/                                                   ''')
    pytest_params = [
        '-x',  # first fail
        '--verbose',  # на каждый тест по строке в выводе
    ]

    args = sys.argv
    if args and len(args) >= 2:
        pytest_params.append('koans/about_%s.py' % args[1])

    pytest.main(pytest_params)
