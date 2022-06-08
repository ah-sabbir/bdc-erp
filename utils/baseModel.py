from django.db import models


class BaseModel(models.Model):
    """
    basic table
    """

    create_by = models.CharField(
        null=True, blank=True, verbose_name="creator", help_text="creator", max_length=50
    )
    update_by = models.CharField(
        null=True, blank=True, verbose_name="creator", help_text="creator", max_length=50
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="creation time",
        help_text="creation time",
        null=True,
        blank=True,
    )
    update_at = models.DateTimeField(
        auto_now=True, verbose_name="Change the time", help_text="Change the time", null=True, blank=True
    )
    is_deleted = models.BooleanField(
        default=False, verbose_name="delete mark", help_text="delete mark"
    )
    is_activate = models.BooleanField(
        default=True, verbose_name="Status: 1 enabled, 0 disabled", help_text="Status: 1 enabled, 0 disabled"
    )

    class Meta:
        abstract = True


class SoftDeleteModel(BaseModel):
    """
    soft delete base table
    """

    class Meta:
        abstract = True

    def delete(self, using=None, soft=False, *args, **kwargs):
        """
        If you need to delete it here, soft=False can be
        """
        if soft:
            self.is_deleted = True
            self.save(using=using)
        else:

            return super(SoftModel, self).delete(using=using, *args, **kwargs)