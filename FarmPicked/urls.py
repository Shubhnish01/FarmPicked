"""
URL configuration for FarmPicked project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from FarmPicked import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Name Changed in Django admin
admin.site.site_header = "Farm Picked Admin"
admin.site.site_title = "Farm Picked Admin Portal"
admin.site.index_title = "Welcome to Farm Picked Admin Portal"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePage, name="home"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("services/", views.services, name="services"),
    path("contactus/", views.contactus, name="contactus"),
    path("fresh-fruits/", views.freshfruits, name="fresh-fruits"),
    path("fresh-vegetables/", views.freshvegetables, name="fresh-vegetables"),
    path("privacy-policy/", views.PrivacyPolicy, name="privacy-policy"),
    path("terms_conditions/", views.terms_conditions, name="terms_conditions"),
    path("customer/", views.customer, name="customer"),
    path("faqs/", views.FAQs, name="faqs"),
    path("walletfaqs/", views.WalletFAQs, name="walletfaqs"),
    path("dealsweek/", views.DealsOfTheWeek, name="dealsweek"),
    path("bigpackdiscount/", views.BigPackDisco, name="bigpackdiscount"),
    path("combo/", views.Comboss, name="combo"),
    path("the30Corner/", views.The30Corner, name="the30Corner"),
    # feedback
    path("feedback/", views.feedb, name="feedback"),
    path("savefeedback/", views.saveFeedback, name="savefeedback"),
    path("thankyou/", views.thankyou, name="thankyou"),
    # CSRequest
    path("CSRequest/", views.CSRequest, name="CSRequest"),
    path("saveCSRequest/", views.saveCSRequest, name="saveCSRequest"),
    path("CSreqconsider/", views.CSreqconsider, name="CSreqconsider"),
    path("shop/", include("shop.urls")),
    path("checkout/", views.Checkout, name="checkout"),
    path("saveCheckout/", views.SaveCheckout, name="saveCheckout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
