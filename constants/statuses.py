"""
Various statuses.
"""

APPROVED = "apr"
PENDING = "pen"
REJECTED = "rej"
FORWARDED = "fwd"
CONFIRMED = "cnf"
COMLAINT_STATUSES = [
    (APPROVED, "Approved"),
    (PENDING, "Pending"),
    (REJECTED, "Rejected"),
]
BOOKING_STATUSES = COMLAINT_STATUSES + [
    (FORWARDED, 'Forwarded'),
    (CONFIRMED, 'Confirmed'),
]
