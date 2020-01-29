import swapper

from formula_one.models.base import Model
from bhawan_app.models import HostelRoomBooking
from django.db import models


class HostelVisitor(Model):
    """
    Describes visitor's relation with hostel inmate and booking.
    """

    name = models.CharField(
        max_length=20,
    )

    relation = models.CharField(
        max_length = 10,
    )

    booking = models.ForeignKey(
         HostelRoomBooking,
         on_delete=models.CASCADE,
         related_name="visitor",
    )