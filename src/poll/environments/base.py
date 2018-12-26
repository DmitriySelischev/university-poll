import os
from typing import List

__all__ = [
    'BaseEnvironmentConfig'
]


class BaseEnvironmentConfig:
    @property
    def base_dir(self) -> str:
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    @property
    def debug(self) -> bool:
        raise NotImplementedError

    @property
    def allowed_hosts(self) -> List[str]:
        raise NotImplementedError

    @property
    def secret_key(self) -> str:
        raise NotImplementedError

    @property
    def static_url(self) -> str:
        raise NotImplementedError

    @property
    def static_root(self) -> str:
        raise NotImplementedError

    @property
    def media_url(self) -> str:
        raise NotImplementedError

    @property
    def media_root(self) -> str:
        raise NotImplementedError

    @property
    def email_backend(self) -> str:
        raise NotImplementedError

    @property
    def email_from(self) -> str:
        raise NotImplementedError
