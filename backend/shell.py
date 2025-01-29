import asyncio
from IPython import embed
from src.core.db import async_session_maker

# Import your models, dependencies, and other modules you want to work with
from src.users.models import User
from src.auth.models import SocialAccount
# Add other imports as needed

async def get_session():
    async with async_session_maker() as session:
        return session

# Create an async function to run async code in the shell
async def async_shell():
    session = await get_session()
    
    # Create a dict of commonly used objects
    context = {
        'session': session,
        'User': User,
        'SocialAccount': SocialAccount,
        # Add other objects you want available in the shell
    }
    
    # Start IPython shell with the context
    embed(colors='neutral', using='asyncio')
    
    # Clean up
    await session.close()

if __name__ == '__main__':
    asyncio.run(async_shell()) 