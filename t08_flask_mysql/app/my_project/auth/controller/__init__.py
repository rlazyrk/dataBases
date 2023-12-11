"""
2023
Rlazyrk@gmail.com
© Roman Lazurkevych
"""

from .orders.artists_controller import ArtistsController
from .orders.artists_events_connect_controller import ArtistsEventConnectController
from .orders.delivery_controller import DeliveryController
from .orders.events_controller import EventsController
from .orders.orders_controller import OrdersController
from .orders.payments_controller import PaymentsController
from .orders.places_controller import PlacesController
from .orders.seats_controller import SeatsController
from .orders.tickets_controller import TicketController
from .orders.travel_tickets_controller import TravelTicketController
from .orders.users_controller import UsersController


artists_controller = ArtistsController()
artists_events_connect_controller = ArtistsEventConnectController()
delivery_controller = DeliveryController()
events_controller = EventsController()
orders_controller = OrdersController()
payments_controller = PaymentsController()
places_controller = PlacesController()
seats_controller = SeatsController()
tickets_controller = TicketController()
travel_tickets_controller = TravelTicketController()
users_controller = UsersController()
