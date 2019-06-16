from django.contrib import admin
from .models.address import PostalAddress, PhysicalAddress
from .models.contact import Contact, Phone
from .models.eligibility import Eligibility
from .models.language import Language
from .models.location import Location, ServiceArea
from .models.organisation import Organisation
from .models.service import Service

# Register your models here.

class ContactInline(admin.TabularInline):
    model = Contact

class OrganisationAdmin(admin.ModelAdmin):
    inlines = (ContactInline,)

admin.site.register(Organisation, OrganisationAdmin)
