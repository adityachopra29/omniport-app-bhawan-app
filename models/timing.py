from formula_one.models.base import Model
from django.db import models

from bhawan_app.constants.days import DAYS
from bhawan_app.models.custom_field.multi_select import MultiSelectField


class Timing(Model):
    """
    Describes the details of a timing registered.
    """

    day = MultiSelectField(choices=DAYS, max_length=50)
    start = models.TimeField()
    end = models.TimeField(null=True, blank=True,)
    description = models.CharField(max_length=63, blank=True, null=True)

    @property
    def get_day(self):
        """
        Returns the string representation of the day
        :return: the string representation of the day
        """

        days_indexed = list(dict(DAYS).keys())
        days_list = self.day
        if isinstance(self.day, str):
            days_list = self.day.split(',')
        days_sorted_list = sorted(days_list, key=days_indexed.index)
        days_string = ",".join(days_sorted_list)
        try:
            return dict(DAYS)[days_string]
        except KeyError:
            return ",".join([dict(DAYS)[i] for i in days_sorted_list])

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        return (
            f'{self.description}: {self.get_day} from {self.start} to {self.end}'
        )
