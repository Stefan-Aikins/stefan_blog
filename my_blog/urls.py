from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home-page"),
    path("about", views.AboutView.as_view(), name="about-page"),
    path("news", views.NewsView.as_view(), name="news-page"),
    path("trending", views.TrendingView.as_view(), name="trending-page"),
    path("places", views.PlacesView.as_view(), name="places-page"),
    path("contact", views.ContactView.as_view(), name="contact-page"),
    path("form_sent", views.FormSentView.as_view(), name="form-sent"),
]
