"""
The type of complaints in any Bhawan
"""

ELECTRIC = "ele"
TOILET = "toi"
CARPENTRY = "car"
CLEANING = "cle"
OTHER = "oth"

COMPLAINT_TYPES = (
    (ELECTRIC, "Electric"),
    (TOILET, "Toilet"),
    (CARPENTRY, "Carpentry"),
    (CLEANING, "Cleaning"),
    (OTHER, "Other"),
)
COMPLAINT_TYPES_DICT = {
    'ELECTRIC': ELECTRIC,
    'TOILET': TOILET,
    'CARPENTRY': CARPENTRY,
    'CLEANING': CLEANING,
    'OTHER': OTHER,
}
