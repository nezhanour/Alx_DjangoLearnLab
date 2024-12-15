from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class UserNotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        # Serialize and return notifications (create a NotificationSerializer)
        return Response({
            "notifications": [{"actor": n.actor.username, "verb": n.verb, "created_at": n.created_at} for n in notifications]
        }, status=200)

    def post(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications.update(read=True)  # Mark all notifications as read
        return Response({"detail": "All notifications marked as read."}, status=200)
