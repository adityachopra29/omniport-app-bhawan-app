"""
Various days.
"""

MONDAY = "mon"
TUESDAY = "tue"
WEDNESDAY = "wed"
THURSDAY = "thu"
FRIDAY = "fri"
SATURDAY = "sat"
SUNDAY = "sun"
WEEKDAY = f"{MONDAY},{TUESDAY},{WEDNESDAY},{THURSDAY},{FRIDAY}"
WEEKEND = f"{SATURDAY},{SUNDAY}"
DAILY = f"{WEEKDAY},{WEEKEND}"

DAYS = (
    (MONDAY, "Monday"),
    (TUESDAY, "Tuesday"),
    (WEDNESDAY, "Wednesday"),
    (THURSDAY, "Thursday"),
    (FRIDAY, "Friday"),
    (SATURDAY, "Saturday"),
    (SUNDAY, "Sunday"),
    (DAILY, "Daily"),
    (WEEKDAY, "Weekday"),
    (WEEKEND, "Weekend"),
)
