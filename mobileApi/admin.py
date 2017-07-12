from django.contrib import admin
import mobileApi.models
admin.site.register(mobileApi.models.Actor)
admin.site.register(mobileApi.models.Category)
admin.site.register(mobileApi.models.Play)
admin.site.register(mobileApi.models.Play_Representation)
admin.site.register(mobileApi.models.Rating)
admin.site.register(mobileApi.models.Theater)
#admin.site.register(mobileApi.models.User)
admin.site.register(mobileApi.models.Profile)
admin.site.register(mobileApi.models.Comment)
admin.site.register(mobileApi.models.Favorite)
# Register your models here.
