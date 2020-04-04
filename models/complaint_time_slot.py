import swapper
from django.db import models

from formula_one.models.base import Model

from bhawan_app.models import Timing
from bhawan_app.constants import complaint_types


class ComplaintTimeSlot(Model):
    """
    Stores the time slot for the complaint rectification
    """

    complaint_type = models.CharField(
        max_length=10,
        choices=complaint_types.COMPLAINT_TYPES,
        default=complaint_types.OTHER,
    )
    timing = models.ManyToManyField(Timing)

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        complaint_type = self.get_complaint_type_display()
        queryset = self.timing.all()
        combined_timings = ''
        for timing in queryset:
            day = timing.get_day
            start = timing.start
            end = timing.end
            combined_timings += f'{day}: {start} - {end} | '

        return f'{complaint_type} | {combined_timings}'
