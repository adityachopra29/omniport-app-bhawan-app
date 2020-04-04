"""
Various statuses.
"""

APPROVED = "apr"
PENDING = "pen"
REJECTED = "rej"
FORWARDED = "fwd"
STATUSES = [
    (APPROVED, "Approved"),
    (PENDING, "Pending"),
    (REJECTED, "Rejected"),
]
BOOKING_STATUSES = STATUSES + [(FORWARDED, 'Forwarded')]
