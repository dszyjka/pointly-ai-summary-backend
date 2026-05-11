from enum import Enum


class ResponseType(str, Enum):
    bullet_points = 'bullet_points'
    paragraph = 'paragraph'
    tldr = 'tldr'
    # more types will be add later