from django.contrib import admin
from .models import Produit
from .models import Categorie
from .models import Fournisseurr
from .models import ProduitNC
from .models import Commande
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Fournisseurr)
admin.site.register(ProduitNC)
admin.site.register(Commande)
