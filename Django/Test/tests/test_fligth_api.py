from rest_framework.test import APITestCase,APIRequestFactory
from flight.views import FlightView

class flightTestCase(APITestCase):
    
    def SetUp(self):
        self.factory = APIRequestFactory()
    

    def test_flight_list_as_non_authenticated_user(self):
        request = self.factory.get('/flight/flights')
        print(request)
        response = FlightView.as_view({'get':"list"})(request)
        print(response)
        self.assertEquals(response.status_code,200)