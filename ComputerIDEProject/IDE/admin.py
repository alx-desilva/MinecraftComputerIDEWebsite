from django.contrib import admin
from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "submitted_at", "updated_at", "code_preview")
    readonly_fields = ("submitted_at", "updated_at", "code")
    search_fields = ("name",)
    ordering = ("-updated_at",)

    def code_preview(self, obj):
        lines = obj.code.strip().splitlines()
        preview = lines[0] if lines else ""
        return f"{preview}{'...' if len(lines) > 1 else ''}"
    code_preview.short_description = "Code (preview)"
