from django.core.exceptions import ValidationError
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        default=0,
        )
    is_auto_generated = models.BooleanField(
        blank=False,
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )
    modified_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__

    def clean(self):
        super().clean()

        if self.name.lower() == "bad":
            raise ValidationError(f"Bad name. Current name: {self.name}")

        self.name = self.name.capitalize()

        return

    class Meta:
        ordering = ["-modified_at", "name"]
