from django.urls import path
from engine import views

urlpatterns = [
    # Changed '' to 'cards/'
    path('cards/', views.CardListView.as_view(), name='cards-list'), 
    # path('<int:pk>/update/', views.CardUpdateView.as_view(), name='cards-edit'),
    path('create/', views.CardCreateView.as_view(), name='cards-create'),
    path('preferences/', views.UserResponseView.as_view(), name='user-preferences'),
    path('<int:pk>/review/', views.UserReviewView.as_view(), name='user-review'),
]
