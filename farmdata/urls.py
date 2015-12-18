from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from farmdata.core.auth.jwt import JWTLoginView, JWTSignUpView
from farmdata.core.views import UserViewSet, FarmViewSet, CropViewSet, UnitViewSet, UnitConversionViewSet, FieldViewSet
from farmdata.farm_admin.views import ConfigurationViewSet
from farmdata.harvest.views import HarvestViewSet

# Django REST framework API routing
router = DefaultRouter()

# API endpoints
router.register(r'users', UserViewSet)
router.register(r'farms', FarmViewSet)
router.register(r'crops', CropViewSet)
router.register(r'units', UnitViewSet)
router.register(r'unit-conversions', UnitConversionViewSet)
router.register(r'fields', FieldViewSet)

# Harvest
router.register(r'harvests', HarvestViewSet)

# Seed

# Soil

# Comments

# Labor

# Admin
router.register(r'configurations', ConfigurationViewSet)


# Construct URLs
urlpatterns = patterns(
	'',

	# API registration
	url(r'^api/', include(router.urls)),

	# Django admin views
    url(r'^api-admin/', include(admin.site.urls)),

    # API Authentication
    url(r'^api/auth/sign-up/', JWTSignUpView.as_view(), name='sign-up'),
    url(r'^api/auth/login/', JWTLoginView.as_view(), name='login'),
)

# DEBUG mode only URLs
if settings.DEBUG:
	urlpatterns += patterns (
		'',

		# REST framework browsable API login/logout views
		url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

		# API documentation
		url(r'^api-docs/', include('rest_framework_swagger.urls')),
	)

	# Media files URL
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

	# Static files URL
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
