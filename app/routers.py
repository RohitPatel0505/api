from rest_framework import routers
from .views import studentViewSet

# router = routers.SimpleRouter()
router = routers.DefaultRouter()

router.register(r'student', studentViewSet)
urlpatterns = router.urls