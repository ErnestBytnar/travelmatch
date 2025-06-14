from django.contrib import admin
from .models import User, UserProfile,BudgetRange,TravelStyle,TravelPriority

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(BudgetRange)
admin.site.register(TravelStyle)
admin.site.register(TravelPriority)


