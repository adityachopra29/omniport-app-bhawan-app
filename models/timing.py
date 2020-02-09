from formula_one.models.base import Model
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from bhawan_app.constants import statuses, days


class Timing(Model):
    """
    Describes the details of a timing registered.
    """

    # Relationship with the facility or event entity
    _limits = models.Q(
        app_label='bhawan_app',
        model='facility',
    ) | models.Q(
        app_label='bhawan_app',
        model='event',
    )

    day = models.CharField(
        max_length=50,
        choices=days.DAYS,
    )
    start = models.TimeField()
    end = models.TimeField(
        null=True,
        blank=True,
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=_limits,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type',
         'object_id',
    )
    description = models.CharField(
        max_length=50,
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        return f"On {self.day} from {self.start} to {self.end}'s booking."
