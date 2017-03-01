from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from bcrypt import hashpw, checkpw, gensalt
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# """
# models come with a hidden key:
#       objects = models.Manager()The Magic Flute
# we are going to overwrite this!
# """


class UserManager(models.Manager):
    def login(self, postData):
        #LOGIC FOR LOGGING IN
        print ("-"*10),"Running a login function!"
        #errors list of errors, as they occur, to be returned as needed
        errors = []

        #check if email exists, if not throw error
        user = User.objects.filter(email=str(postData['email']))

        #check pre hashed PW:
        # if bcrypt.hashpw(password, hashed) == hashed:
        if not user or not checkpw(postData['password'].encode('utf-8'),user[0].password.encode('utf-8')):
            return False

        else:
            print ("-"*10),"completed a login function!"
            return user[0]

        # print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
        # print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"

    def register(self, postData):
        #LOGIC FOR REGISTRATION
        print ("-"*10),"Running a registration function!"
        #errors list of errors, as they occur, to be returned as needed
        errors = []

        #TEST first name
        if len(postData['first_name']) < 2:
            errors.append("First name must be more than two characters.")

        #TEST last name
        if len(postData['last_name']) < 2:
            errors.append("Last name must be more than two characters.")

        #TEST email validation
        try:
            validate_email(postData['email'])
        except:
            errors.append("Email is not valid")

        #TEST password length
        if len(postData['password']) < 8 or len(postData['password']) > 32:
            errors.append("Passwords must be at least 8 characters and no more than 32 characters.")

        #TEST password matches confirm
        if postData['confirm'] != postData['password']:
            errors.append("Passwords do not match.")

        # if there are errors present, redirect and dislpay the errors in messages
        if errors:
            return (False, errors)

        else:
            #If no errors, complete the registration process:
            #hash the password:
            hashed = hashpw(postData['password'].encode('utf-8'), gensalt(14))
            user = User.objects.create(
                first_name = postData['first_name'],
                last_name = postData['last_name'],
                email = postData['email'],
                password = hashed
            )
            print ("-"*10),"completed a registration function!"
            return (True, user)

        # pass

    def logout(self, session):
        try:
            del session['is_logged']
            del session['user_id']
            del session['first_name']
        except KeyError:
            pass
        print ("-"*10),"completed a logout function!"
        return True


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=30, default="blank@example.com")
    password = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # objects = UserManager()

    # *************************
