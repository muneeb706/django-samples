from .models import TestA, TestB, HistoricalTestB, TestC, HistoricalTestC
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

@admin.register(TestA) 
class TestAAdmin(admin.ModelAdmin):
    pass

@admin.register(TestB)
class TestBAdmin(admin.ModelAdmin):
    pass

@admin.register(HistoricalTestB)
class HistoricalTestBAdmin(admin.ModelAdmin):
   pass

# @admin.register(TestC)
# class TestCAdmin(admin.ModelAdmin):
#    pass

# @admin.register(HistoricalTestC)
# class HistoricalTestCAdmin(admin.ModelAdmin):
#    pass

admin.site.register(TestC, SimpleHistoryAdmin)