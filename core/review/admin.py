from django.contrib import admin
from .models import ReviewModels
# ======================================================================================================================
@admin.register(ReviewModels)
class ReviewModelsAdmin(admin.ModelAdmin):
    list_display = ('id','user','product', 'status', 'rate','created_date')
    search_fields = ('id', 'user',)
# ======================================================================================================================

