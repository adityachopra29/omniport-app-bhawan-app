import swapper

from django.db import models
from formula_one.models.base import Model

from bhawan_app.models import RoomBooking

class Relative(Model):
    """
    This model contains profile information of a hostel in an institute
    """

    name = models.CharField(
        max_length=50,
    )
    relation = models.CharField(
        max_length=50,
    )
    booking = models.ForeignKey(
        RoomBooking, 
        on_delete=models.CASCADE,
        related_name='relative',
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        return f"{self.person.full_name}'s {self.relation}"
        