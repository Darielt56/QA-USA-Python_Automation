import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print(" Connected to the Urban Routes server")
        else:
            print("Cannot connect to thr Urban Routes server.Check the server is on and still running")

    def test_set_route(self):
        # Add code in S8
        print('Function for set route')
        pass

    def test_select_plan(self):
        # Add code in S8
        print('Function select plan')
        pass

    def test_fill_phone_number(self):
        # Add code in S8
        print('Function for fill phone number')
        pass

    def test_fill_card(self):
        # Add code in S8
        print('Function for fill card')
        pass

    def test_comment_for_driver(self):
        # Add code in S8
        print('Function for test comment for driver')
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add code in S8
        print('Function for order blanket and handkerchiefs')
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_cream = 2  # number of iterations
        for ice_cream in range(number_of_ice_cream):
            print(' Function for order 2 ice cream')
            pass
        # Add code in S8
        print('Function for order 2 ice cream')
        pass

    def test_car_search_model_appears(self):
        # Add code in S8
        print('Function for car search model appears')
        pass
