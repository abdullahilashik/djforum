from django.contrib import admin
from django.urls import path, include
from .views import (
    HomePageView
)


admin.site.site_title = 'DJ Forum'
admin.site.site_header = 'DJ Forum'
admin.site.index_title = 'DJ Forum Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', HomePageView.as_view(), name='home'),
    path('', include('forums.urls', namespace='forums')),    
]
