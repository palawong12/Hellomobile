from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ReportList, AllCustomer, Profile, DocumentUpload, Contact
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

def HomePage(request):
	return render(request, 'hellomobileapp/homepage.html')

def AboutPage(request):
	return render(request, 'hellomobileapp/about.html')

def ContactUs(request):
	if request.method =='POST':
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		phone = request.POST.get('phone','')
		desc = request.POST.get('desc','')
		contact = Contact(name=name, email=email, phone=phone, desc=desc)
		contact.save()
		messages.success(request, 'Your message was send successfully!')

	return render(request, 'hellomobileapp/contact.html')

def ShowPrice(request):
	pricesale = ReportList.objects.all()

	context = {'pricesale':pricesale}

	return render(request, 'hellomobileapp/showprice.html', context)

def InputPrice(request):
	if request.method =='POST':
		brand = request.POST.get('brand','')
		model_name = request.POST.get('model_name','')
		customer_name = request.POST.get('customer_name','')
		pricesale = request.POST.get('pricesale','')
		status = request.POST.get('status','')
		priceinput = ReportList(brand=brand, model_name=model_name, customer_name=customer_name, pricesale=pricesale, status=status)
		priceinput.save()
		messages.success(request, 'Your custmoer is created successfully!')

	return render(request, 'hellomobileapp/priceinput.html')

def Register(request):

	if request.method == 'POST':
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		username = data.get('username')
		email = data.get('email')
		password = data.get('password')

		newuser = User()
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.username = username
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
		messages.success(request, 'Your account was created successfully!')

		return redirect('home-page')

	return render(request, 'hellomobileapp/register.html')

@login_required
def SearchCustomer(request):

	if request.method == 'POST':
		data = request.POST.copy() #
		searchid = data.get('search') #100001
		print(searchid, type(searchid))
		try:
			result = AllCustomer.objects.get(customer_id=searchid)
			print('RESULT:',result)
			context = {'result':result,'check':'found'}
		except:
			context = {'result':'notfound','check':'notfound'}

		return render(request, 'hellomobileapp/search.html',context)

	return render(request, 'hellomobileapp/search.html')

@login_required	
def EditProfile(request):

	username = request.user.username
	current = User.objects.get(username=username)

	if request.method == 'POST' and request.FILES['photoprofile']:
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		#password = data.get('password')
		
		myprofile = User.objects.get(username=username)

		try:
			setprofile = Profile.objects.get(user=myprofile)
		except:
			setprofile = Profile()
			setprofile.user = myprofile
		file_image = request.FILES['photoprofile']
		file_image_name = request.FILES['photoprofile'].name
		fs = FileSystemStorage()
		filename = fs.save(file_image_name,file_image)
		upload_file_url = fs.url(filename)
		setprofile.photoprofile = upload_file_url[6:]
		setprofile.save()
		#######
		myprofile.first_name = first_name
		myprofile.last_name = last_name
		myprofile.email = email
		myprofile.save()
		messages.success(request, 'Your profile is updated successfully!')

		return redirect('edit-profile')

	context = {'data':current}
	return render(request, 'hellomobileapp/editprofile.html',context)

def ShowDocument(request):
	document = DocumentUpload.objects.all()
	context = {'document':document}
	return render(request, 'hellomobileapp/document.html', context)