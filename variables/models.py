from django.db import models

class Variable(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document_type = models.CharField(max_length=50)
    document_number = models.IntegerField() 
    date_of_birth = models.DateField()
    city_of_residence = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.name,self.first_name,self.last_name,self.document_type,self.document_number,self.date_of_birth,
                           self.city_of_residence,self.email,self.phone_number,self.monthly_income)

