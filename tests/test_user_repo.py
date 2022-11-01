from configs.database import get_session
from fastapi import Depends
from entities.base import init_models
from entities.user import User
from entities.user_image import UserImage
from repositories.user_repository import UserRepository
from test_setup import run_test


async def test_user_repo_users():
    ASYNC_FOR = True
    if ASYNC_FOR:
        async for s in get_session():
            user_repo = UserRepository(s)
            users = await user_repo.users()
            for u in users:
                print(u.id, u.name)
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


async def add_user():
    async for s in get_session():
        user_repo = UserRepository(s)
        await user_repo.create(
            User(
                name='test_user'
            )
        )
        users = await user_repo.users()
        for u in users:
            print(u.id, u.name)


async def update_user():
    async for s in get_session():
        user_repo = UserRepository(s)
        for u in await user_repo.users():
            u.name = f'id is {u.id}'
            await user_repo.update(u)

        for u in await user_repo.users():
            print(u.id, u.name)


async def delete_users():
    async for s in get_session():
        user_repo = UserRepository(s)
        for u in await user_repo.users():
            await user_repo.delete(u.id)


run_test(init_models)
# run_test(add_user)
# run_test(update_user)

run_test(delete_users)
run_test(test_user_repo_users)
