from django.contrib import admin

from ..assets import models
# Register your models here.

admin.site.register(models.Asset)
admin.site.register(models.AssetDetails)
admin.site.register(models.AssetGroup)
admin.site.register(models.Idc)
admin.site.register(models.UserInfo)
admin.site.register(models.Cabinet)
admin.site.register(models.IpSource)
admin.site.register(models.InterFace)
