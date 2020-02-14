import swapper

from django.db import models
from formula_one.models.base import Model

from bhawan_app.models import RoomBooking


class Visitor(Model):
    """
    This model contains profile information of a hostel in an institute
    """

    person = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Person'),
        on_delete=models.CASCADE,
    )
    booking = models.ForeignKey(
        RoomBooking,
        on_delete=models.CASCADE,
        related_name='visitor',
    )
    relation = models.CharField(
        max_length=50,
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        ResidentialInformation = swapper.load_model(
            'kernel',
            'ResidentialInformation',
        )
        full_name = self.person.full_name
        relation = self.relation
        booked_by = self.booking.person
        booked_by_name = booked_by.full_name
        booked_by_room_no = booked_by.residentialinformation.room_number
        return (
            f'{full_name} - {relation} of {booked_by_name} | '
            f'{booked_by_room_no}'
        )
