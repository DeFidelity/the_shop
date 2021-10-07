from shop.models import Promotion

def promo(request):
    return {
    'promotion':Promotion.objects.all(),
    }
