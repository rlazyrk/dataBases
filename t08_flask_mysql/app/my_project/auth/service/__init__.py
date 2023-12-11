"""
2023
rlazyrk@gmail.com
© Roman Lazurkevych
"""

from .orders.artists_service import ArtistsService
from .orders.artists_events_connect_service import ArtistsEventConnectService
from .orders.delivery_service import DeliveryService
from .orders.events_service import EventsService
from .orders.orders_service import OrdersService
from .orders.payments_service import PaymentsService
from .orders.places_service import PlacesService
from .orders.seats_service import SeatsService
from .orders.tickets_service import TicketsService
from .orders.travel_tickets_service import TravelTicketsService
from .orders.users_service import UsersService
from .orders.referrals_service import ReferralsService

artists_service = ArtistsService()
artists_events_connect_service = ArtistsEventConnectService()
delivery_service = DeliveryService()
events_service = EventsService()
orders_service = OrdersService()
payments_service = PaymentsService()
places_service = PlacesService()
seats_service = SeatsService()
ticket_service = TicketsService()
travel_ticket_service = TravelTicketsService()
user_service = UsersService()
referral_service = ReferralsService()
