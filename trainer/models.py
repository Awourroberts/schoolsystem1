from django.db import models


class Trainer(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    course=models.CharField(max_length=50)
    work_experience=models.CharField(max_length=50)
    contract=models.FileField(upload_to="images/",null=True)
    trainer_gender=models.FileField(max_length=50)
    trainer_id=models.PositiveIntegerField()
    profile_picture=models.ImageField(upload_to="images/",null=True)
    biograph=models.TextField(max_length=300,null=True)
    date_hired=models.DateField()
    national_id=models.CharField(max_length=20)
    language_choices=(
    ("Eng","english"),
    ("Kisw","kiswahili")
    )
    language=models.CharField(max_length=20, choices=language_choices,null=True)
    age=models.PositiveBigIntegerField()
    courses=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    gender_choices=(
    ("Female",'Female'),
    ("Male",'Male')
    )
    gender=models.CharField(max_length=20, choices=gender_choices,null=True)


# Create your models here.
