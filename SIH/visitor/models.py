from django.db import models

#Model of children laws and right:

class ChildrenLR(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='CLR/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 

#Model of Mens  laws and right:

class MensLR(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='MLR/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 

#Model of Women  laws and right:

class WomenLR(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='WLR/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 

#Model of Transgender laws and right:

class TransgenderLR(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='TLR/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 

#Model of Commons laws and right:

class CommonsLR(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='CLR/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 
