from django.db import models

class item(models.Model):
    item_name = models.CharField(max_length=100)
    item_hsn = models.CharField(max_length=8)
    stock= models.IntegerField(default=0)
    # Add more fields as needed
    def __str__(self):
        return self.item_name


class buyer(models.Model):
    buyer_name = models.CharField(max_length=100)
    buyer_address = models.CharField(max_length=200)
    b_city=models.CharField(max_length=30, null=True)
    b_state=models.CharField(max_length=30, null=True)
    b_pincode=models.CharField(max_length=10, null=True)
    buyer_email = models.CharField(max_length=100)
    buyer_mobile = models.CharField(max_length=15)
    buyer_gst = models.CharField(max_length=20, blank=True)
    # Add more fields as needed
    def __str__(self):
        return self.buyer_name

class seller(models.Model):
    seller_name = models.CharField(max_length=100)
    seller_address = models.CharField(max_length=200)
    s_city=models.CharField(max_length=30, null=True)
    s_state=models.CharField(max_length=30, null=True)
    s_pincode=models.CharField(max_length=10, null=True)
    seller_email = models.CharField(max_length=100)
    seller_mobile = models.CharField(max_length=15)
    seller_gst = models.CharField(max_length=20, blank=True)
    bank_name= models.CharField(max_length=30, blank=True)
    bank_acno= models.CharField(max_length=20, blank=True)
    bank_ifsc= models.CharField(max_length=20, blank=True)
    bank_branch= models.CharField(max_length=20, blank=True)
    # Add more fields as needed
    def __str__(self):
        return self.seller_name

class bill(models.Model):
    bill_no = models.CharField(max_length=4,blank=True)
    seller=models.CharField(max_length=100)
    buyer=models.CharField(max_length=100)

    def __str__(self):
        return self.bill_no


