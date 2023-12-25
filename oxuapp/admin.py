from django.contrib import admin
from oxuapp.models import Info, Announcement, Direction, News, Support, Contract

# Register your models here.


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ["title", "count"]
    fields = ["title", "count"]


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ["name", "surename", "phone", "payment_check", "is_payment"]

    fields = ["name", "surename", "father_name", "phone","second_phone","age","contract_type", "study_type", "study_lang", "education_form", "direction", "payment_check", "is_payment"]

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]
    fields = ["title", "description", "image"]


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ["title"]
    fields = ["title"]



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]
    fields = ["title", "description", "image"]



@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ["name", "surename", "father_name", "phone", "direction"]
    fields = ["name", "surename", "father_name", "phone", "direction"]