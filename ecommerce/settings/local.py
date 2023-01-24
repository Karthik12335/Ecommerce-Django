from .base import *

DATABASES = {
    "default": {},
    "auth_db": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    # "auth_db": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "auth_ecommerce",
    #     "HOST": "localhost",
    #     "USER": "root",
    #     "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
    # },
    "ecomm_db": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ecommerce",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
    },
}

DATABASE_ROUTERS = ["routers.db_routers.AuthRouter", "routers.db_routers.PrimaryRouter"]
