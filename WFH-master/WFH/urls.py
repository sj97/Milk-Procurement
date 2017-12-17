"""WFH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Milk import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', core_views.home, name='home'),
    url(r'login/$', core_views.login),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^productsave/$', core_views.productSaved),
    url(r'^search/$', core_views.search),
    #url(r'^bla/$', core_views.bla),
    #url(r'^supplier/$', core_views.bla),
    #url(r'^receiver/$', core_views.bla),
]


