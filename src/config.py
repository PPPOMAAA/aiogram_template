from dataclasses import dataclass
from typing import List

from environs import Env


@dataclass
class BotConfig:
    token: str
    admin_ids: List[int]


@dataclass
class MiscConfig:
    pass


@dataclass
class Config:
    bot: BotConfig
    misc: MiscConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        bot=BotConfig(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS")))
        ),
        misc=MiscConfig()
    )
