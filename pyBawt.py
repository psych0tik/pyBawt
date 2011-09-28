#!/usr/bin/env python
"""This is the main entry point to pyBawt.

The rest of the infrastructure ties together to make all the components of a
working IRC bot, this is just one sample implementation"""

##
# pyBawt is (Will be) released under the WTFPL
# You are hereby licensed to do WHATEVER THE FUCK YOU WANT with it's source
# code
##

# Rich Healey '08
from lib import *
import logging
try:
    import config
except InvalidConfig as e:
    logging.fatal("Couldn't load config file: %s" % (str(e)))

import ircSocket
import time
import sys
import os
import random
import bModules
import traceback


logging.info("pyBawt started")

# Have a crack at sweet argparsing

# TODO - hax involving stdout for debugging

try:
    import argparse
    parser = argparse.ArgumentParser(description='IRC bot written in python')
    parser.add_argument("-d", "--debug", dest='debug', action='store_true',
            default=False,
            help='include debug data, also crash violently on error')
    args = parser.parse_args()

    debug = args.debug
except ImportError:
# no argparse, probably py2.6
    debug = False
    # TODO - something clever here to make args still work

def restart_stub():
    net.quit("Going down for restart")
    os.execv(sys.executable, [sys.executable] + sys.argv)

net = ircSocket.chatnet(config.host, port=config.port, use_ssl=config.ssl)
# Ugly hax, port to argparse if we see any more nicks
nick = config.nick
net.identify(nick)
net.auth_self(config.nickserv_nick, config.nickserv_pass)

# Before we hit mainloop, write pidfile
if not debug:
    try:
        fh = open('/tmp/pyBawt.pid', 'w')
        fh.write(str(os.getpid()))
        fh.close()
    except IOError:
        logging.fatal("Couldn't write pidfile")

try:
    for i in config.channels:
        net.join(i)
    while True:
        try:
            net.recv_wait()
        except FlushQueue:
            pass
        net.dump_queue()
except KeyboardInterrupt:
    logging.error("Shutting down due to user intervention")
    net.quit("Killed from terminal")
except Restart:
    # TODO Include the user who did this
    logging.error("Restarting due to user intervention")
    restart_stub()
except IrcDisconnected:
    if ircSocket.should_reconnect():
        restart_stub()
except IrcTerminated:
    # Catch but don't handle, die gracefully
    pass
except Exception:
    # TODO - Checkout from stable git branch
    if debug: # Debug hook? Either way it's stupid.
        logging.error("Shutting down and bailing out")
        raise
    else:
        logging.error("Exception caught, restarting")
        traceback.print_exception(*sys.exc_info(), file=logging.Writer(logging.error))
        restart_stub()

