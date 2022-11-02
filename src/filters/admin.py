from aiogram.dispatcher.filters import BoundFilter

from src.config import Config


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin=None):
        self.is_admin = is_admin

    async def check(self, obj):
        config: Config = obj.bot.get('config')
        user_id = obj.from_user.id
        if user_id in config.bot.admin_ids:
            return True
        return False
