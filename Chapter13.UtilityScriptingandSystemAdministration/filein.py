#!/usr/bin/env python3

import fileinput

with fileinput.input('/etc/os-release') as f_input:
    for line in f_input:
        # filename .filename()
        # line number .lineno()
        print(f_input.filename(), f_input.lineno(),line, end='')
