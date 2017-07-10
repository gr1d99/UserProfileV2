# userprofile
is a simple pluggable django app that provides you with an opportunity to 
add extra fields to default Django User model.

## dependencies
this app runs on `python2` and `django 1.10`
I haven't tested it on `python3` but am certain it may work.

usage
-----

**Note: Kindly create a new project before using it on your existing project**


1. add `AUTH_USER_MODEL = 'userprofile.UserProfile'` into your `settings.py` file.

2. add your fields in the class `UserProfile`, as shown in the example below.

```python
class UserProfile(AbstractUser):
    contact = PhoneNumberField(null=True)
```

then go to `admin.py` which is inside `userprofile` app and under `UserProfileAdmin` look for a variable called 
`fieldsets` add the `phone_number` eg.

```python
class UserProfileAdmin(admin.ModelAdmin):
    ...
    fieldsets = (
        ...
        ('Contact info', {'fields': ('phone_number', )}),
        ...
    )
```

run `python manage.py makemigrations`

then

`python manage.py migrate`

finally navigate to your django administration site and you will see the changes.



