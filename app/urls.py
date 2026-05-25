from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('track-status/', views.track_status, name='track_status'),
    path('school-list/', views.school_list, name='school_list'),
    path('school-detail/<slug:slug>/', views.school_detail, name='school_detail'),
    path('apply-now/<slug:slug>/', views.apply_now, name='apply_now'),
    path('review-page/', views.review_page, name='review_page'),
    path('application-submitted/<int:application_id>/',views.application_submitted, name='application_submitted'),
    path('submit-application/', views.submit_application, name='submit_application'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    
]