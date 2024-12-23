from dao.base import BaseDAO
from models.profile import Profile


class ProfileDAO(BaseDAO):
    model = Profile
