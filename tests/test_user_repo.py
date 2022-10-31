from configs.database import get_session
from fastapi import Depends
from entities.base import init_models
from entities.user import User
from repositories.user_repository import UserRepository
from test_setup import run_test


async def test_user_repo_users():
    ASYNC_FOR = False
    if ASYNC_FOR:
        async for s in get_session():
            user_repo = UserRepository(s)
            users = await user_repo.users()
    else:
        s = get_session()
        siter = s.__aiter__()
        sess = await siter.__anext__()
        user_repo = UserRepository(sess)
        users = await user_repo.users()
        try:
            await siter.__anext__()
        except StopAsyncIteration:
            print('StopAsyncIteration')


run_test(init_models)
run_test(test_user_repo_users)
