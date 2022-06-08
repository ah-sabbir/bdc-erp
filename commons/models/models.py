from django.db import models


class Role(models.Model):
    """
    角色
    """

    data_type_choices = (
        ("all", "all"),
        ("自定义", "自定义"),
        ("同级及以下", "同级及以下"),
        ("本级及以下", "本级及以下"),
        ("本级", "本级"),
        ("仅本人", "仅本人"),
    )
    role_id = models.AutoField("角色表主键ID", primary_key=True)
    role_name = models.CharField("角色", max_length=255, unique=True)
    role_level = models.IntegerField("角色级别", null=True)
    description = models.CharField("描述", max_length=255, blank=True, null=True)
    data_scope = models.CharField(
        "数据权限",
        max_length=255,
        choices=data_type_choices,
        default="自定义",
        null=True,
        blank=True,
    )
    menus = models.ManyToManyField(Menu, blank=True, verbose_name="角色菜单关联")

    depts = models.ManyToManyField(Dept, blank=True, verbose_name="角色部门关联")

    class Meta:
        managed = True
        verbose_name = "角色"
        verbose_name_plural = verbose_name
        ordering = ["role_id"]

    def __str__(self):
        return self.role_name