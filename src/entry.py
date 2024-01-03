from dataclasses import dataclass
from enum import Enum
from datetime import date


class EntryCategory(Enum):
    WORK = "Work Experience"
    PROJECT = "Projects"
    VOLUNTEER = "Volunteer Experience"
    EDUCATION = "Education"


@dataclass
class BulletPoint:
    body: str
    tags: list[str]


@dataclass
class Entry:
    category: EntryCategory
    title: str
    subtitle: str
    start_date: date
    end_date: date
    is_ongoing: bool
    bullet_points: list[BulletPoint]
    tags: list[str]
