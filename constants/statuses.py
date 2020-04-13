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
COMLAINT_STATUSES_DICT = {
    'RESOLVED':  RESOLVED,
    'UNRESOLVED': UNRESOLVED,
    'PENDING': PENDING,
}
BOOKING_STATUSES_DICT = {
    'APPROVED': APPROVED,
    'PENDING': PENDING,
    'REJECTED': REJECTED,
    'FORWARDED': FORWARDED,
    'CONFIRMED': CONFIRMED,
}