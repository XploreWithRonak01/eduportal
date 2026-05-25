from django.db import models
from django.core.validators import RegexValidator
import uuid

mobile_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message="Enter valid 10 digit mobile number"
)

aadhar_validator = RegexValidator(
    regex=r'^\d{12}$',
    message='Enter valid 12 digit Aadhar number'
)

# Create your models here.
class School(models.Model):
    BOARD_CHOICES = [
        ('CBSE', 'CBSE'),
        ('RBSE', 'RBSE'),
        ('ICSE', 'ICSE'),
        ('IB', 'IB'),
        ('STATE', 'State Board'),
        ('OTHER', 'Other'),
    ]

    SCHOOL_TYPE_CHOICES = [
        ('PLAY', 'Play School'),
        ('PRIMARY', 'Primary School'),
        ('PUBLIC', 'Public School'),
        ('SECONDARY', 'Secondary School'),
        ('SENIOR_SECONDARY', 'Senior Secondary School'),
    ]

    MEDIUM_CHOICES = [
        ('ENGLISH', 'English'),
        ('HINDI', 'Hindi'),
        ('Hindi & English', 'Hindi & English'),
    ]

    # Basic Information
    school_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    board = models.CharField(
        max_length=100,
        choices=BOARD_CHOICES,
        default='CBSE'
    )
    medium = models.CharField(
        max_length=100,
        choices=MEDIUM_CHOICES,
        default='ENGLISH'
    )
    established_year = models.PositiveIntegerField()
    primary_image = models.ImageField(upload_to='schools/')
    description = models.TextField(null=True, blank=True)

    # Location
    full_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10, blank=True, null=True)

    school_type = models.CharField(
        max_length=100,
        choices=SCHOOL_TYPE_CHOICES,
        default='SENIOR_SECONDARY'
    )
    student_teacher_ratio = models.CharField(max_length=20,blank=True,null=True, help_text="Enter ratio in format like 25:1")
    campus_size = models.CharField(max_length=100, blank=True, null=True, help_text="Example: 8 Acres / 1200 Sq. meters")
    affiliation_number = models.CharField(max_length=20, blank=True, null=True, help_text="Enter valid affiliation number (e.g. 1730123)")

    total_seats = models.PositiveIntegerField(default=0)
    admission_last_date = models.DateField()
    admission_open = models.BooleanField(default=True)

    # Contact Info
    mobile = models.CharField(max_length=10, validators=[mobile_validator])
    email = models.EmailField()
    website = models.URLField(blank=True)

    # Timing Info
    school_time = models.CharField(max_length=100)
    visiting_hours = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    show_on_homepage = models.BooleanField(default=False)

    # System
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schools'
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

        indexes = [
            models.Index(fields=['school_name']),
            models.Index(fields=['city']),
            models.Index(fields=['board']),
            models.Index(fields=['school_type']),
        ]

    def __str__(self):
        return self.school_name

# School Gallery Model:---
class SchoolImage(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='school_gallery/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'school_images'
        verbose_name = 'School Image'
        verbose_name_plural = 'School Images'

    def __str__(self):
        return f"{self.school.school_name} Image"
    
# School Facility Model:---
class SchoolFacility(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='facilities')
    facility_name = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=100,default='fas fa-school')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'school_facilities'
        verbose_name = 'School Facility'
        verbose_name_plural = 'School Facilities'

    def __str__(self):
        return f"{self.school.school_name} - {self.facility_name}"

# School Document Model:---
class AdmissionRequiredDocument(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='documents')
    document_name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'admission_required_docs'
        verbose_name = 'Admission Required Document'
        verbose_name_plural = 'Admission Required Documents'

    def __str__(self):
        return f"{self.school.school_name} - {self.document_name}"

#Student Application Form Model:---
class StudentApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ]
    CATEGORY_CHOICES = [
    ('GENERAL', 'General'),
    ('OBC', 'OBC'),
    ('SC', 'SC'),
    ('ST', 'ST'),
    ('EWS', 'EWS'),
    ('OTHER', 'OTHER')
    ]
    CLASS_CHOICES = [
    ('PLAYGROUP', 'Playgroup'),
    ('NURSERY', 'Nursery'),
    ('LKG', 'LKG'),
    ('UKG', 'UKG'),
    ('PREP', 'Prep'),
    ('CLASS_1', 'Class 1'),
    ('CLASS_2', 'Class 2'),
    ('CLASS_3', 'Class 3'),
    ('CLASS_4', 'Class 4'),
    ('CLASS_5', 'Class 5'),
    ('CLASS_6', 'Class 6'),
    ('CLASS_7', 'Class 7'),
    ('CLASS_8', 'Class 8'),
    ('CLASS_9', 'Class 9'),
    ('CLASS_10', 'Class 10'),
    ('CLASS_11_SCIENCE', 'Class 11 (Science)'),
    ('CLASS_11_COMMERCE', 'Class 11 (Commerce)'),
    ('CLASS_11_HUMANITIES', 'Class 11 (Humanities)'),
    ('CLASS_11_AGRICULTURE', 'Class 11 (Agriculture)'),
    ('CLASS_12_SCIENCE', 'Class 12 (Science)'),
    ('CLASS_12_COMMERCE', 'Class 12 (Commerce)'),
    ('CLASS_12_HUMANITIES', 'Class 12 (Humanities)'),
    ('CLASS_12_AGRICULTURE', 'Class 12 (Agriculture)'),
    ]
    INCOME_CHOICES = [
    ('Below ₹2 Lakhs', 'Below ₹2 Lakhs'),
    ('2 Lakhs - ₹5 Lakhs', '₹2 Lakhs - ₹5 Lakhs'),
    ('₹5 Lakhs - ₹10 Lakhs', '₹5 Lakhs - ₹10 Lakhs'),
    ('₹10 Lakhs - ₹15 Lakhs', '₹10 Lakhs - ₹15 Lakhs'),
    ('Above ₹15 Lakhs', 'Above ₹15 Lakhs'),
    ]
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='applications')

    # Student Information
    application_no = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )
    student_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ]
    )
    
    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES,
        blank=True
    )
    aadhar_number = models.CharField(max_length=12, validators=[aadhar_validator])
    religion = models.CharField(max_length=50, blank=True)
    
    cast_category = models.CharField(
            max_length=20,
            choices=CATEGORY_CHOICES
    )

    # Student Address
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)

    apply_class = models.CharField(
        max_length=30,
        choices=CLASS_CHOICES
    )

    # Student Previous School
    previous_school_name = models.CharField(max_length=255, blank=True)
    previous_board = models.CharField(max_length=100, blank=True)
    last_class_attended = models.CharField(max_length=50, blank=True)
    year_of_passing = models.PositiveIntegerField(blank=True, null=True)

    # Student Parent / Guardian Information
    father_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_mobile = models.CharField(max_length=15, validators=[mobile_validator])
    father_email = models.EmailField(blank=True, null=True)
    
    father_income = models.CharField(
        max_length=100,
        choices=INCOME_CHOICES,
        blank=True
    )

    mother_name = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_mobile = models.CharField(max_length=15, validators=[mobile_validator])
    mother_email = models.EmailField(blank=True, null=True)

    declaration_confirmed = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.application_no:
            self.application_no = f"EP-{uuid.uuid4().hex[:8].upper()}"

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'student_applications'
        verbose_name = 'Student Application'
        verbose_name_plural = 'Student Applications'

    def __str__(self):
        return f"{self.application_no} - {self.student_name}"
    
# Newsletter Subscriber :---
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email