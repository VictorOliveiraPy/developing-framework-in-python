from api import API

app = API()  # Aqui e onde __call__ e chamado


def home(request, response):
    response.text = "Hello from the HOME page"


def about(request, response):
    response.text = "Hello from the ABOUT page"
