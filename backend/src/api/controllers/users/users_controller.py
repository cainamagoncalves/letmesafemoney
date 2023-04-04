from ...useCases.handlers.users.get_users_handler import GetUsersUseCase


class GetAllUsersController:
    @staticmethod
    def handle():
        return GetUsersUseCase.execute()
