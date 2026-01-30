from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from core.models import Note
from core.serializers import NoteSerializer
# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    """ ViewSet For The Note Model """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # customize the post method to set the owner to the logged in user
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
            return Response({'status':HTTP_200_OK,'message':'Note created successfully'})
        else:
            return Response({'status':403,'message':'Authentication required to create a note'})
