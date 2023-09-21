from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import ContactMe
from django.views import View

# from . import

posts_details = []


# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "my_blog/index.html")


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "my_blog/contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/form-sent.html")
        else:
            return render(request, "my_blog/contact.html", {"form": form})


# the general information page
class AboutView(View):
    def get(self, request):
        return render(request, "my_blog/about.html")


class NewsView(View):
    def get(self, request):
        return render(request, "my_blog/news.html")


class TrendingView(View):
    def get(self, request):
        return render(request, "my_blog/trending.html")


class PlacesView(View):
    def get(self, request):
        return render(request, "my_blog/places.html")


# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             customer_communicated = ContactMe(
#                 firstname=form.cleaned_data["fullname"],
#                 lastname=form.cleaned_data["lastname"],
#                 message=form.cleaned_data["message"],
#             )
#             customer_communicated.save()
#         return HttpResponseRedirect("form_sent")

#     form = ContactForm()
#     return render(request, "my_blog/contact.html", {"form": form})


class FormSentView(View):
    def get(self, request):
        return render(request, "my_blog/form_sent.html")
