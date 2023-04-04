from ....repositories.users.users_repository import UserRepository


class GetUsersUseCase:

    def __init__(self) -> None:
        pass

    @staticmethod
    def execute():
        return UserRepository.select()
