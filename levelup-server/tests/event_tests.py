import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import Event, Game, GameType

class EventTest(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }

        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        gametype = GameType()
        gametype.label = "Board game"
        gametype.save()

        game = Game()
        game.title = "title"
        game.number_of_players = 4
        game.description = "This gmae is fun"
        game.gamer_id = 1
        game_type = 1
        game.game_type_id = game_type
        game.save()

    def test_create_event(self):
        """
        Ensure we can create a new game.
        """
        # DEFINE GAME PROPERTIES
        url = "/events"
        data = {
            "event_day": "2020-10-25",
            "event_time": "14:30",
            "game": 1,
            "location": "Basement",
            "gamer_id": 1
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["event_day"], "2020-10-25")
        self.assertEqual(json_response["event_time"], "14:30")
        self.assertEqual(json_response["location"], "Basement")

    def test_get_game(self):
        """
        Ensure we can get an existing game.
        """
        event = Event()
        event.event_day = "1820-10-25"
        event.event_time = "14:39"
        event.game_id = 1
        event.location =  "Tom's"
        event.gamer_id = 1

        event.save()

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.get(f"/events/{event.id}")

         # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["event_day"], "1820-10-25")
        self.assertEqual(json_response["event_time"], "14:39:00")
        self.assertEqual(json_response["location"], "Tom's")

    

