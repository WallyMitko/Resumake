from dataclasses import dataclass
from enum import Enum
import uuid


class EntryCategory(Enum):
    WORK = "Work Experience"
    PROJECT = "Projects"
    VOLUNTEER = "Volunteer Experience"
    EDUCATION = "Education"


@dataclass
class BulletPoint:
    body: str
    tags: list[str]
    id: str

    def __init__(self, body: str, tags: list[str]):
        self.body = body
        self.tags = tags
        self.id = str(uuid.uuid4())

    def __eq__(self, other):
        return self.id == other.id


@dataclass
class Entry:
    category: EntryCategory
    title: str
    subtitle: str
    start_year: int
    start_month: int    # 0=none, 1-12=Jan-Dec
    start_day: int      # 0=none
    end_year: int
    end_month: int
    end_day: int
    is_ongoing: bool
    bullet_points: list[BulletPoint]
    tags: list[str]
    id: str

    def __init__(self, category: EntryCategory, title: str, subtitle: str, start_year: int, start_month: int,
                 start_day: int, end_year: int, end_month: int, end_day: int, is_ongoing: bool,
                 bullet_points: list[BulletPoint], tags: list[str]):
        self.category = category
        self.title = title
        self.subtitle = subtitle
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.end_year = end_year
        self.end_month = end_month
        self.end_day = end_day
        self.is_ongoing = is_ongoing
        self.bullet_points = bullet_points
        self.tags = tags
        self.id = str(uuid.uuid4())

    def __eq__(self, other):
        return self.id == other.id
