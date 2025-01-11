# Remove the direct imports and use __all__ to specify what should be exported
from .core.models import BaseModel
from .users.models import User
from .items.models import Item
from .auth.models import SocialAccount

__all__ = ["BaseModel", "User", "Item", "SocialAccount"]
