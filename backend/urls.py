from rest_framework.routers import DefaultRouter

from .views import ContactApiView, AddressApiView

router = DefaultRouter()
router.register('contacts', ContactApiView)
router.register('addresses', AddressApiView)

urlpatterns = router.urls