from rest_framework import viewsets, permissions
from .models import Dataset
from .serializers import DatasetSerializer

class DatasetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datasets to be viewed or edited.

    This ViewSet provides the full set of CRUD operations:
    - GET (list, retrieve)
    - POST (create)
    - PUT / PATCH (update, partial_update)
    - DELETE (destroy)
    """
    # Define the queryset that will be used for all list and detail views.
    queryset = Dataset.objects.all().order_by('-modified_on')
    
    # Specify the serializer class to use for validating and deserializing input,
    # and for serializing output.
    serializer_class = DatasetSerializer
    
    # Set the permission classes. IsAuthenticated ensures that only logged-in
    # users can access this endpoint.
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Override the default create behavior to automatically set
        the `modified_by` field to the currently authenticated user.
        """
        serializer.save(modified_by=self.request.user)

    def perform_update(self, serializer):
        """
        Override the default update behavior to automatically set
        the `modified_by` field to the currently authenticated user on update.
        """
        serializer.save(modified_by=self.request.user)
