from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

CustomUser = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  # e.g., "liked your post"
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # To mark if the notification has been read
