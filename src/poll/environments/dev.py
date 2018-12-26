import os
from typing import List

from .base import BaseEnvironmentConfig

__all__ = [
    'DevEnvironmentConfig'
]


class DevEnvironmentConfig(BaseEnvironmentConfig):
    @property
    def debug(self) -> bool:
        return True

    @property
    def allowed_hosts(self) -> List[str]:
        return ['localhost', '127.0.0.1']

    @property
    def secret_key(self) -> str:
        return 'a5&7jlfpbg3)vifjdzpng!-n_@3x3$dcwnbcaw7$)d@xzfn_%-'

    @property
    def static_url(self) -> str:
        return '/static/'

    @property
    def static_root(self) -> str:
        return os.path.join(self.base_dir, 'staticfiles')

    @property
    def media_url(self) -> str:
        return '/media/'

    @property
    def media_root(self) -> str:
        return os.path.join(self.base_dir, 'mediafiles')

    @property
    def email_backend(self) -> str:
        return 'django.core.mail.backends.console.EmailBackend'

    @property
    def email_from(self) -> str:
        return 'admin@poll.local'


config: BaseEnvironmentConfig = DevEnvironmentConfig
