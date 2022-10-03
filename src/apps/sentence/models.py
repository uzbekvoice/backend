from django.db import models

from apps.user.models import User


class InvalidityReasons(models.IntegerChoices):
    NOT_CORRECT = 0, "Not correct sentence"
    OTHERS = 1, "Other invalidities"
    UNKNOWN_YET = 2, "Unknown yet"


class Sentence(models.Model):
    text = models.TextField(verbose_name="Text")
    author = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Author")
    reads_count = models.IntegerField(default=0, verbose_name="Reads count")
    is_valid = models.BooleanField(default=True, verbose_name="Is valid")
    invalidity_reason = models.IntegerField(
        default=InvalidityReasons.UNKNOWN_YET, choices=InvalidityReasons.choices, verbose_name="Invalidity reason"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text if len(self.text) < 50 else f"{self.text[:50]}..."

    class Meta:
        verbose_name = "Sentence"
        verbose_name_plural = "Sentences"
