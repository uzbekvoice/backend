from django.db import models

from apps.user.models import User
from apps.sentence.models import Sentence, InvalidityReasons


class Voice(models.Model):
    audio_url = models.URLField()
    author = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Author")
    sentence = models.ForeignKey(Sentence, on_delete=models.RESTRICT, verbose_name="Sentence")
    checks_count = models.PositiveSmallIntegerField(default=0, verbose_name="Checks count")
    is_valid = models.BooleanField(default=False, verbose_name="Is valid")
    invalidity_reason = models.IntegerField(
        default=InvalidityReasons.UNKNOWN_YET, choices=InvalidityReasons.choices, verbose_name="Invalidity reason"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Voice from {self.author.full_name} (ID: {self.id}), checks: {self.checks_count}"

    class Meta:
        verbose_name = "Voice"
        verbose_name_plural = "Voices"


class VoiceChecker(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Author")
    voice = models.OneToOneField(Voice, on_delete=models.RESTRICT, verbose_name="Voice")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Check for voice ID: {self.voice_id} from author ID: {self.author_id}"

    class Meta:
        verbose_name = "Voice checker"
        verbose_name_plural = "Voice checkers"
