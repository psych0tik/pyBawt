#!/usr/bin/env python
import os
import sys

reset = "[0m"
def red(text):
    red = "[31m"
    return "%s%s%s" % (red, text, reset)
def green(text):
    green = "[32m"
    return "%s%s%s" % (green, text, reset)
def yellow(text):
    yellow = "[33m"
    return "%s%s%s" % (yellow, text, reset)
def blue(text):
    blue = "[34m"
    return "%s%s%s" % (blue, text, reset)
def purple(text):
    purple = "[35m"
    return "%s%s%s" % (purple, text, reset)
def cyan(text):
    cyan = "[36m"
    return "%s%s%s" % (cyan, text, reset)


sys.path.append(os.getcwd())

def ASSERT(cond, errormsg):
    if cond:
        print errormsg
        print green("\t\t\tPASS")
    else:
        # COLORS
        print >>sys.stderr, errormsg
        print red("\t\t\tFAIL")
        # TODO Add this to something and continue
        # Maybe even raise a token exceptiont o catch so I can
        # examine the stack
        exit()
def START(test):
    # epic kludge
    os.current_test = test
    print(cyan("== %s ==" % test))
def END():
    try:
        print(cyan("== %s ==" % os.current_test))
    except AttributeError:
        ASSERT(False, red("No test in progress"))
