from django.db import models

import swapper
from django.contrib.contenttypes.fields import GenericRelation
from formula_one.models.base import Model
from formula_one.utils.upload_to import UploadTo
from bhawan_app.models import Timing


class Event(Model):
    """
    This model contains information about a facility of a hostel
    """

    hostel = models.ForeignKey(
        to=swapper.get_model_name("kernel", "Residence"), on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=63,)
    description = models.TextField(blank=True, null=True,)
    display_picture = models.ImageField(
        upload_to=UploadTo("bhawan_app", "hostel"),
        max_length=255,
        blank=True,
        null=True,
    )
    timings = models.ManyToManyField(Timing,)
    date = models.DateField()

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        name = self.name
        return f"{name}"
