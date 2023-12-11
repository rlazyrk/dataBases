"""
2023
Rlazyrk@gmail.com
© Roman Lazurkevych
"""

# orders DB
from .orders.artists_dao import ArtistsDao
from .orders.artist_events_connect_dao import ArtistsEventsConnectDao
from .orders.delivery_dao import DeliveryDao
from .orders.events_dao import EventsDao
from .orders.orders_dao import OrdersDao
from .orders.payments_dao import PaymentsDao
from .orders.places_dao import PlacesDao
from .orders.seats_dao import SeatsDao
from .orders.tickets_dao import TicketsDao
from .orders.travel_tickets_dao import TravelTicketsDao
from .orders.users_dao import UsersDao
from .orders.referrals_dao import ReferralsDao


artists_dao = ArtistsDao()
artists_events_connect_dao = ArtistsEventsConnectDao()
delivery_dao = DeliveryDao()
events_dao = EventsDao()
orders_dao = OrdersDao()
payments_dao = PaymentsDao()
places_dao = PlacesDao()
seats_dao = SeatsDao()
tickets_dao = TicketsDao()
travel_tickets_dao = TravelTicketsDao()
users_dao = UsersDao()
referrals_dao = ReferralsDao()
