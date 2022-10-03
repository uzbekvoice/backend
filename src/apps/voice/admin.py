from django.contrib import admin

from .models import Voice, VoiceChecker


admin.site.register([Voice, VoiceChecker])
