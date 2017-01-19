"""This module contains `tsaotun toolbox` class"""

from tsaotun.lib.Docker.Addon.command import Command
from tsaotun.cli import Tsaotun


class Toolbox(Command):
    """This class implements `tsaotun toolbox` command"""

    name = "toolbox"
    require = []

    def __init__(self):
        Command.__init__(self)
        self.settings[self.name] = None

    def eval_command(self, args):
        cli = Tsaotun()
        if args["shell"]:
            cli.send("exec -it {} /bin/bash".format(args["container"]))
        elif args["show_ip"]:
            cli.send(
                "container inspect {} \
                -f {{{{NetworkSettings.IPAddress}}}}".format(args["container"]))
        elif args["exec"]:
            cli.send("exec {} {}".format(args["container"], args["exec"]))
        self.settings[self.name] = cli.recv()

    def final(self):
        return self.settings[self.name]
