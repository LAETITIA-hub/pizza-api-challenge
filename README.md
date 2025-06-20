🍕 Pizza Place API
A RESTful API built with Flask for managing pizza restaurants, their pizzas, and relationships. Utilizes Flask, SQLAlchemy, Flask-Migrate, and adheres to the MVC architecture.

🚀 Installation Guide
git clone <https://github.com/Laetitia-Kamangu/pizza-api-project>
cd pizza-api-project
pipenv install
pipenv shell
cd server
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
flask db init
flask db migrate -m "First migration"
flask db upgrade
python seed.py
flask run

📂 Project Structure (MVC)
server/
├── app.py                  # Application configuration
├── config.py               # Database configuration
├── seed.py                 # Data seeding script
├── models/                 # SQLAlchemy model definitions
├── controllers/            # Route logic

💿 Data Models
Restaurant

id, name, address
Linked to multiple RestaurantPizza

Pizza

id, name, ingredients
Linked to multiple RestaurantPizza

RestaurantPizza

id, price (must be 1–30)
pizza_id, restaurant_id

🌟 API Endpoints



Method
Endpoint
Description



GET
/restaurants
Retrieve all restaurants


GET
/restaurants/<id>
Fetch a restaurant and its pizzas


DELETE
/restaurants/<id>
Remove a restaurant


GET
/pizzas
List all pizzas


POST
/restaurant_pizzas
Associate a pizza with a restaurant


🧪 Sample Request
POST /restaurant_pizzas
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2
}

Success Response:
{
  "id": 4,
  "price": 10,
  "pizza": {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Dough, Cheese, Pepperoni"
  },
  "restaurant": {
    "id": 2,
    "name": "Mama's Pizza",
    "address": "123 Main St"
  }
}

❌ Sample Error Response
{ "errors": ["Price must be between 1 and 30"] }

🧪 Testing with Postman

Import challenge-1-pizzas.postman_collection.json into Postman.
Configure the environment or use http://localhost:5555.
Test all endpoints with the provided collection.

✅ Validations

price in RestaurantPizza must be between 1 and 30.
Clear error messages for 404s and invalid inputs.

👩‍💻 Author
Laetitia Kamangu📧 laetitia.kamangu@student.moringaschool.com
