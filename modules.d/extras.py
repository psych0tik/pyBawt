
# EXTRAS
#-------
class OrlyModule(BawtM2):
    "Screams yarly at newbs"
    privmsg_re = "orly"
    privmsg_flags = re.I
    _name = "OrlyModule"
    def handle_privmsg(self, msg, ORLOG=['', 0, 0]):
        if not msg.nick:
            return
        if ORLOG[0] != msg.nick.lower() or ORLOG[1] + 150 < time.time():
            ORLOG[0] = msg.nick.lower()
            ORLOG[1] = time.time()
            ORLOG[2] = 0
            self.parent.privmsg(msg.replyto, "%s: yarly" % (msg.nick))
            return
        else:
            if ORLOG[2] == 0:
                self.parent.privmsg(msg.replyto, "%s: yasrsly" % (msg.nick))
                ORLOG[2] += 1
                return
            elif ORLOG[2] == 1:
                self.parent.privmsg(msg.replyto, "%s: ya, SRSLY FFS!!" % (msg.nick))
                ORLOG[2] += 1
                return
            else:
                self.parent.privmsg(msg.replyto,
                        "%s: Yes, really, you goddamn retarded pile of baby sputum." % (msg.nick))              
                self.parent.kick(msg.replyto, msg.nick, "GTFO")
                return

class SnackModule(BawtM2):
    ":D"
    _name = "SnackModule"
    privmsg_re = "botsnack"
    privmsg_flags = re.I
    def handle_privmsg(self, msg):
        self.parent.privmsg(msg.replyto, ":D")

class HarrassModule(BawtM2):
    "Yells incessantly at someone's bot"
    _name = "HarrassModule"
    def handle_privmsg(self, msg):
        if not msg.nick:
            return
        if msg.nick.lower() == "james":
            self.parent.privmsg(msg.replyto, "james, you're a douchenozzle")

class IllustrationModule(BawtM2):
    "Proves my point"
    _name = "HarrassModule"
    privmsg_re = "^!molested"
    def handle_privmsg(self, msg):
        self.parent.privmsg(msg.replyto, "Authored by richo (warl0ck) before you start arguing. Dynamic module loading bitchez0rz.")

class DebugTopicModule(BawtM2):
    "Testing for dynamic topic handling, checking that I can hook topic changes at the module level"
    topic_re = "."
    privmsg_re = "^!topic"
    _name = "DebugTopicModule"
    def handle_privmsg(self, msg):
        # XXX Epic kludge
        try:
            self.parent.privmsg(msg.replyto, "As far as I know, the topic is: %s" % (repr(self.channel.topic)))
        except:
            self.parent.privmsg(msg.replyto, "Your stupid topic module is broken, newb")
    def handle_topic(self, msg):
        self.parent.privmsg(msg.replyto, "%s set topic to: %s" % (msg.nick,  msg.data_segment))
        self.channel.topic = msg.data_segment
#/EXTRAS
#-------
