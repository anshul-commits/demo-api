from ninja import NinjaAPI, Schema, Path
import datetime
from .models import Book, BookSchema

api = NinjaAPI()
# Example: Basic GET Request i.e. https://localhost:8000/api/hello
@api.get("/hello")
def hello(request):
    return f"Hello World!"

# Example: GET Request with Parameters i.e https://localhost:8000/api/hello?name=Anshul
@api.get("/hello")
def hello(request, name="world!"):
    return f"Hello {name}"

# Alternatively i.e. https://localhost:8000/api/hello/Anshul
@api.get("/hello/{name}")
def greet_name(request, name:str):
    return f"Hello, {name}!"
# i.e. https://localhost:8000/api/hello/Anshul
@api.get("/math")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}

class HelloSchema(Schema):
    name: str = "world"

# Example: Basic POST Request, with help of a Schema to structure the response data!!
@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"

#Example: POST Request with JSON Data
@api.post("/submit-form")
def submit_form(request, name: str, age: int):
    return {"message": f"Form submitted! \n Welcome! {name}, Okay so you are {age} years old!"}

# Example : Using multiple Parameters
@api.get("/events/{year}/{month}/{day}")
def events(request, year: int, month: int, day: int):
    return {"The Date is": [year, month, day]}

# Example : Using Schema to handle and validate path parameters that depend on each other
class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return datetime.date(self.year, self.month, self.day)
    
@api.get("/events/{year}/{month}/{day}")
def events(request, date: Path[PathDate]):
    return {"date": date.value()}

# Example : GET Request for handling multiple response data using Schemas!
class UserSchema(Schema):
    username: str
    email: str
    first_name: str
    last_name: str

class Error(Schema):
    message: str

@api.get("/me", response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user 

@api.post("/add-book")
def add_book(request, payload: BookSchema):
    book = Book.objects.create(
        title=payload.title,
        author=payload.author,
        published_date=payload.published_date,
        isbn=payload.isbn
    )
    return {"id": book.id, "message": "Book added successfully"}