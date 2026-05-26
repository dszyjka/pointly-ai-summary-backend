from enum import Enum


class ResponseType(str, Enum):
    bullet_points = 'Bullet Points'
    standard = 'Standard'
    tldr = 'TL;DR'
    # more types will be add later