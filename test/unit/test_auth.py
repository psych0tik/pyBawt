#!/usr/bin/env python
from helpers import *

import stubs #.message

import auth
import hashlib

sys.path.append("modules.d")

import regen_modules
regen_modules.rebuild_bModules()
import bModules


pw = "testpass"
pw_hash = hashlib.md5(pw).hexdigest()

START("auth")
at = auth.Authenticator(auth_hash=pw_hash)

auth_msg = stubs.message()
auth_msg.nick = "richo"
bad_msg = stubs.message()
bad_msg.nick = "buttfayse"

fake_module = stubs.message()

ASSERT(at.try_auth(auth_msg, pw), "Should authenticate with correct password")

ASSERT(at.authed(auth_msg), "Should still be authenticated")

@bModules.with_auth(fail_message="auth failed")
def func_with_auth(msg):
    print "inside func with auth! %s" % msg.nick
    return "Successful Auth"

ASSERT(func_with_auth(fake_module, auth_msg) == "Successful Auth",
        "func_with_auth should have recieved valid auth details")

ASSERT(func_with_auth(fake_module, bad_msg) == False,
        "non-authenticated nicks should not access the protected function")

END()
