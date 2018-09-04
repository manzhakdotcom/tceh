from django.contrib import admin
from journal.models import WriteOut, WriteDown, ExtraWriteOut

# Register your models here.


@admin.register(WriteOut)
class WriteOutAdmin(admin.ModelAdmin):
    list_dispalay = ['date']


@admin.register(WriteDown)
class WriteDownAdmin(admin.ModelAdmin):
    list_dispalay = ['date']


@admin.register(ExtraWriteOut)
class ExtraWriteOutAdmin(admin.ModelAdmin):
    list_dispalay = ['date']
