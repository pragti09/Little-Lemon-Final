from django.urls import path, include
# from .views import menuview, bookingview
from .views import MenuItemsView, SingleMenuItemView,BookingViewSet
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path('booking/', bookingview.as_view()),
    # path('menu/', menuview.as_view()),
    
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),    
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]