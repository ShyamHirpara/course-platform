import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from decouple import config 

CLOUDINARY_CLOUD_NAME = config("CLOUDINARY_CLOUD_NAME",default="")
CLOUDINARY_PUBLIC_API_KEY = config("CLOUDINARY_PUBLIC_API_KEY",default="866757245267231")
CLOUDINARY_SECRET_API_KEY = config("CLOUDINARY_SECRET_API_KEY")

# Configuration      
def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME,
        api_key = CLOUDINARY_PUBLIC_API_KEY ,
        api_secret = CLOUDINARY_SECRET_API_KEY,
        secure=True
    )