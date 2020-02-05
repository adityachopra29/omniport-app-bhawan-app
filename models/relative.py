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
    person = models.ForeignKey(
        to=swapper.get_model_name('Kernel', 'Person'),
        on_delete=models.CASCADE,
    )
    relation = models.CharField(
        max_length=50,
    )
    booking = models.ForeignKey(
        RoomBooking, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        return f"{self.person.name}'s {self.relation}"
