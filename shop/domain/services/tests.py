from unittest import TestCase, mock

from shop.domain import entities
from shop.domain.abstract_shop_repository import AbstractShopRepository
from shop.domain.services.customer_service import CustomerService


class CustomerServiceTestCase(TestCase):

    def test_promote_user_to_customer_succeeds_with_new_customer(self):
        # Given a user id
        user_id = 123

        mock_repository: AbstractShopRepository = mock.create_autospec(AbstractShopRepository)
        service = CustomerService(mock_repository)
        
        # When the user is promoted to a customer
        customer: entities.Customer = service.promote_user_to_customer(user_id)
        
        # then the get or create customer method should have been called
        mock_repository.get_or_create_customer.assert_called()

    def test_promote_user_to_customer_returns_existing_customer(self):
        # Given a user id
        user_id = 123

        mock_repository: AbstractShopRepository = mock.create_autospec(AbstractShopRepository)
        mock_repository.get_or_create_customer.return_value = entities.Customer(
            id=1,
            user_id=user_id,
            first_name="foo",
            last_name="bar",
        )
        service = CustomerService(mock_repository)
        
        # When the user is promoted to a customer
        customer: entities.Customer = service.promote_user_to_customer(user_id)
        
        # then the get or create customer method should have been called
        mock_repository.get_or_create_customer.assert_called()

        # and a customer object with the user id returned
        self.assertEqual(customer.user_id, user_id)