from formula_one.models.base import Model
from django.db import models

from bhawan_app.constants import statuses, days


class Timing(Model):
    """
    Describes the details of a timing registered.
    """

    # Relationship with the facility or event entity
    day = models.CharField(max_length=50, choices=days.DAYS,)
    start = models.TimeField()
    end = models.TimeField(null=True, blank=True,)
    description = models.CharField(max_length=63, blank=True, null=True)

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        return f"On {self.day} from {self.start} to {self.end}"
