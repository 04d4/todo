""" Django settings for local development """


from todo.todo.settings.base import INSTALLED_APPS, MIDDLEWARE

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# ===
# Email settings
# ===

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
