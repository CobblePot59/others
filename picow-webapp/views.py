from app import app

@app.route('/')
def index(request):
    return 'Hello, from Pico'