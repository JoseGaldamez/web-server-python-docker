import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>Basic server on python</title>
        </head>
        <body>  
            <h1>Home</h1>
            <p>
                <a href="./contact">
                Ir a la pagina de contacto
                </a>
            </p>
        </body>
    </html>
    """


@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
    <html>
        <head>
            <title>Contact</title>
        </head>
        <body>  
            <h1>Contact</h1>
            <p>Phone: +504 3175-1455</p>
            <p>Email:
                <a href="mailto:josegaldamez1991@gmail.com">
                josegaldamez@gmail.com
                </a>
            </p>
        </body>
    </html>
    """


def main():
    store.get_categories()


if __name__ == '__main__':
    main()
