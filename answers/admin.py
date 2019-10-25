from django.contrib import admin
from .models import Answer


class CustomAnswerAdmin(admin.ModelAdmin):
    """ The fields to be used in displaying the choice model """

    model = Answer

    list_display = (
        'answer',
        'user',
        'choice',
        'created_at',
        'updated_at',
    )
    list_select_related = (
        'user',
        'choice',
    )
    list_filter = (
        'user',
        'created_at',
    )

    fieldsets = (
        ("Answer:", {
            'fields': ('answer',),
            'description': "Designates na answer ",
        }),
        ('Choice:', {
            'fields': ('choice',),
            'description': "Designates a choice",
        }),
    )

    search_fields = (
        'user',

    )
    ordering = (
        'created_at',

    )
    filter_horizontal = ()
    empty_value_display = 'None'
    list_per_page = 8

    def save_model(self, request, obj, form, change):
        #  required to add user's name to the author field

        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Answer, CustomAnswerAdmin)
