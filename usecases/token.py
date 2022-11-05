from fastapi import Request, HTTPException, Depends, status


class VerifyUseCase:
    def __init__(self
                 # , token_repository: TokenRepository = Depends(),
                 ):
        pass

    def verify(self, token):
        # todo
        return True


async def verify(req: Request, verifier: VerifyUseCase = Depends()):
    # todo
    enable = False
    token_name = 'awesome_token'

    if not enable:
        return

    token = req.headers.get(token_name)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    if not verifier.verify(token):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
