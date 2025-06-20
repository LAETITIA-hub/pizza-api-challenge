# server/seed.py
from server.app import db, create_app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create restaurants
    r1 = Restaurant(name="Kiki's Pizza", address="Address 3")
    r2 = Restaurant(name="Joe's Pizza", address="Address 1")

    # Create pizzas
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Sauce, Cheese, Pepperoni")

    # Add and commit restaurants and pizzas
    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    # Create restaurant-pizza relationships
    rp1 = RestaurantPizza(price=5, restaurant_id=r1.id, pizza_id=p1.id)
    db.session.add(rp1)
    db.session.commit()

    print("Database seeded successfully!")