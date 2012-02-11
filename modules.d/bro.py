class BroModule(BawtM2):
    privmsg_re = ".*"
    privmsg_flags = re.I
    _name = "BroModule"

    def handle_privmsg(self, msg):
        if "bro" not in msg.data_segment:
            self.parent.kick(msg.replyto, msg.nick, "browned")
