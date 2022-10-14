from django.db import models

from apps.user.models import User
from apps.sentence.models import Sentence, StatusChoices


class Voice(models.Model):
    audio_url = models.URLField()
    author = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Author")
    sentence = models.ForeignKey(Sentence, on_delete=models.RESTRICT, verbose_name="Sentence")
    status = models.IntegerField(
        default=StatusChoices.UNKNOWN_YET, choices=StatusChoices.choices, verbose_name="Status"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Voice from {self.author.full_name} (ID: {self.id})"

    class Meta:
        verbose_name = "Voice"
        verbose_name_plural = "Voices"


class VoiceChecker(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Author")
    voice = models.OneToOneField(Voice, on_delete=models.RESTRICT, verbose_name="Voice")
    status = models.IntegerField(
        default=StatusChoices.UNKNOWN_YET, choices=StatusChoices.choices, verbose_name="Status"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Check for voice ID: {self.voice_id} from author ID: {self.author_id}"

    class Meta:
        verbose_name = "Voice checker"
        verbose_name_plural = "Voice checkers"
