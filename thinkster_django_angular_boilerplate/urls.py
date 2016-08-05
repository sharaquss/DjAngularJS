from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from authentication.views import AccountViewSet, LoginView
from thinkster_django_angular_boilerplate.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    # API endpoint for registering
    url(r'^api/v1/', include(router.urls)),
    # API endpoint for logging in
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    # if request url does
    url('^.*$', IndexView.as_view(), name='index'), #this url must be last, always
)

# urlpatterns = [
#     # '',
#     url(r'^api/v1', include(router.urls)),
#     url('^.*$', IndexView.as_view(), name='index'), #this url must be last, always
# ]

