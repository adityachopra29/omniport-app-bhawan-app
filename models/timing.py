from formula_one.models.base import Model
from django.db import models
from bhawan_app.constants import statuses, days
from bhawan_app.models import Facility


class Timing(Model):
    """
    Describes the details of a complaint registered.
    """

    day = models.CharField(
        max_length=50,
        choices=days.DAYS,
    )
    start = models.TimeField()
    end = models.TimeField()
    facility = models.ForeignKey(
         Facility,
         on_delete=models.CASCADE,
         related_name='timings',
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        return f"On {self.day} from {self.start} to {self.end}'s booking."
