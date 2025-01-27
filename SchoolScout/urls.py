"""SchoolScout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=False)),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),

    path('auth/', include('user_auth.urls')),
    
    path('articles/', include('core.articles.urls')),
    path('advisor/', include('core.advisor.urls')), 
    path('articles/<slug:slug>/comments/', include('core.comments.urls')),
    path('schools/<slug:slug>/courses/', include('core.courses.urls')),
    path('faculty/<slug:slug>/department/', include('core.department.urls')),
    path('schools/<slug:slug>/faculty/', include('core.faculty.urls')),
    path('schools/<slug:slug>/fees/', include('core.fees.urls')),
    # path('location/', include('core.location.urls')),
    path('schools/<slug:slug>/news/', include('core.news.urls')),
    path('schools/<slug:slug>/requirement/', include('core.requirement.urls')),
    path('schools/<slug:slug>/reviews/', include('core.reviews.urls')),
    path('student/', include('core.savedcourse.urls')),
    path('student/', include('core.savedscholarship.urls')),
    path('student/', include('core.savedschool.urls')),
    path('scholarships/', include('core.scholarships.urls')),  
    path('schools/', include('core.schools.urls')),
    path('student/', include('core.student.urls')),
    path('testimonials/', include('core.testimonials.urls')),
    path('schools/<slug:slug>/programs/', include('core.programs.urls')),      
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(template_name='swagger-ui.html', url_name='schema'), name='swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')), 
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('careerquestionoption/', include('core.careerquestionoption.urls')),
    path('careerquestionanswer/', include('core.careerquestionanswer.urls'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
