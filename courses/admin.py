from django.contrib import admin
from .models import Currency, Course


@admin.register(Course)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "language", "price", "currency")
    list_filter = ("name", "language")
    search_fields = ["name", "language"]


admin.site.register(Currency)
