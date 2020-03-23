import swapper

from formula_one.models.base import Model
from django.db import models
from bhawan_app.constants import statuses


class RoomBooking(Model):
    """
    Describes the details of a complaint registered.
    """

    hostel = models.ForeignKey(
        to=swapper.get_model_name("kernel", "Residence"), on_delete=models.CASCADE,
    )
    person = models.ForeignKey(
        to=swapper.get_model_name("Kernel", "Person"), on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=10, choices=statuses.STATUSES, default=statuses.PENDING,
    )
    requested_from = models.DateField()
    requested_till = models.DateField()
    booked_by_room_no = models.PositiveIntegerField()
    forwarded = models.BooleanField(default=False)

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        return f"{self.person.full_name}'s booking."
