from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import signUp, ProductsAvailable
from django.db.models import Q



# Create your views here.
# @login_required
# def home(request):
#     return render(request, 'base.html')
@api_view(['POST'])
def signup(request):
    email1 = request.data['email']
    try:
        user = signUp.objects.get(email = email1)
    except ObjectDoesNotExist:
        user = None
    if user is not None:
        return HttpResponse("User already exists")
    elif user is None:
        newUser = signUp()
        newUser.category = request.data['category']
        newUser.first_name = request.data['first_name']
        newUser.last_name = request.data['last_name']
        newUser.password = request.data['password']
        newUser.email = request.data['email']
        newUser.contact = request.data['contact']
        newUser.companyName = request.data['companyName']
        newUser.address = request.data['address']
        newUser.save()
        user = authenticate(username=newUser.email, password=newUser.password)
    # login(request, user)
    return HttpResponse("success")

@api_view(['POST'])
def login(request):
    email1 = request.data['email']
    password1 = request.data['password']
    try:
        user = signUp.objects.get(email = email1)
    except ObjectDoesNotExist:
        user = None
    if user is None:
        return HttpResponse("No user")
    elif user is not None:
        if password1 == user.password:
            return HttpResponse("success")
        else:
            return  HttpResponse("Email and password do not match")


@api_view(['POST'])
def productSaved(request):
    newProduct = ProductsAvailable()
    newProduct.supplier = request.data['supplier']
    newProduct.productType = request.data['productType'] # which type of milk (full cream, cow, buffalo)
    newProduct.quantity = request.data['quantity']
    newProduct.expectedDelivery = request.data['expectedDelivery']
    newProduct.expiryDate = request.data['expiryDate']
    newProduct.location = request.data['location']
    newProduct.save()
    return HttpResponse("Check")


@api_view(['POST'])
def search(request):
    expectedDelivery = request.data['expectedDelivery']
    try:
        product = ProductsAvailable.objects.get(expectedDelivery = expectedDelivery)
        #print(product)
    except ObjectDoesNotExist:
        product = None
    if product is None:
        return HttpResponse("No product available")
    elif product is not None:
        q_list = ProductsAvailable.objects.all().values('id', 'productType', 'quantity', 'expiryDate', 'location', 'supplier','expectedDelivery').order_by('productType')
        #print(q_list)
        q_list = q_list.filter(expectedDelivery=expectedDelivery)
        #print(q_list)
        # if product:
        #     q_list = q_list.filter(Q(location=product))
        #     print(q_list)
        return HttpResponse("Check")

#
# @api_view(['POST'])
# def wastageCheck(request):
#     email = request.signUp.email
#     try:
#         product = ProductsAvailable.objects.get(email = email)
#     except ObjectDoesNotExist:
#         product=None
#     if product is None:
#         return  HttpResponse("No products available")
#     elif product is not None:
#         q_list = ProductsAvailable.objects.all().values('id', 'productType', 'quantity', 'expiryDate', 'location', 'supplier').order_by('productType')
#         q_list = q_list.filter(email=email)
#         for product in q_list:
#             if expiryDate - currentDate ==1
#                 return HttpResponse("orphanges")
#             elif expiryDate - currentDate ==0
#                 return HttpResponse("petstores")





@api_view(['POST'])
def orderPlaced(request, id):
    quantity = request.data['quantity']
    product = ProductsAvailable.objects.get(id = id)
    product.quatity = product.quatity - quantity
    product.save()
    # This is not tested yet


    # def profileSupplier(request):
#     newSupplier = Supplier()
#     newSupplier.companyName = request.data['companyName']
#     newSupplier.address = request.data['address']
#     newSupplier.save()
#     return  HttpResponse("Check")
#
#
# def profileReceiver(request):
#     newReceiver = Receiver()
#     newReceiver.shopName = request.data['shopName']
#     newReceiver.address = request.data['address']
#     newReceiver.save()
#     return  HttpResponse("Check")


# def login_success(request):
#     test = request.user.first_name
#     test1 = request.user.profile.email_confirmed
#     if test1 == True:
#         if test == '0':
#             return redirect('supplier/')
#         else:
#             return redirect('receiver/')
#     return HttpResponse("success")


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})
# @api_view(['POST'])
# def bla(request):
#     Name = request.data['name']
#     newobj = example()
#     newobj.name = Name
#     newobj.save()
#     return HttpResponse("success")