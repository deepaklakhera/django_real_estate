from django.shortcuts import render,redirect
from.models import Contact
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    print(request.POST)
    if request.method=="POST":
        print("hello")
        listing_id=request.POST['listing_id']
        name=request.POST['name']
        listing=request.POST['listing']        
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']

    if request.user.is_authenticated:
        user_id=request.user.id
        has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
        if has_contacted:
            print('error! Already Enquired')
    contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
    contact.save()
    send_mail(
    'Property Enquiry',
    'Enquiry.',
    'deepaklakhera24hr@gmail.com',
    ['deepaklakhera24hr@gmail.com', 'deepak.lakhera1994@gmail.com'],fail_silently=False
)
    return redirect('/listings/'+listing_id)