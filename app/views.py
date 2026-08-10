from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentApplication, School, NewsletterSubscriber
from django.db.models import Q
from .utils import get_status_message
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.

def home(request):

    featured_schools = School.objects.filter(
        is_active=True,
        show_on_homepage=True
    )[:3]

    context = {
        'featured_schools': featured_schools
    }

    return render(request, 'home.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')

def track_status(request):
    application = None
    error = request.session.pop('error', None)
    status_note = None
    
    if request.method == "POST":
        application_id = request.POST.get("application_id", "").strip()

        if application_id:
            try:
                application = StudentApplication.objects.get(
                    application_no = application_id
                )

                status_note = get_status_message(application)

            except StudentApplication.DoesNotExist:
                request.session['error'] = "Application not found"
                return redirect('track_status')
        
        else:
            request.session['error'] = "Please enter Application ID"
            return redirect('track_status')
                
    return render(request,'track_status.html', {
        'application': application,
        'error': error,
        'status_note': status_note
    })

def school_list(request):
    search = request.GET.get('q')
    school = School.objects.all().order_by('-established_year')
    if search:
        school = school.filter(
            Q(school_name__icontains=search) |
            Q(city__icontains=search)
        )
    
    return render(request, 'school_list.html', {'school':school})  

def school_detail(request, slug):
    school = get_object_or_404(School, slug=slug)

    primary_image = school.primary_image
    other_images = school.images.all().order_by('-created_at')

    return render(request, 'school_detail.html', {
        'school': school,
        'primary_image': primary_image,
        'other_images': other_images
    })

def apply_now(request, slug):
    school = get_object_or_404(School, slug=slug)
    saved_data = request.session.get('application_data', {})

    if request.method == "POST":

        student_name = request.POST.get('student_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        father_name = request.POST.get('father_name')
        father_mobile = request.POST.get('father_mobile')

        #Validation 
        if not all([
            student_name,
            date_of_birth,
            gender,
            father_name,
            father_mobile,
        ]):
            return render(request, 'apply_now.html',{
                'school': school,
                'data': request.POST,
                'error': 'Please fill all required fields.'
            })

        request.session['application_data'] = {
            'school_id': school.id,
            'school_slug': slug,
            'student_name': request.POST.get('student_name'),
            'date_of_birth': request.POST.get('date_of_birth'),
            'gender': request.POST.get('gender'),
            'blood_group': request.POST.get('blood_group'),
            'aadhar_number': request.POST.get('aadhar_number'),
            'religion': request.POST.get('religion'),
            'cast_category': request.POST.get('cast_category'),
            'address': request.POST.get('address'),
            'city': request.POST.get('city'),
            'state': request.POST.get('state'),
            'pin_code': request.POST.get('pin_code'),
            'apply_class': request.POST.get('apply_class'),
            'previous_school_name': request.POST.get('previous_school_name'),
            'previous_board': request.POST.get('previous_board'),
            'last_class_attended': request.POST.get('last_class_attended'),
            'year_of_passing': request.POST.get('year_of_passing'),
            'father_name': request.POST.get('father_name'),
            'father_occupation': request.POST.get('father_occupation'),
            'father_mobile': request.POST.get('father_mobile'),
            'father_email': request.POST.get('father_email'),
            'father_income': request.POST.get('father_income'),
            'mother_name': request.POST.get('mother_name'),
            'mother_occupation': request.POST.get('mother_occupation'),
            'mother_mobile': request.POST.get('mother_mobile'),
            'mother_email': request.POST.get('mother_email'),
            'declaration_confirmed': bool(request.POST.get('declaration_confirmed'))
        }

        return redirect('review_page')
    
    return render(request, 'apply_now.html', {
        'school': school,
        'data': saved_data
    })

def review_page(request):
    data = request.session.get('application_data')

    # TODO
    # Save application data into db table
    if not data:
        return redirect('school_list')
    
    school = get_object_or_404(School, slug=data['school_slug'])
    return render(request, 'review_page.html', {
        'data': data,
        'school': school})

def application_submitted(request, application_id):
    application = get_object_or_404(StudentApplication, id=application_id)

    return render(request, 'application_submitted.html', {
        'application': application})

def submit_application(request):
    if request.method == "POST":
        data = request.session.get('application_data')
        if not data:
            return redirect('home')
        
        school = get_object_or_404(School, id=data['school_id'])
        try:
            application = StudentApplication.objects.create(
                school=school,
                student_name=data['student_name'],
                date_of_birth=data['date_of_birth'],
                gender=data['gender'],
                blood_group=data['blood_group'],
                aadhar_number=data['aadhar_number'],
                religion=data['religion'],
                cast_category=data['cast_category'],
                address=data['address'],
                city=data['city'],
                state=data['state'],
                pin_code=data['pin_code'],
                apply_class=data['apply_class'],
                previous_school_name=data['previous_school_name'],
                previous_board=data['previous_board'],
                last_class_attended=data['last_class_attended'],
                year_of_passing=data['year_of_passing'],
                father_name=data['father_name'],
                father_occupation=data['father_occupation'],
                father_mobile=data['father_mobile'],
                father_email=data['father_email'],
                father_income=data['father_income'],
                mother_name=data['mother_name'],
                mother_occupation=data['mother_occupation'],
                mother_mobile=data['mother_mobile'],
                mother_email=data['mother_email'],
                declaration_confirmed=data['declaration_confirmed']
            )
            request.session.pop('application_data', None)

            return redirect('application_submitted', application_id=application.id)

        except ValidationError as e:

            return render(request, 'review_page.html', {'data': data, 'school': school, 'errors': e.message_dict
            })

    return redirect('home')

def sitemap(request):
    return render(request, 'sitemap.html')

def terms_of_use(request):
    return render(request, 'terms_of_use.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def subscribe_newsletter(request):

    if request.method == "POST":

        email = request.POST.get("email").lower().strip()

        try:
            validate_email(email)

            obj, created = NewsletterSubscriber.objects.get_or_create(
                email=email
            )

            if created:
                messages.success(request, "Subscribed successfully!")
            else:
                messages.info(request, "You are already subscribed!")

        except ValidationError:
            messages.error(request, "Please enter a valid email address.")

    return redirect(request.META.get('HTTP_REFERER', 'home'))
