from django.db import models

# Create your models here.
class Patient(models.Model):

    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    state_choices = (
        ('Andhra Pradesh','Andhra Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh','Himachal Pradesh'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Maharashtra','Maharashtra')
    )

    maritual_choices = (
        ('Single','Single'),
        ('Married' ,'Married'),
        ('Divorsed', 'Divorsed'),
        ('Widowed', 'Widowed')
    )

    disease_choices = (
        ('Topographic', 'Topographic'),
        ('Anatomic','Anatomic'),
        ('Physiological','Physiological'),
        ('Pathological','Pathological'),
        ('Etiologic','Etiologic'),
        ('Juristic','Juristic'),
        ('Epidemiological','Epidemiological'),
        ('Statistical','Statistical'),
        ('Other','Other'),
    )

    patient_name = models.CharField(max_length=30)
    contact_no = models.IntegerField(primary_key=False, null=False)
    email = models.EmailField()
    state = models.CharField(max_length=40, choices=state_choices)
    street_address = models.TextField()
    house_no = models.IntegerField(primary_key=False)
    city = models.CharField(max_length=30)
    zip = models.IntegerField()
    dob = models.DateField(auto_now=False)
    gender = models.CharField(choices=gender_choice, max_length=6)
    maritual_status = models.CharField(choices=maritual_choices, max_length=10)
    disease_category = models.CharField(choices=disease_choices, max_length=15)
    problem = models.TextField()
    previous_health_issue = models.TextField()
    date_admitted = models.DateField(auto_now=True)
    def __str__(self):
        return self.patient_name

