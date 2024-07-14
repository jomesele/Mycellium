from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
from .encode import Encoder

class MyUserManager(BaseUserManager):   
    #Agent 
    def create_user(self, phone, password=None):
        """
        Creates and saves an Agent with the given specs
        """       
        if not phone:
            raise ValueError('Users must have a phone address')
        user = self.model(
            phone=phone,      
        )        
           
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, phone, password):
        """
        Creates and saves a superuser with the given specs.
        """
        user = self.create_user( phone,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    


class MyUser(AbstractBaseUser):
    class Types(models.TextChoices):
        AGENT = 'AGENT', 'agent'
        STORE = 'STORE', 'store'
        ADMINA = 'ADMINA', 'admina'
    
    
    def cats():
        CATGS =[
            ("Electronics", "electronics"), 
            ("Fashion", "fashion"), 
            ("Books", "books"), 
            ("Building Material", "building material"), 
            ("Stationary", "stationary"), 
            ("Fashion", "fashine"), 
            ("Furniture", "furniture"), 
        ]
        return CATGS

    type = models.CharField(max_length = 8, choices = Types.choices, default = Types.AGENT)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True) # Validators should be a list
    name = models.CharField(max_length=100)
    qrImg = models.ImageField(upload_to='user_qr')
    
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    storeQrImg = models.ImageField(upload_to='Store_qr')
    logo = models.ImageField(upload_to='store_logo') 
    
    category1 = models.CharField(max_length = 100, choices = cats(), default = Types.AGENT)    

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_agent = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)
    is_admina = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'phone'
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_phone(self):
        # The user is identified by their email address
        return self.phone

    def __str__(self):              # __unicode__ on Python 2
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class AgentManager(models.Manager): 
    def create_user(self , phone , name, category1, qrImg, password = None): 
        if not phone or len(phone) <= 0 :  
            raise  ValueError("phone field is required !") 
        if not password : 
            raise ValueError("Password is must !") 
        user = self.model( 
            phone = phone,
            name = name,
            category1 = category1, 
            qrImg =qrImg,
        ) 
        user.set_password(password)
        user.save(using = self._db) 
        return user 
      
    def get_queryset(self , *args,  **kwargs): 
        queryset = super().get_queryset(*args , **kwargs) 
        queryset = queryset.filter(type = MyUser.Types.AGENT) 
        return queryset 

class Agent(MyUser): 
    class Meta:  
        proxy = True
    objects = AgentManager() 
    
    def gen(self):
        data_to_encode = self.phone # Customize as needed
        enc = Encoder()
        qr_code = enc.encode(data_to_encode)
        qr_code.save(f"{'media/user_qr/' + data_to_encode + '.png'}", "PNG")    
        self.qrImg = f"{'user_qr/' + data_to_encode + '.png'}"
        self.save()
      
    @property
    def get_photo_url(self):
        if self.qrImg and hasattr(self.qrImg, 'url'):
            return self.qrImg.url
        else:
            return f"{'/media/user_qr/' + self.phone + '.png'}"
      
    def save(self , *args , **kwargs): 
        self.type = MyUser.Types.AGENT
        self.is_agent = True
        return super().save(*args , **kwargs)  

class StoreManager(models.Manager): 
    def create_user(self, phone, name, category1, address, description, storeQrImg, password = None): 
        if not phone or len(phone) <= 0 :  
            raise  ValueError("phone field is required !") 
        if not password : 
            raise ValueError("Password is must !") 
        user = self.model( 
            phone = phone,
            name = name,
            category1 = category1,
            address = address,
            description = description,
            storeQrImg = storeQrImg 
        ) 
        user.set_password(password)
        user.save(using = self._db) 
        return user 
      
    def get_queryset(self , *args,  **kwargs): 
        queryset = super().get_queryset(*args , **kwargs) 
        queryset = queryset.filter(type = MyUser.Types.STORE) 
        return queryset 

class Store(MyUser):
    class Meta:  
        proxy = True
    objects = StoreManager() 

    def gen(self):
        data_to_encode = self.phone  # Customize as needed
        enc = Encoder()
        qr_code = enc.encode(data_to_encode)
        qr_code.save(f"{'media/Store_qr/' + data_to_encode + '.png'}", "PNG")    
        self.storeQrImg = f"{'Store_qr/' + data_to_encode + '.png'}"
        self.save()

    @property
    def get_ph_url(self):
        if self.storeQrImg and hasattr(self.storeQrImg, 'url'):
            return self.storeQrImg.url
        else:
            return f"{'/media/Store_qr/' + self.phone + '.png'}"
      
    def save(self , *args , **kwargs): 
        self.type = MyUser.Types.STORE
        self.is_store = True
        return super().save(*args , **kwargs)          
    
class AdminaManager(models.Manager): 
    def create_user(self , phone , name, category1, password = None): 
        if not phone or len(phone) <= 0 :  
            raise  ValueError("phone field is required !") 
        if not password : 
            raise ValueError("Password is must !") 
        user = self.model( 
            phone = phone,
            name = name,
            category1 = category1, 
        ) 
        user.set_password(password) 
        user.save(using = self._db) 
        return user 
      
    def get_queryset(self , *args,  **kwargs): 
        queryset = super().get_queryset(*args , **kwargs) 
        queryset = queryset.filter(type = MyUser.Types.ADMINA) 
        return queryset 

class Admina(MyUser): 
    class Meta:  
        proxy = True
    objects = AdminaManager() 
      
    def save(self , *args , **kwargs): 
        self.type = MyUser.Types.ADMINA
        self.is_admina = True
        return super().save(*args , **kwargs)  