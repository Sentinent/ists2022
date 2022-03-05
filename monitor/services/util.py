from enum import Enum

class COLOR(Enum):
    Black = '\u001b[30m'
    Red = '\u001b[31m'
    Green = '\u001b[32m'
    Yellow = '\u001b[33m'
    Blue = '\u001b[34m'
    Magenta = '\u001b[35m'
    Cyan = '\u001b[36m'
    White = '\u001b[37m'
    Reset = '\u001b[0m'

def colorize(message, mapping):
    for (s, color) in mapping.items():
        message = message.replace(s, f'{color.value}{s}{COLOR.Reset.value}')

    return message
