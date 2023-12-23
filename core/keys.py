from enum import Enum


class TEXTS(Enum):
    CUSTOM_NODE_NAME = "Crystools"
    LOGGER_PREFIX = "Crystools"
    CONCAT = "Concatenated"
    INACTIVE_MSG = "inactive"
    INVALID_METADATA_MSG = "Invalid metadata raw"


class CATEGORY(Enum):
    TESTING = "_for_testing"
    MAIN = "crystools"
    PRIMITIVE = "/Primitive"
    DEBUGGER = "/Debugger"
    LIST = "/List"
    SWITCH = "/Switch"
    PIPE = "/Pipe"
    IMAGE = "/Image"
    UTILS = "/Utils"


# remember, all keys should be in lowercase!
class KEYS(Enum):
    LIST = "list_string"
    PREFIX = "prefix"