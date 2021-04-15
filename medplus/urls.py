"""medplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index, name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^users/', include('users.urls')),
    url(r'^outpatients/', include('outpatients.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^pharmacy/', include('pharmacy.urls')),
    url(r'^laboratory/', include('laboratory.urls')),
    url(r'^frontoffice/', include('frontoffice.urls')),
    url(r'^purchase/', include('purchase.urls')),
    url(r'^billing/', include('billing.urls')),
    url(r'^iamadmin/', include('iamadmin.urls')),
    url(r'^finance/', include('finance.urls')),
    #url(r'^rc/', include('rc.urls')),
    #url(r'^inventory/', include('inventory.urls')),
    url(r'^fleet/', include('fleet.urls')),
    #url(r'^pm/', include('pm.urls')),
    #url(r'^sales/', include('sales.urls')),
    url(r'^settings/', include('settings.urls')),
    url(r'^settings/', include('uzer_settings.urls')),
    url(r'^iam/', include('iamadmin.urls')),
    #url(r'^pdf/', include('dopdf.urls')),
    url(r'^signin/$',views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
]
