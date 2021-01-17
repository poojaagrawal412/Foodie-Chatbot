from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
from email.message import EmailMessage
import smtplib
import requests
from concurrent.futures import ThreadPoolExecutor

class ActionSearchRestaurants(Action):
    
    config = {'config':'1ab7e0cb5e13107753ac51b512c68a61'}
    
    def name(self):
        return 'action_search_restaurants'
    
    def run(self, dispatcher, tracker, domain):
        config = {'user_key':'1ab7e0cb5e13107753ac51b512c68a61'}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        results,lat,lon = self.get_location(loc,zomato)
        maxcost = int(tracker.get_slot('budgetmax'))
        mincost = int(tracker.get_slot('budgetmin'))
        # Zomato API was unable to find the given location
        if results==0:
            restaurant_exist = False
            dispatcher.utter_message("Sorry! No results found in this location:("+ "\n")
        else:
            d_rest = self.get_restaurants(lat, lon, mincost, maxcost, cuisine)
            
            # Restaurants are filtered based on the selected budget
            d_budget_filter = [restaurant_single for restaurant_single in d_rest if ((int(restaurant_single['restaurant']['average_cost_for_two']) > mincost) &
            (int(restaurant_single['restaurant']['average_cost_for_two']) < maxcost))]
            # Sort the filtered results according to the restaurants' rating given at Zomato
            d_budget_rating_sorted = sorted(
            d_budget_filter, key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True)
                    
            # Build the Response
            response = ""
            budget_for_2 = ""
            restaurant_exist = False
            # If no restaurant selected based on the given budget criteria
            if len(d_budget_rating_sorted) == 0:
                dispatcher.utter_message("Sorry! No results found :("+ "\n")
            else:
                # Pick the top 5 restaurants based on the budget and rating
                d_top5_restaurants = d_budget_rating_sorted[:5]
                top_5_len = str(len(d_top5_restaurants))
                global d_email_restaurant
                d_email_restaurant = d_budget_rating_sorted[:10]
                if(d_email_restaurant and len(d_email_restaurant) > 0):
                    restaurant_exist = True
                for restaurant in d_top5_restaurants:
                    budget_for_2 = str(restaurant['restaurant']['average_cost_for_two'])
                    response = response + restaurant['restaurant']['name'] + " in location " + restaurant['restaurant']['location']['address'] + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + " with an average budget for two of Rs. "+ budget_for_2 + "\n" + "\n"
                dispatcher.utter_message("Here are the top "+ top_5_len + " restaurants for you!!"+ "\n" + response)
        return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]
        
    def get_location(self, loc, zomato):
        # Get location details including latitude and longitude
        location_detail = zomato.get_location(loc, 1)
        detail = json.loads(location_detail)
        lat = 0
        lon = 0
        results = len(detail["location_suggestions"])
        if (results > 0):
            lat = detail["location_suggestions"][0]["latitude"]
            lon = detail["location_suggestions"][0]["longitude"]
        return results, lat, lon
        
    def get_restaurants(self, lat, lon, budgetmin, budgetmax , cuisine):
        cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
        d_rest = []
        executor = ThreadPoolExecutor(max_workers=5)
        for res_key in range(0, 101, 20):
            executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, d_rest)
        executor.shutdown()
        return d_rest
        
        
class VerifyCuisine(Action):

    def name(self):
        return "verify_cuisine"

    def run(self, dispatcher, tracker, domain):
        cuisines = ['chinese','mexican','italian','american','south indian','north indian']
        error_msg = "Sorry!! The cuisine you have selected is not supported. Please re-enter."
        cuisine = tracker.get_slot('cuisine')
        try:
            cuisine = cuisine.lower()
        except (RuntimeError, TypeError, NameError, AttributeError):
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('cuisine_ok', False)]
        if cuisine in cuisines:
            return [SlotSet('cuisine', cuisine), SlotSet('cuisine_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('cuisine_ok', False)]


def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, d_rest):
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json',
                'user-key': '1ab7e0cb5e13107753ac51b512c68a61'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
            cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
    except:
        return
    d = json.loads(results)
    d_rest.extend(d['restaurants'])


class VerifyBudget(Action):

    def name(self):
        return "verify_budget"

    def run(self, dispatcher, tracker, domain):
        budgetmin = None
        budgetmax = None
        error_msg = "Sorry!! Price range you have selected is not supported. Please re-enter."
        try:
            budgetmin = int(tracker.get_slot('budgetmin'))
            budgetmax = int(tracker.get_slot('budgetmax'))
        except ValueError:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', None), SlotSet('budgetmax', None), SlotSet('budget_ok', False)]
        min_dict = [0, 300, 700]
        max_dict = [300, 700]
        if budgetmin in min_dict and (budgetmax in max_dict or budgetmax > 700):
            return [SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('budget_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', 0), SlotSet('budgetmax', 10000), SlotSet('budget_ok', False)]


class VerifyLocation(Action):

    tier_1 = []
    tier_2 = []

    def __init__(self):
        self.tier_1 = ['ahmedabad', 'bangalore', 'chennai',
                       'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune']
        self.tier_2 = ['agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi',
                       'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal']
    def name(self):
        return "verify_location"
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if not (self.verify_location(loc)):
            dispatcher.utter_message(
                "Oops..!! We are not operating in " + loc + " yet. Please try another location.")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        else:
            return [SlotSet('location', loc), SlotSet("location_ok", True)]

    def verify_location(self, loc):
        return loc.lower() in self.tier_1 or loc.lower() in self.tier_2
        
        
class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
        
    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')

        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global d_email_restaurant
        email_rest_count = len(d_email_restaurant)
        # Construct the email 'subject' and the contents.
        d_email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n"
        for restaurant in d_email_restaurant:
            d_email_msg = d_email_msg + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + " with an average budget for two of Rs. " + str(restaurant['restaurant']['average_cost_for_two'])+ "\n" +"\n"

        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("skchatbot06@gmail.com", "Sk@chatbot")

        # Create the msg object
        msg = EmailMessage()

        # Fill in the message properties
        msg['Subject'] = d_email_subj
        msg['From'] = "skchatbot06@gmail.com"

        # Fill in the message content
        msg.set_content(d_email_msg)
        msg['To'] = to_email

        s.send_message(msg)
        s.quit()
        
        dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")
        return []
