from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from CustomerServiceRequest.models import Customer_Service_Request, OrderCheckout
from Feedback.models import feedback
from shop.models import (
    HomepageProductFruits,
    HomepageProductVegetable,
    FreshFruit,
    SomeCoolOfferfruits,
    TopDealsTodayfruits,
    FreshVegetables,
    SomeCoolOffervegetables,
    TopDealsTodayvegetables,
    DealsWeek,
    BigPackBiggerDiscount,
    Combos,
    The30RsCorner,
)

# from .forms import usersForm


def HomePage(request):
    homeproductfruitdata = HomepageProductFruits.objects.all()
    homeproductvegedata = HomepageProductVegetable.objects.all()
    data = {
        "homeproductfruitdata": homeproductfruitdata,
        "homeproductvegedata": homeproductvegedata,
    }
    return render(request, "index.html", data)


def aboutus(request):
    return render(request, "aboutus.html")


def services(request):
    return render(request, "services.html")


def contactus(request):
    return render(request, "contactus.html")


def DealsOfTheWeek(request):
    dealweekdata = DealsWeek.objects.all()

    data = {
        "dealweekdata": dealweekdata,
    }

    return render(request, "Dealsoftheweek.html", data)


def BigPackDisco(request):
    bigdiscountdata = BigPackBiggerDiscount.objects.all()

    data = {
        "bigdiscountdata": bigdiscountdata,
    }

    return render(request, "BigPackBiggerDis.html", data)


def Comboss(request):
    combodata = Combos.objects.all()

    data = {
        "combodata": combodata,
    }

    return render(request, "Combo.html", data)


def The30Corner(request):
    the30data = The30RsCorner.objects.all()

    data = {
        "the30data": the30data,
    }

    return render(request, "The30Corner.html", data)


# Servies dropdown


def freshfruits(request):
    freshfruitdata = FreshFruit.objects.all()
    somecoolofferfruitsdata = SomeCoolOfferfruits.objects.all()
    topdealsdata = TopDealsTodayfruits.objects.all()
    data = {
        "freshfruitdata": freshfruitdata,
        "somecoolofferfruitsdata": somecoolofferfruitsdata,
        "topdealsdata": topdealsdata,
    }
    return render(request, "FreshFruits.html", data)


def freshvegetables(request):
    freshvegedata = FreshVegetables.objects.all()
    somecooloffervegedata = SomeCoolOffervegetables.objects.all()
    topdealsvegedata = TopDealsTodayvegetables.objects.all()
    data = {
        "freshvegedata": freshvegedata,
        "somecooloffervegedata": somecooloffervegedata,
        "topdealsvegedata": topdealsvegedata,
    }
    return render(request, "FreshVegetables.html", data)


# about inherit link


def Aboutdetail(request, aboutus):
    return render(request, "aboutus.html")


# customer review


def customer(request):
    return render(request, "customer.html")


# Privacy-Policy
def PrivacyPolicy(request):
    return render(request, "Privacy-Policy.html")


# Terms & Conditions
def terms_conditions(request):
    return render(request, "Terms_Conditions.html")


# FAQs


def FAQs(request):
    return render(request, "FAQs.html")


def WalletFAQs(request):
    return render(request, "WalletFAQ.html")


# Forms Page HTML


def CSRequest(request):
    return render(request, "CSRequest.html")


def CSreqconsider(request):
    return render(request, "CSreqConsider.html")


def saveCSRequest(request):
    if request.method == "POST":
        if request.POST.get("name") == "":
            return render(request, "CSRequest.html", {"error": True})
        elif request.POST.get("email") == "":
            return render(request, "CSRequest.html", {"error": True})
        elif request.POST.get("phone") == "":
            return render(request, "CSRequest.html", {"error": True})
        elif request.POST.get("Subject") == "":
            return render(request, "CSRequest.html", {"error": True})
        elif request.POST.get("message") == "":
            return render(request, "CSRequest.html", {"error": True})
    else:
        print("invalid method")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        Subject = request.POST.get("Subject")
        message = request.POST.get("message")
        csr = Customer_Service_Request(
            CSR_name=name,
            CSR_email=email,
            CSR_phone=phone,
            CSR_Subject=Subject,
            CSR_message=message,
        )
        csr.save()
    return render(request, "CSreqConsider.html")


# Feedback from Customers


def feedb(request):
    return render(request, "FeedbackPage.html")


def thankyou(request):
    return render(request, "Thankyou.html")


def saveFeedback(request):
    if request.method == "POST":
        if request.POST.get("f_name") == "":
            return render(request, "FeedbackPage.html", {"error": True})
        elif request.POST.get("phone") == "":
            return render(request, "FeedbackPage.html", {"error": True})
        elif request.POST.get("comment") == "":
            return render(request, "FeedbackPage.html", {"error": True})
    else:
        print("invalid method")

    if request.method == "POST":
        name = request.POST.get("f_name")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")
        fb = feedback(fb_name=name, fb_phone=phone, fb_comment=comment)
        fb.save()
    return render(request, "Thankyou.html")


def Checkout(request):
    return render(request, "Checkout.html")


def SaveCheckout(request):
    if request.method == "POST":
        if request.POST.get("name") == "":
            return render(request, "Checkout.html", {"error": True})
        elif request.POST.get("email") == "":
            return render(request, "Checkout.html", {"error": True})
        elif request.POST.get("address") == "":
            return render(request, "Checkout.html", {"error": True})
        elif request.POST.get("city") == "":
            return render(request, "Checkout.html", {"error": True})
        elif request.POST.get("State") == "":
            return render(request, "Checkout.html", {"error": True})
        elif request.POST.get("zip") == "":
            return render(request, "Checkout.html", {"error": True})
        elif request.POST.get("phone") == "":
            return render(request, "Checkout.html", {"error": True})
    else:
        print("invalid method")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        addressline2 = request.POST.get("addressline2")
        city = request.POST.get("city")
        State = request.POST.get("State")
        zip = request.POST.get("zip")
        phone = request.POST.get("phone")
        cout = OrderCheckout(
            name=name,
            email=email,
            address=address,
            addressline2=addressline2,
            city=city,
            State=State,
            zip=zip,
            phone=phone,
        )
        cout.save()

    return render(request, "index.html")
