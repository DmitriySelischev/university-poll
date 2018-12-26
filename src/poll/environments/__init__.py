import os
from .base import BaseEnvironmentConfig

ENV = os.environ.get('ENV', 'dev').lower()

if ENV == 'dev':
    from .dev import DevEnvironmentConfig

    env = DevEnvironmentConfig()
elif ENV == 'prod':
    from .prod import ProdEnvironmentConfig

    env = ProdEnvironmentConfig()
else:
    env: BaseEnvironmentConfig = None
    raise RuntimeError('Cannot resolve config for environment \'{}\''
                       .format(ENV))
