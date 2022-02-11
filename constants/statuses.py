"""
Various statuses.
"""

APPROVED = "apr"
PENDING = "pen"
REJECTED = "rej"
FORWARDED = "fwd"
CONFIRMED = "cnf"
RESOLVED = "res"
UNRESOLVED = "unr"
LIVING = "liv"
NOT_LIVING = "nlv"
NON_DINING = "nd"

COMLAINT_STATUSES = [
    (RESOLVED, "Resolved"),
    (PENDING, "Pending"),
    (UNRESOLVED, "Unresolved"),
]
BOOKING_STATUSES = [
    (APPROVED, "Approved"),
    (PENDING, "Pending"),
    (REJECTED, "Rejected"),
    (FORWARDED, 'Forwarded'),
    (CONFIRMED, 'Confirmed'),
]
FEE_TYPES = [
    (LIVING, "LIVING"),
    (NOT_LIVING, "NOT LIVING"),
    (NON_DINING, "NON DINING"),
]

COMLAINT_STATUSES_MAP = {
    'RESOLVED':  RESOLVED,
    'UNRESOLVED': UNRESOLVED,
    'PENDING': PENDING,
}
BOOKING_STATUSES_MAP = {
    'APPROVED': APPROVED,
    'PENDING': PENDING,
    'REJECTED': REJECTED,
    'FORWARDED': FORWARDED,
    'CONFIRMED': CONFIRMED,
}
FEE_TYPES_MAP = {
    'LIVING': LIVING,
    'NOT LIVING': NOT_LIVING,
    'NON DINING': NON_DINING,
}