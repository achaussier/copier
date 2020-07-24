#!/usr/bin/env python3
import os
import os.path
import sys
from contextlib import suppress

from plumbum.cmd import git

with open("created-with-tasks.txt", "a", newline="\n") as cwt:
    cwt.write(" ".join([os.environ["STAGE"]] + sys.argv[1:]) + "\n")
    git("init")
    with suppress(FileNotFoundError):
        os.unlink("delete-in-tasks.txt")
