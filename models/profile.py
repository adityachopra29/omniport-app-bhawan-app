from django.db import models

import swapper
from formula_one.models.base import Model
from formula_one.utils.upload_to import UploadTo


class Profile(Model):
    """
    This model contains profile information of a hostel in an institute
    """

    hostel = models.OneToOneField(
        to=swapper.get_model_name('kernel', 'Residence'),
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    display_picture = models.ImageField(
        upload_to=UploadTo('bhawan_app', 'hostel'), 
    )
    homepage_url = models.URLField(
        blank=True,
        verbose_name='Homepage URL',
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        hostel = self.hostel
        return f'{hostel}'
