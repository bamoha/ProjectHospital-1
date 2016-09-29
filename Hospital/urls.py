from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
                url(r'^admin/', admin.site.urls),
                url(r'^$', views.index,   name='index'),
                url(r'^index/', views.index,   name='index'),
                url(r'^about/hospital/$', views.about, name='about'),
                url(r'^about/mission/$', views.mission, name='about'),
                url(r'^about/vision/$', views.vision, name='about'),
                url(r'^contact/book/$', views.book, name='about'),
                url(r'^contact/complaint/$', views.complaint, name='about'),
                url(r'^contact/enquiry/$', views.enquiry, name='about'),
                url(r'^careers/$', views.careers, name='about'),
                url(r'^department/burns/$', views.burns, name='about'),
                url(r'^department/general_surgery/$', views.surgery, name='about'),
                url(r'^department/general_medical/$', views.medical, name='about'),
                url(r'^department/ortho/$', views.ortho, name='about'),
                url(r'^department/therapy/$', views.therapy, name='about'),

]




