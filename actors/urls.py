from django.urls import path
from actors.views import ActorListCreate, ActorRetrieveUpdateDestroy


urlpatterns = [
    path('actors/', ActorListCreate.as_view(), name='actor-list-create'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroy.as_view(), name='actor-detail-update-delete'),
]
