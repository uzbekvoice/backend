from django.db import models

from apps.user.models import User


class StatusChoices(models.IntegerChoices):
    NOT_CORRECT = 0, "Not Valid"
    VALID = 1, "Valid"
    UNKNOWN_YET = 2, "Unknown Yet"
    OTHERS = 3, "Other Invalidity"


class Sentence(models.Model):
    text = models.TextField(verbose_name="Text")
    author = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Author")
    status = models.IntegerField(
        default=StatusChoices.UNKNOWN_YET, choices=StatusChoices.choices, verbose_name="Status"
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sentence from: {self.author.full_name}. [{self.text}]" \
            if len(self.text) < 50 else f"[Sentence from: {self.author.full_name}. {self.text[:50]}...]"

    class Meta:
        verbose_name = "Sentence"
        verbose_name_plural = "Sentences"


class SentenceChecker(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Author")
    sentence = models.OneToOneField(Sentence, on_delete=models.RESTRICT, verbose_name="Sentence")
    status = models.IntegerField(
        default=StatusChoices.UNKNOWN_YET, choices=StatusChoices.choices, verbose_name="Status"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Check for sentence ID: {self.sentence_id} from author ID: {self.author_id}"

    class Meta:
        verbose_name = "Sentence checker"
        verbose_name_plural = "Sentence checkers"
