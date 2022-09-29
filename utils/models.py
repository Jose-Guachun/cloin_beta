from django.db import models

class ModeloBase(models.Model):
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Fecha y hora en que se creo el objeto'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Fecha y hora en el que se modifico el objeto'
    )
    status=models.BooleanField(
        'modified at',
        default=True,
        help_text='Fecha y hora en el que se modifico el objeto'
    )

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']