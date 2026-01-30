

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Note(models.Model):
    """
    Represents a user's personal notes.

    Fields:
    - title: The main heading of the note.
    - content: The detailed text description.
    - created_at: Timestamp set automatically on creation.
    - owner: The user who created the note.
"""
    # The title of the note
    title = models.CharField(verbose_name= "Note Title", max_length=250)
    # The detailed content/description of the note 
    content = models.TextField(verbose_name= "Note Description")
    # Automatically records the date and time when the note is created
    created_at = models.DateTimeField(verbose_name= 'Created Time',auto_now_add=True)
    # Link to the User model; deltes ntoes if the user is deleted
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name='Owner'
        )
    def __str__(self) -> str:
        return str(self.title)