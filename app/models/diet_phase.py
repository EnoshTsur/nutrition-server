from enum import Enum


class DietPhase(str, Enum):
    CUT = "CUT"
    MAINTENANCE = "MAINTENANCE"
    BULK = "BULK"
