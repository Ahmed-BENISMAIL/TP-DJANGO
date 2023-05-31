from .models import ModelSerializer
from .models import *
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name']
class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'libelle','description','catégorie_id']        