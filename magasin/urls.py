from django.urls import path,include
from . import views
from .views import CategoryAPIView,ProductViewset
urlpatterns = [
    path('', views.index,name='index'),
    path('listeCat/<int:id>',views.listeProduitCategorie,name='listeCat'),
    path('fournisseur',views.fournisseur,name='fournisseur'),
    path('addFournisseur',views.addFournisseur,name='addFournisseur'),
    path('addProduit',views.addProduit,name='addProduit'),
    path('register/',views.register, name = 'register'),
    path('api/category/', CategoryAPIView.as_view()),
]