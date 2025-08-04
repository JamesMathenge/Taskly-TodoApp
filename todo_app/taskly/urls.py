from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='taskly'),  # Home view
    path('del/<str:item_id>', views.remove, name='remove'),  # Delete task
]
