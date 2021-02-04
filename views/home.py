import fastapi

router = fastapi.APIRouter()

@router.get('/')
def index():
    return "Move along... "

@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/assets/images/favicon.ico')