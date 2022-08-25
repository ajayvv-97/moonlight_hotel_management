from django.db import models

class Customer_tb(models.Model):
    ID_PROOF_TYPE = (
			('adhar card', 'adhar card'),
			('voter id', 'voter id'),
			('licence', 'lience'),
			)
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('other','other'),
        )

    cuts_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True ,null =True)
    cuts_password=models.TextField()
    cuts_address=models.TextField()    
    cuts_ph = models.CharField(max_length=12)
    gender=models.CharField(max_length=200, null=True, choices=GENDER)
    id_proof_type=models.CharField(max_length=200, null=True, choices=ID_PROOF_TYPE)
    id_proof_number=models.TextField()
    cuts_image=models.ImageField(upload_to='customer_pic')
    status=models.TextField()

    def __str__(self):
        return self.cuts_name
    
    class Meta:
        db_table='Customer_tb'
    
