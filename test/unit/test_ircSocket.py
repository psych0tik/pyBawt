#!/usr/bin/env python
from helpers import *

import ircSocket

START("mangle")
mangle = ircSocket.mangle

nick = "richo"

nick = mangle(nick)
ASSERT(nick == "richo_", "Mangle should pad with underscores to 8 chars")

for i in xrange(3):
    nick = mangle(nick)

ASSERT(nick == "richo_00", "Mangle should add numbers when nick length exceeded")

for i in xrange(3):
    nick = mangle(nick)

ASSERT(nick == "richo_03", "Mangle should then increment those numerals")


END()


