from rest_framework import serializers
from core.models import Note

class NoteSerializer(serializers.ModelSerializer):
    """ This serializer represents the Note model. """
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Note
        fields ="__all__"
        