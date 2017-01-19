"""This module contains `docker container rm` class"""

from docker.errors import APIError
from tsaotun.lib.Docker.Container.command import Command
from tsaotun.cli import Tsaotun


class Rm(Command):
    """This class implements `docker container rm` command"""

    name = "container rm"
    require = []

    def __init__(self):
        Command.__init__(self)
        self.settings[self.name] = None

    def eval_command(self, args):
        try:
            containers = args["containers"]
            clear = args["clear"]
            del args["containers"]
            del args["clear"]
            Ids = []
            if clear:
                cli = Tsaotun()
                cli.send('ps -a --format {{Id}}')
                ress = cli.recv()
                if ress:
                    ress = ress.split('\n')
                    ress = [res[0:4] for res in ress]
                    for Id in ress:
                        Ids.append(Id)
                        args['container'] = Id
                        self.client.remove_container(**args)
            else:
                for Id in containers:
                    Ids.append(Id)
                    args['container'] = Id
                    self.client.remove_container(**args)
            self.settings[self.name] = '\n'.join(Ids)

        except APIError as e:
            raise e

    def final(self):
        return self.settings[self.name]
