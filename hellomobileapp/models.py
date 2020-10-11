from django.db import models
from django.contrib.auth.models import User

class ReportList(models.Model):

	alldevices = (('Apple','แอปเปิ้ล'),
				  ('Samsung','ซัมซุง'),
				  ('Huawei','หัวเว่ย'),
				  ('OPPO','ออปโป'),
				  ('VIVO','วีโว'),
				  ('Xiaomi','เสียวหมี่'))
	status = (('Complete','สำเร็จ'),
				('Not Complete','ยังไม่สำเร็จ'))
	cus_id = models.AutoField(primary_key=True)
	brand = models.CharField(max_length=100, choices=alldevices, default='Apple')
	model_name = models.CharField(max_length=100)
	customer_name = models.CharField(max_length=200)
	pricesale = models.IntegerField(default=0)
	status = models.CharField(max_length=100, choices=status, default='Complete')

	def __str__(self):
		return self.customer_name +'-'+	self.brand +'-'+ self.model_name +'-'+ str(self.pricesale) +'-'+ str(self.status)

class AllCustomer(models.Model):
	levellist = ( ('Bronze','ทองแดง'),
					('Silver','เงิน'),
					('Gold','ทอง'),
					('Diamond','เพชร'))

	level = models.CharField(max_length=100, choices=levellist, default='Bronze')
	customer_name = models.CharField(max_length=200)
	customer_id = models.CharField(max_length=200)
	customer_tel = models.CharField(max_length=200,blank=True,null=True)
	othercontact_name = models.CharField(max_length=200,blank=True,null=True)
	othercontact_tel = models.CharField(max_length=200,blank=True,null=True)
	other = models.TextField(blank=True,null=True)
	photo = models.ImageField(upload_to="customerphoto",blank=True,null=True)

	def __str__(self):
		return '{}-{}'.format(self.customer_id,self.customer_name)

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	photoprofile = models.ImageField(default='default.png',upload_to='photo_profile',blank=True,null=True)
	usertype = models.CharField(max_length=100,null=True,blank=True,default='customer')

	def __str__(self):
		return f'{self.user.username} Profile'

class DocumentUpload(models.Model):
	levellist = ( ('Bronze','ทองแดง'),
					('Silver','เงิน'),
					('Gold','ทอง'),
					('Diamond','เพชร'))

	level = models.CharField(max_length=100, choices=levellist, default='Bronze')
	document_name = models.CharField(max_length=100)
	document = models.FileField(upload_to='alldocument')
	other = models.TextField(blank=True,null=True)
	
	def __str__(self):
		return self.document_name

class Contact(models.Model):
	msg_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=70, default="")
	phone = models.IntegerField(default="")
	desc = models.CharField(max_length=500, default="")
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name +'-'+ str(self.date)