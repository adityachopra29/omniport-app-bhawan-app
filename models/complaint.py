import swapper

from formula_one.models.base import Model
from django.db import models
from bhawan_app.constants import complaint_types, statuses


class Complaint(Model):
    """
    Describes the details of a complaint registered.
    """

    hostel = models.ForeignKey(
        to=swapper.get_model_name("kernel", "Residence"), on_delete=models.CASCADE,
    )

    person = models.ForeignKey(
        to=swapper.get_model_name("Kernel", "Person"), on_delete=models.CASCADE,
    )

    complaint_type = models.CharField(
        max_length=10,
        choices=complaint_types.COMPLAINT_TYPES,
        default=complaint_types.OTHER,
    )

    status = models.CharField(
        max_length=10, choices=statuses.STATUSES, default=statuses.PENDING
    )
    description = models.TextField()
    available_from = models.TimeField()
    available_till = models.TimeField()
    room_no = models.PositiveIntegerField()
    forwarded = models.BooleanField(default=False)

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        complaint_type = self.get_complaint_type_display()
        return f"{complaint_type} issue in {self.room_no}"
