from .base import BaseEnvironmentConfig

__all__ = [
    'ProdEnvironmentConfig'
]


class ProdEnvironmentConfig(BaseEnvironmentConfig):
    pass


config: BaseEnvironmentConfig = ProdEnvironmentConfig
