= pyBawt

pyBawt is the stupid and lovable bot that floats around on psych0tik.net

He is pretty easy to develop for, the one part that is reasoanbly sane is his
plugin mechanisms.

They are documented in modules.d/000\_core.py which contains a working spec,
amongst other things

= Running pyBawt

pyBawt takes all of his config from two files

== pyBawt.conf

Which contains details of the bot, his nick, where to connect to and which
channels to join initially.

It also contains a hash to use for authentication in the Auth module, if you
choose to use it.

== module\_config.py

This is a python file which is essentially for configuration. It specifies
which modules to use for which channels by default (It can be overridden at run
with the !add command, for example)

The channel names should be in lowercase and are literal, with two exceptions;

* default: Any modules specified in default will work in any channel, including
  new ones that are joined.
* privmsg: This specifies which modules will be available to handle privmsg's.
  This also includes notices, for implementation purposes.
