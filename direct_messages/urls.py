# urls.py
from django.urls import path
from .views import SendDirectMessageView, InboxView,ChatView

app_name = "direct_messages"

urlpatterns = [
    path('send/<int:recipient_id>/', SendDirectMessageView.as_view(), name='send_direct_message'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    # path('chat/', ChatView.as_view(), name='chat'),
    path('chat/<int:partner_id>/', ChatView.as_view(), name='chat'),

]

