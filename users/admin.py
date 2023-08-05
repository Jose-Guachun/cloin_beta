#clases de admin

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group

#Models
from users.models import User, Profile, City, Country, Province, Person

# Register your models here.

admin.site.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'country',)

admin.site.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'country',
        'province',)

admin.site.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'province',
        'city',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'user',
        'city',
        'dni',
        'gender',
        'birth_date',
        'biography',
        'phone_number',
        'picture',)

    list_display_links=('pk', 'user', 'city',)

    list_editable=(
        'gender',
        'birth_date',
        'biography',
        'phone_number',
        'picture',)

    search_fields=(
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name_first',
        'phone_number',
        )

    list_filter=(
        'user__is_active',
        'created',
        'modified',
    )

    fieldsets=(
        ('Profile', {
            'fields':
                (
                    'user', 'picture',
                    'country','province','city','favorites',
                    'gender',
                    'birth_date',
                    ),
        }),
        ('Extra info',{
            'fields':(
                ('phone_number'),
                ('biography'),
            )
        }),
        ('Metadata', {
            'fields':(('created', 'modified'),),
        })
    )
    readonly_fields=('created', 'modified',)

class PersonInline(admin.StackedInline):
    model=Person
    can_delete=False
    verbose_name_plural='personas'

class UserAdmin(BaseUserAdmin):
    inlines=(PersonInline,)
    list_display=(
        'username',
        'email',
        'first_name',
        'last_name',
        'is_verified',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',

    )
    list_filter=('is_staff',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin,)
admin.site.unregister(Group)
