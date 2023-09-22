from django.db import models


#===================================Model of Commons laws and right:=============================================

class Commons_law(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='CL/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 

#===================================Model of children laws and right:===============================================

class Children_law(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='CLR/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 

#====================================Model of Mens  laws and right:======================================================

class Mens_law(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='MLR/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 

#=====================================Model of Women  laws and right:======================================================

class Women_law(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='WLR/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 

#=======================================Model of Transgender laws and right:====================================================

class Transgender_law(models.Model):

   title=models.CharField(max_length=50,blank=True,null=True)

   content=models.TextField(blank=True,null=True)

   file=models.FileField(upload_to='TLR/',blank=True,null=True)

   website_link=models.URLField(blank=True,null=True)

   date=models.DateTimeField(auto_now_add=True,blank=True,null=True) 

