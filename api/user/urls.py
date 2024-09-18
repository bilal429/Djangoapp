from django.urls import path
from api.user.views import UserListView

urlpatterns = [
    path('userlist/',UserListView.as_view(),name='productlist'),

     
]
