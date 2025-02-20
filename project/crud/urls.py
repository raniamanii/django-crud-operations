from django.urls import path
from crud.views import emp, show, update, destroy  # Supprime l'import de 'update'

urlpatterns = [
    path('emp/', emp, name='emp'),
    path('show/', show, name='show'),
    path('update/<str:id>/', update, name='update'),
    path('edit/<str:id>/', update, name='edit'),  # Ajout d'une route pour "edit"
    path('delete/<str:id>/', destroy, name='delete'),
]
