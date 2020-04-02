from django import forms
from django.db import models
from django.utils.text import capfirst
from django.core.exceptions import ValidationError


class MultiSelectFormField(forms.MultipleChoiceField):
    """
    Class for rendering the form field on the interface
    """

    widget = forms.SelectMultiple
 
    def clean(self, value):
        """
        Cleans and runs validations against the value
        :param value: the input give by the user
        :return: the value for futher validation
        """

        if not value and self.required:
            raise forms.ValidationError(self.error_messages['required'])
        return value

 
class MultiSelectField(models.Field):
    """
    Class for defining a MultiSelectField
    """
 
    def get_internal_type(self):
        """
        Returns the type of field
        :return: the type of field
        """

        return 'CharField'
 
    def get_choices_default(self):
        """
        Returns the available choices
        :return: the available choices
        """

        return self.get_choices(include_blank=False)
 
    def formfield(self, **kwargs):
        """
        Returns the django form field instance for this field
        :return: the django form field instance for this field
        """

        defaults = {'required': not self.blank, 'label': capfirst(self.verbose_name),
                    'help_text': self.help_text, 'choices': self.choices}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return MultiSelectFormField(**defaults)

    def get_prep_value(self, value):
        """
        Removes repetition for choices
        :return: the list with unique elements
        """

        if value is None:
            return None
        combined_string = ''
        for i in value:
            combined_string += f'{i},'
        combined_string = combined_string[0:len(combined_string)-1]
        value = combined_string.split(',')
        seen = set()
        unique_day_list = [
            day for day in value if not (
                day in seen or seen.add(day)
            )
        ]
        return unique_day_list

    def get_db_prep_value(self, value, connection=None, prepared=False):
        """
        Converts the value to string so that it can be save in the database
        :return: the string of the user input
        """

        if not prepared:
            value = self.get_prep_value(value)
        if isinstance(value, str):
            return value
        elif isinstance(value, list):
            return ",".join(value)
 
    def to_python(self, value):
        """
        Converts the input value into the expected Python data type, raising
        django.core.exceptions.ValidationError if the data can't be converted.
        :param value: the value after sanitization by `clean` method
        :return: the converted value.
        """

        if value is not None:
            return value if isinstance(value, list) else value.split(',')
        return ''     

    def validate(self, value, model_instance):
        """
        Validates if the choice field is given a valid input and is one of the
        available choices
        :param value: the choices keys as list eg. - ['mon', 'thu']
        :param model_instance: object of the model where the this field exists
        """

        arr_choices = dict(self.get_choices_default()).keys()
        for opt_select in value:
            if (str(opt_select) not in arr_choices):
                raise ValidationError(self.error_messages['invalid_choice'] % {'value': value})
        return
