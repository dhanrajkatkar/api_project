from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Dataset(models.Model):
    """
    Represents a dataset record with various types and associated data.
    """

    class DatasetType(models.TextChoices):
        """
        Enum for the different types of datasets.
        """
        ROUTE_DEVIATION = 'route_deviation', _('Route Deviation')
        POWER_DISCONNECT = 'power_disconnect', _('Power Disconnect')
        STOPPAGE_VIOLATION = 'stoppage_violation', _('Stoppage Violation')
        DEVICE_REMOVED = 'device_removed', _('Device Removed')
        SPEED_VIOLATION = 'speed_violation', _('Speed Violation')
        NIGHT_DRIVING = 'night_driving', _('Night Driving')
        HARSH_ACCELERATION = 'harsh_acceleration', _('Harsh Acceleration')
        HARSH_BREAKING = 'harsh_breaking', _('Harsh Breaking')
        HARSH_TURN = 'harsh_turn', _('Harsh Turn')
        CONTINUOUS_DRIVING = 'continous_driving', _('Continous Driving')
        CABINET_OPEN = 'cabinet_open', _('Cabinet Open')
        DRIVER_PANIC = 'driver_panic', _('Driver Panic')

    # The JSON data associated with the record.
    data = models.JSONField(
        help_text="The JSON data payload for the dataset."
    )

    # The type of dataset, chosen from the predefined enum.
    dataset_type = models.CharField(
        max_length=50,
        choices=DatasetType.choices,
        help_text="The type of violation or event."
    )

    # The start timestamp for the data's time range.
    from_date = models.DateTimeField(
        help_text="The start date and time for this data record."
    )

    # The end timestamp for the data's time range.
    to_date = models.DateTimeField(
        help_text="The end date and time for this data record."
    )

    # The timestamp when this record was last modified. Automatically updated.
    modified_on = models.DateTimeField(
        auto_now=True,
        help_text="The timestamp of the last modification."
    )

    # The user who last modified this record.
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='datasets',
        help_text="The user who created or last modified this record."
    )

    def __str__(self):
        """
        String representation of the Dataset model.
        """
        return f"{self.get_dataset_type_display()} from {self.from_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-from_date']
        verbose_name = "Dataset"
        verbose_name_plural = "Datasets"
