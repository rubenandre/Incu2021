from flask import Flask, request
import requests
import json
import os

bot_name = os.getenv('BOT_NAME')
token = os.getenv('BOT_TOKEN')
header = {"content-type": "application/json; charset=utf-8",
          "authorization": "Bearer " + token}

app = Flask(__name__)


def get_random_chuck_norris_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url).json()
    return response['value']


def get_random_meal():
    url = 'https://www.themealdb.com/api/json/v1/1/random.php'
    response = requests.get(url).json()
    meal = response['meals'][0]

    ingredients_quantity = []

    instructions = str(meal['strInstructions']).replace("\r", "")

    for i in range(1, 20):
        ingredient = meal[f'strIngredient{i}']
        quantity = meal[f'strMeasure{i}']

        if ingredient == "" or quantity == "":
            break

        ingredients_quantity.append((ingredient, quantity))

    def build_ingredients_text():
        text = ""
        for element in ingredients_quantity:
            text += f'{element[0]} ({element[1]})\n'
        return text

    return f'''
**Name:** {meal['strMeal']}
**Type:** {meal['strCategory']}
**Country:** {meal['strArea']}

**Ingredients**
{build_ingredients_text()}

**Instructions**
{instructions}

**Tutorial**
{meal["strYoutube"]}
    ''', meal['strMealThumb']


def build_bot_help_message():
    return '''
Welcome to my Bot!
    
What I can do for you:
- Print this message `help`
- Tell you a chuck norris joke `chuck`
- Give you a random meal `meal`
- Show you a random cat picture `cat`
- Show you a random dog picture `dog`
    '''


def get_random_cat_pic():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url).json()
    return response[0]['url']


def get_random_dog_pic():
    url = "https://random.dog/woof.json"
    response = requests.get(url).json()
    return response['url']


def get_csrv1000_interface_informations():
    url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface"
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    response = requests.get(url, auth=('developer', 'C1sco12345'), headers=headers, verify=True).json()

    text = ""

    for interface in response['Cisco-IOS-XE-native:interface']['GigabitEthernet']:
        text += f"**Name:** GigabitEthernet{interface['name']}\n"
        try:
            address = interface["ip"]["address"]["primary"]["address"]
            mask = interface["ip"]["address"]["primary"]["mask"]
            text += f"**Address:** {address} netmask {mask}\n"
        except:
            text += "**Address:** \- \n"
        try:
            _ = interface["shutdown"]
            text += "**Status:** shutdown\n\n"
        except:
            text += "**Status** up\n\n"

        text += '---\n\n'

    return text

@app.route("/", methods=["GET", "POST"])
def send_message():
    webhook = request.json
    url = 'https://webexapis.com/v1/messages'
    msg = {"roomId": webhook["data"]["roomId"]}
    sender = webhook["data"]["personEmail"]
    message = get_message()
    if sender != bot_name:
        if message == "help":
            msg["markdown"] = build_bot_help_message()
        elif message == "chuck":
            msg["markdown"] = get_random_chuck_norris_joke()
        elif message == "meal":
            response, image = get_random_meal()
            msg["markdown"] = response
            msg["files"] = image
        elif message == "cat":
            msg["files"] = get_random_cat_pic()
        elif message == "dog":
            msg["files"] = get_random_dog_pic()
        elif message == "csr interfaces":
            msg["markdown"] = get_csrv1000_interface_informations()
        else:
            msg["markdown"] = "Sorry! I don't learn how to do that, but if you yype **help** you can see the " \
                              "fantastic things that I can do "
        requests.post(url, data=json.dumps(msg), headers=header, verify=True)
    return 'OK'


def get_message():
    webhook = request.json
    url = 'https://webexapis.com/v1/messages/' + webhook["data"]["id"]
    get_msgs = requests.get(url, headers=header, verify=True)
    message = get_msgs.json()['text']
    return message


app.run(debug=True)
