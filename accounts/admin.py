from django.contrib import admin
from .models import Profile, User


class ProfileInLine(admin.TabularInline):
    model = Profile
    verbose_name_plural = 'User Profile'


class CustomUserAdmin(admin.ModelAdmin):

    inlines = (ProfileInLine,)

# class ProfileAdmin(admin.ModelAdmin):

#     date_hierarchy = 'created_at'
#     readonly_fields = ('created_at', 'updated_at')
#     # inlines = (ProfileInLine,)
#     list_display = (
#         'user',
#         'age',
#         'city',
#         'created_at'
#     )
#     list_filter = (
#         'user',
#         'age',
#         'created_at'
#     )
#     fieldsets = (
#         ("Question's title:", {
#             'fields': ('user',),
#             'description': "Designates a title to this question",
#         }),
#         ('Content:', {
#             'fields': ('country',),
#             'description': "Designates a body of exam to question",
#         }),
#         ('Question status:', {
#             'fields': ('age',),
#             'description': "Switch between approved or unapproved question",
#         }),
#         ('Question status:', {
#             'fields': ('city',),
#             'description': "Switch between approved or unapproved question",
#         }),

#     )

#     search_fields = (
#         'title',
#         'approved_question'
#     )
#     empty_value_display = 'None'
#     filter_horizontal = ()
#     list_per_page = 10


admin.site.register(User, CustomUserAdmin)
