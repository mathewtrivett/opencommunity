from django.contrib import admin
from .models.address import PostalAddress, PhysicalAddress
from .models.contact import Contact, Phone
from .models.eligibility import Eligibility
from .models.language import Language
from .models.location import Location, ServiceArea
from .models.organisation import Organisation
from .models.service import Service
from .models.identification_body import IdentificationBody
from .models.identifier import Identifier
from .models.taxonomy import Taxonomy

# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
    pass


class IdentifierInline(admin.TabularInline):
    model = Identifier
    extra = 0
    autocomplete_fields = ('identification_body',)

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0

class ServiceInline(admin.StackedInline):
    model = Service
    extra = 0

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0
    inlines = (PhoneInline,)

class OrganisationAdmin(admin.ModelAdmin):
    inlines = (ContactInline, ServiceInline, IdentifierInline,)
    search_fields = ('name', 'alternate_name',)

class ServiceAdmin(admin.ModelAdmin):
    autocomplete_fields = ('organisation',)
    list_display = ('name','alternate_name','description','status','updated_at',)

class IdentificationBodyAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id','name',)
    search_fields = ('name',)

class TaxonomyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ('parent',)
    list_display = ('name', 'parent', 'vocabulary',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(IdentificationBody, IdentificationBodyAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Taxonomy,TaxonomyAdmin)
