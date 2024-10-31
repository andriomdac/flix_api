from django.urls import path
from reviews.views import ReviewListCreate, ReviewRetrieveUpdateDestroy

urlpatterns = [
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>', ReviewRetrieveUpdateDestroy.as_view(), name='review-detail-update-delete')
]
