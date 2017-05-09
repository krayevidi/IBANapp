from django.conf.urls import include, url

from rest_framework.routers import SimpleRouter

from bank_accounts.api_views import AccountViewSet

router = SimpleRouter()
router.register(r'', AccountViewSet, base_name='account')

urlpatterns = [
    url(r'^', include(router.urls)),
]
