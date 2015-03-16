from django.contrib import admin
from di_scoring import models

# copypastad with love from :
# `http://stackoverflow.com/questions/10543032/how-to-show-all-fields-of-model-in-admin-page`
# subclassed modeladmins' list_displays will contain all model fields except
# for id
class CustomModelAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields
                             if field.name != "id"]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)


@admin.register(
        models.Manager,
        models.School,
        models.TeamChallenge,
        models.Location,
        models.Team,
        models.TC_Field,
        models.TC_Appraiser,
        models.TC_Event,
        models.TC_Score,
        models.IC_Appraiser,
        models.IC_Event,
        models.IC_Score,
        models.TC_Appraiser_Permission,
)
class DefaultModelAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

