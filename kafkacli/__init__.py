from kafkacli.args_parser import (
    ArgsParser, __version__
)

from kafkacli.killer import (
    Killer,
)

from kafkacli.k import (
    K,
)

VERSION = tuple([int(v) for v in __version__.split('.')])