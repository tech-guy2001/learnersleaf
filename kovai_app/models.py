from django.db import models
import os
from django.utils import timezone


def upload_to(instance, filename):
    return os.path.join('kovai_app/static/images/', filename)
def upload_to_stu(instance, filename):
    return os.path.join('kovai_app/static/stu_images/', filename)


# Create your models here.
class TutorRequest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    w_number = models.CharField(max_length=15,null=True,blank=True)
    password= models.CharField(max_length=100,null=True,blank=True)
    coin=models.IntegerField(null=True, blank=True)

    
   
class Requestpost(models.Model):
    
    email = models.EmailField(null=True, blank=True)
    dyr = models.TextField(verbose_name="Details of your requirement",null=True, blank=True)
    dates = models.DateTimeField(default=timezone.now) 
    level = models.CharField(max_length=50, choices=[
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Expert", "Expert"),
        ("school", "Preschool, Kindergarten, KG, Nursery"),
        ("g2", "Grade 2"),
        ("g1", "Grade 1"),
        ("g3", "Grade 3"),
        ("g4", "Grade 4"),
        ("g5", "Grade 5"),
        ("g6", "Grade 6"),
        ("g7", "Grade 7"),
        ("g8", "Grade 8"),
        ("g9", "Grade 9"),
        ("g10", "Grade 10"),
        ("IGCSE", "IGCSE"),
        ("GCSE", "GCSE"),
        ("O_level", "O level"),
        ("g11", "Grade 11"),
        ("AS_level", "AS level"),
        ("A2_level", "A2 level"),
        ("A_level", "A level"),
        ("g12", "Grade 12"),
        ("Diploma", "Diploma"),
        ("Bachelors/Undergraduate", "Bachelors/Undergraduate"),
        ("Masters/Postgraduate", "Masters/Postgraduate"),
        ("MPhil", "MPhil"),
        ("Doctorate/PhD", "Doctorate/PhD"),
    ])
    subject = models.CharField(max_length=255)
    two_subject = models.CharField(max_length=255, null=True, blank=True)
    three_subject = models.CharField(max_length=255, null=True, blank=True)
    four_subject = models.CharField(max_length=255, null=True, blank=True)
    five_subject = models.CharField(max_length=255, null=True, blank=True)
    i_want = models.CharField(max_length=50, choices=[
        ("tutoring", "Tutoring"),
        ("assignment_help", "Assignment Help")
    ])
    meeting_option = models.CharField(max_length=255, null=True,blank=True)
   
    budget = models.CharField(max_length=255)
    budget_need = models.CharField(max_length=50, choices=[
        ("per_hour", "per hour"),
        ("per_day", "per day"),
        ("per_week", "per week"),
        ("per_month", "per month")
    ])
   
    language = models.CharField(max_length=255)
    tutor_want = models.CharField(max_length=10, choices=[
        ("one", "only one"),
        ("two", "only two"),
        ("more", "As many as possible")
    ])
    need = models.CharField(max_length=10, choices=[
        ("part_time", "Part time"),
        ("full_time", "Full time")
    ])
    message = models.TextField()
    gender = models.CharField(max_length=10, choices=[
        ("male", "Male"),
        ("female", "Female"),
        ("both", "Both")
    ],null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    profile_photo = models.ImageField(upload_to=upload_to_stu,null=True)
    filename=models.CharField(max_length=200,  null=True, blank=True)
    coin=models.IntegerField(null=True, blank=True)

   
    


from django.db import models

class TutorRegistration(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    TEACHING_TYPES = [
        ('individual_teaching', 'Individual Teaching'),
        ('teaching_company', 'Teaching Company'),
    ]

    DEGREE_TYPES = [
        ('Secondary', 'Secondary'),
        ('Higher_Secondary', 'Higher Secondary'),
        ('Diploma', 'Diploma'),
        ('Graduation', 'Graduation'),
        ('AdvancedDiploma', 'Advanced Diploma'),
        ('PostGraduation', 'Post Graduation'),
        ('Doctorate/PhD', 'Doctorate/PhD'),
        ('Certification', 'Certification'),
        ('Other', 'Other'),
    ]

    ASSOCIATION_CHOICES = [
        ('parttime', 'Part time'),
        ('fulltime', 'Full time'),
        ('Correspondence', 'Correspondence / Distance Learning'),
    ]

    FEE_CHOICES = [
        ('per_hour', 'per hour'),
        ('per_month', 'per month'),
        ('per_year', 'per year'),
    ]

    INTEREST_CHOICES = [
        ('online_teaching', 'Online teaching'),
        ('offline_teaching', 'Offline teaching'),
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('both', 'Both'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    types = models.CharField(max_length=50, choices=TEACHING_TYPES, null=True, blank=True)
    strength = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=50, choices=TEACHING_TYPES, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    two_subject = models.CharField(max_length=255, null=True, blank=True)
    three_subject = models.CharField(max_length=255, null=True, blank=True)
    four_subject = models.CharField(max_length=255, null=True, blank=True)
    five_subject = models.CharField(max_length=255, null=True, blank=True)

    from_level = models.CharField(max_length=255, null=True, blank=True)
    two_from_level = models.CharField(max_length=255, null=True, blank=True)
    three_from_level = models.CharField(max_length=255, null=True, blank=True)
    four_from_level = models.CharField(max_length=255, null=True, blank=True)
    five_from_level = models.CharField(max_length=255, null=True, blank=True)
    to_level = models.CharField(max_length=255, null=True, blank=True)
    two_to_level = models.CharField(max_length=255, null=True, blank=True)
    three_to_level = models.CharField(max_length=255, null=True, blank=True)
    four_to_level = models.CharField(max_length=255, null=True, blank=True)
    five_to_level = models.CharField(max_length=255, null=True, blank=True)
    institution_name = models.CharField(max_length=255, null=True, blank=True)
    degree_type = models.CharField(max_length=50, choices=DEGREE_TYPES, null=True, blank=True)
    degree_name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    association = models.CharField(max_length=50, choices=ASSOCIATION_CHOICES, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    job_roll = models.CharField(max_length=255, null=True, blank=True)
    job_start_date = models.DateField(null=True, blank=True)
    job_end_date = models.DateField(null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    i_charge = models.CharField(max_length=20, choices=FEE_CHOICES, null=True, blank=True)
    min_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_experience = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    teaching_experience = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    online_experience = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    willing_to_travel = models.CharField(
        max_length=3, 
        choices=[('yes', 'Yes'), ('no', 'No')], 
        default='no', 
        null=True, 
        blank=True
    )
    available_for_online_teaching = models.CharField(
        max_length=3, 
        choices=[('yes', 'Yes'), ('no', 'No')], 
        default='no', 
        null=True, 
        blank=True
    )
    help_with_homework = models.CharField(
        max_length=3, 
        choices=[('yes', 'Yes'), ('no', 'No')], 
        default='no', 
        null=True, 
        blank=True
    )
    full_time_teacher = models.CharField(
        max_length=3, 
        choices=[('yes', 'Yes'), ('no', 'No')], 
        default='no', 
        null=True, 
        blank=True
    )
    interested_in = models.CharField(max_length=20, choices=INTEREST_CHOICES, null=True, blank=True)
    profile_description = models.TextField(null=True, blank=True)
    id_proof = models.ImageField(upload_to=upload_to, null=True, blank=True)
    profile_photo = models.ImageField(upload_to=upload_to,null=True)
    phone = models.CharField(max_length=15 ,null=True, blank=True)
    otp=models.BigIntegerField(null=True,blank=True)
    filename=models.CharField(max_length=500, choices=INTEREST_CHOICES, null=True, blank=True)
    coin=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name



# message__________________________________________

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender_name= models.CharField(max_length=255,null=True, blank=True)
    sender_email = models.EmailField()
    receiver_email  = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_date = models.DateTimeField(default=timezone.now) 

class teacher_addcard(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    cid=models.IntegerField(null=True, blank=True)
class student_addcard(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    cid=models.IntegerField(null=True, blank=True)