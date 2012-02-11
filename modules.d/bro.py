class BroModule(BawtM2):
    privmsg_re = ".*"
    privmsg_flags = re.I
    _name = "BroModule"

    def handle_privmsg(self, msg):
        data = msg.data_segment.lower()
        if "bro" not in data and "brah" not in data:
            self.parent.kick(msg.replyto, msg.nick, "browned")
