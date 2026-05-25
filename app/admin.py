from django.contrib import admin
from .models import School, SchoolImage, SchoolFacility, AdmissionRequiredDocument, StudentApplication, NewsletterSubscriber

# Register your models here.
class AdmissionRequiredDocumentInline(admin.TabularInline):
    model = AdmissionRequiredDocument
    extra = 1

class SchoolFacilityInline(admin.TabularInline):
    model = SchoolFacility
    extra = 1

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'city', 'board', 'total_seats', 'show_on_homepage', 'is_active']

    search_fields = ['school_name', 'city']

    list_filter = ['board', 'school_type', 'medium', 'admission_open', 'is_active']

    list_editable = ['show_on_homepage','is_active']

    prepopulated_fields = {'slug': ('school_name',)}

    inlines = [
        AdmissionRequiredDocumentInline,
        SchoolFacilityInline,
    ]

admin.site.register(School, SchoolAdmin)

admin.site.register(SchoolImage)

admin.site.register(StudentApplication)

admin.site.register(NewsletterSubscriber)




