class Mapping(dict):
    def __getitem__(self, item):
        try:
            return super(Mapping, self).__getitem__(item)
        except KeyError:
            self[item] = []
            return self[item]

class LowerList(list):
    @staticmethod
    def lower(n):
        try:
            return n.lower()
        except AttributeError:
            return n
    def __contains__(self, value):
        return self.lower(value) in map(self.lower, self)

# Put all exceptions in lib.py

class ModuleError(Exception):
    pass

class IrcDisconnected(Exception):
    """IRC server closed connection"""
    pass

class IrcTerminated(Exception):
    """Irc session closed dilibrately"""
    pass
class FlushQueue(Exception):
    """ Flush the event queue, don't wait for IO"""
    pass
class ModulesDidntLoadDueToSyntax(Exception):
    def __nonzero__(self):
        # This allows us to retain the logical "if status" test.
        return False

class Restart(Exception):
    """Restart pyBawt, treat as being uncatchable"""
    pass
class StopHandling(Exception):
    """Bail out and stop trying to handle this event"""
    pass

class ModuleAlreadyLoaded(Exception):
    """Trying to load a module that's already active in this context"""
    pass

