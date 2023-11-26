"""
2023
Rlazyrk@gmail.com
© Roman Lazurkevych
"""


from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    from .orders.artists_route import artists_bp
    from .orders.delivery_route import delivery_bp
    from .orders.orders_route import orders_bp
    from .orders.event_route import events_bp
    from .orders.seats_route import seats_bp
    from .orders.payments_route import payments_bp
    from .orders.places_route import places_bp
    from .orders.travel_tickets_route import travel_tickets_bp
    from .orders.users_route import users_bp
    from .orders.tickets_route import tickets_bp

    app.register_blueprint(artists_bp)
    app.register_blueprint(delivery_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(seats_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(travel_tickets_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(err_handler_bp)


