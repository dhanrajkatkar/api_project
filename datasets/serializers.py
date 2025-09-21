from rest_framework import serializers
from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    """
    Serializer for the Dataset model.

    This serializer converts Dataset model instances to JSON format for the API,
    and validates incoming data for creating or updating Dataset instances.
    """

    # We use a ReadOnlyField to display the username of the modifier,
    # which is more user-friendly than showing the user ID.
    modified_by = serializers.ReadOnlyField(source='modified_by.username')

    class Meta:
        model = Dataset
        # Include all fields from the model in the serialization.
        fields = [
            'id',
            'data',
            'dataset_type',
            'from_date',
            'to_date',
            'modified_on',
            'modified_by'
        ]
        # The `modified_on` field should be read-only as it's automatically managed.
        read_only_fields = ['modified_on']
