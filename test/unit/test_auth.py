#!/usr/bin/env python
from helpers import *

import stubs #.message

import auth
import hashlib

START("auth")
# {{{ Stub out a stack of test harness
pw = "testpass"
pw_hash = hashlib.md5(pw).hexdigest()

sys.path.append("modules.d")

import regen_modules
regen_modules.rebuild_bModules()
import bModules


pw = "testpass"
pw_hash = hashlib.md5(pw).hexdigest()

at = auth.Authenticator(auth_hash=pw_hash)

auth_msg = stubs.message()
auth_msg.nick = "richo"

bad_msg = stubs.message()
bad_msg.nick = "buttfayse"
bad_msg.replyto = "buttfayse"
bad_msg.data_segment = "badpassword"


last_msg = ""
fake_module = stubs.message()
fake_module.parent = stubs.ircSocket()
def privmsg(to, msg):
    global last_msg
    last_msg = msg
fake_module.parent.privmsg = privmsg
fake_module.parent.authenticator = at

# }}}

ASSERT(at.try_auth(auth_msg, pw), "Should authenticate with correct password")

ASSERT(at.authed(auth_msg), "Should still be authenticated")

defined_fail_msg = "auth failed"
@bModules.with_auth(fail_message=defined_fail_msg)
def func_with_auth(inst, msg):
    return "Successful Auth"

ASSERT(func_with_auth(fake_module, auth_msg) == "Successful Auth",
        "func_with_auth should have recieved valid auth details")

ASSERT(func_with_auth(fake_module, bad_msg) == False,
        "non-authenticated nicks should not access the protected function")

ASSERT(last_msg == defined_fail_msg, "Auth should send the correct fail message")
END()
