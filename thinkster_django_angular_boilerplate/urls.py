from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from authentication.views import AccountViewSet, LoginView, LogoutView
from thinkster_django_angular_boilerplate.views import IndexView
from entries.views import UserAccountEntriesViewSet, EntryViewSet, EntryDetailViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

router.register(r'entries', EntryViewSet)
accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'entries', UserAccountEntriesViewSet)

urlpatterns = patterns(
    '',
    # API endpoint for registering
    url(r'^api/v1/', include(router.urls)),
    # API endpoint for logging in
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    # endpoint for logging out
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),

    # if request url does not match any of the above, then:
    url('^.*$', IndexView.as_view(), name='index'), #this url must be last, always
)

# urlpatterns = [
#     # '',
#     url(r'^api/v1', include(router.urls)),
#     url('^.*$', IndexView.as_view(), name='index'), #this url must be last, always
# ]

