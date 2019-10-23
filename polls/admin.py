from django.contrib import admin

from .models import Question


class CustomQuestionAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the Exams model.

    model = Question
    list_display = (
        'title',
        'slug',
        'body',
        'active',
        'created_by',
        'created_at',
        'updated_at',

    )
    list_select_related = (
        'created_by',
    )
    list_filter = (
        'title',
        'active',
        'created_by'
    )

    fieldsets = (
        ("Question's title:", {
            'fields': ('title',),
            'description': "Designates a title to this question",
        }),
        ('Content:', {
            'fields': ('body',),
            'description': "Designates a body of exam to question",
        }),
        ('Question status:', {
            'fields': ('active',),
            'description': "Switch between approved question",
        }),

    )

    search_fields = (
        'title',
        'status'
    )
    ordering = (
        'created_at',

    )
    # exclude=['created_by', ]
    filter_horizontal = ()
    empty_value_display = 'None'
    list_per_page = 8

    def save_model(self, request, obj, form, change):
        #  required to add user's name to the created_by field

        obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Question, CustomQuestionAdmin)
