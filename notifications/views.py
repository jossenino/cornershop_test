import datetime
from django.shortcuts import render

from menus.models import Menus, MenusDishes, Dishes
from .models import Notifications
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Create your views here.
def create_notifications(request):
    dishes = []
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    menus = Menus.objects.get(create_date=(datetime.date.today()))
    if request.method == 'POST':
        create_notification = Notifications.objects.create(type = 'slack', 
                                                           description = 'Notification for slack channel',
                                                           send_date = datetime.date.today(),
                                                           menus_id = Menus.objects.get(id = menus.id, description = menus.description, create_date = menus.create_date, url_id = menus.url_id))
        
        client = WebClient(token='xoxb-1660361739158-1664060132981-0xwdFkeKtj54TTmG3fDLHK2W')
        try:
            slack_message = "We have a new menu available for you, please access the following link for more information -> http://localhost:8000/menus/show/" + str(menus.url_id)
            response = client.chat_postMessage(channel='#general', text=slack_message)
            #assert response["message"]["text"] == "Hello world!"
            print(response["message"]["text"])
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            print(f"Got an error: {e.response['error']}")
    return render(request, 'notifications/create.html', {'menus':  menus})