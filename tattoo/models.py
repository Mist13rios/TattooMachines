from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, commit=True, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(username=username,
                          email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    # username and email fields are needed for python social auth
    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    TITLE_CHOICES = (
        ('mister', 'Mister'),
        ('miss', 'Miss'),
    )
    SEX_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    title = models.CharField('Title', max_length=30, choices=TITLE_CHOICES, default='mister')
    first_name = models.CharField('First name', max_length=30, blank=True, null=True)
    last_name = models.CharField('Last name', max_length=30, blank=True, null=True)
    sex = models.CharField('Sex', max_length=10, choices=SEX_CHOICES, default='male')
    birth_date = models.CharField('Birth date', max_length=10, blank=True, null=True)
    password_open = models.CharField('Password', max_length=255, blank=True, null=True)

    username = models.CharField(
        'username',
        max_length=30,
        unique=True,
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                'Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.'
            ),
        ],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField('email address', unique=True)

    is_staff = models.BooleanField(('staff status'), default=False,
                                   help_text='Designates whether the user can log into this admin '
                                               'site.')
    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.')
    is_manager = models.BooleanField('manager', default=False,
                                     help_text='Designates whether the user can log into manager admin part')
    date_joined = models.DateTimeField('date joined', auto_now_add=True, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        full_name = full_name.strip()
        if not full_name:
            full_name = self.email
        return full_name

    def get_short_name(self):
        return self.first_name or self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        original = None
        if self.pk is not None:
            original = User.objects.get(pk=self.pk)
            if self.password_open != original.password_open:
                self.set_password(self.password_open)
        super(User, self).save(*args, **kwargs)