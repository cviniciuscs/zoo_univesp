from typing import Optional
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


admin.site.unregister(User)

@admin.register(User)
class CustumUserAdmin(UserAdmin):
    def get_form(self, request, obj = None, **kwargs):
        form =  super().get_form(request, obj, **kwargs)

        if not request.user.is_superuser:
            # form.base_fields["is_superuser"].readonly = True
            pass
        return form