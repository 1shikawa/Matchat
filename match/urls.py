from django.urls import path
from .views import index, user, reaction, chat
from .controller import reaction_controller, chat_controller

app_name = 'match'

urlpatterns = [
    path('', index.top, name='index'),
    path('login/', index.Login.as_view(), name='login'),
    path('logout/', index.Logout.as_view(), name='logout'),
    path('users/', user.gets, name='users'),
    path('users/regist/', user.regist, name='regist'),
    path('users/profile/<int:user_id>', user.profile),
    path('users/<int:user_id>/edit/', user.edit),
    path('reactions/', reaction_controller.create, name='reactions'),
    path('matching/', reaction.matching, name='matching'),  # 追加
    path('chat/create/<int:user_id>', chat.create, name='chat_create'),  # 追加
    path('chat/show/<int:room_id>', chat.show, name='chat_show'),  # 追加
    path('chat/show/<int:room_id>/messages/', chat.messages, name='chat_messages'),  # 追加
]
