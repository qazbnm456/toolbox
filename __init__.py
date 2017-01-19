"""Configuration file for toolbox addon"""

from .System import version
from .Container import rm
from .Addon import placeholder # Toolbox class

__override__ = {
    'System.version': 'Version',
    'Container.rm': 'Rm',
    'Addon.placeholder': 'Toolbox',
}

__argparse__ = [
    {
        'namespace': "Version",
        'position': "Self",
        'subcommand': None,
        'actions': [
            "add_argument('--client', '-c',    \
                          action='store_true', \
                          dest='client',       \
                          help='Show the Tsaotun version information')",
        ],
    },
    {
        'namespace': "Container",
        'position': "Child",
        'subcommand': "rm",
        'actions': [
            "add_argument('--clear',            \
                           action='store_true', \
                           dest='clear',        \
                           help='Remove all dead and alive containers. \
                                 You still need to give a whatever container ID.')",
        ],
    },
    {
        'namespace': "System",
        'position': "Child",
        'subcommand': None,
        'actions': [
            "add_parser('{}',                                                  \
                         formatter_class=argparse.RawDescriptionHelpFormatter, \
                         usage='%(prog)s [OPTIONS] [COMMANDS]')".format(__name__),
            "add_argument('container',         \
                          type=str,            \
                          metavar='CONTAINER', \
                          help='Container to execute')",
            "add_argument('--shell',            \
                           action='store_true', \
                           help='Enter into the shell of given container.')",
            "add_argument('--show-ip',          \
                           action='store_true', \
                           help='Show the IP address of given container.')",
            "add_argument('--exec',  \
                           type=str, \
                           help='Execute a command.')",
        ]
    },
]
