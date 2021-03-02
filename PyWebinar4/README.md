# My PyWebinar4 Webex Bot

## How to use this bot?

Set the follow env variables:
- BOT_NAME (normaly the bot username follow by @webex.com)
- BOT_TOKEN

## What the bot can do?

| **Bot Command**   | **Description**                                                               |
|:-----------------:|-------------------------------------------------------------------------------|
| `cat`             | Displays a random picture of a cat                                            |
| `dog`             | Displays a random picture of a dog                                            |   
| `chuck`           | Texts a random chuck norris joke                                              |
| `meal`            | Display detail information of a meal: country, ingredients, instructions, ... |
| `csr interfaces`  | Display the interfaces of a public CSRv1000 device                            |

### Cat Feature

**API Used:** [thecatapi.com](https://api.thecatapi.com/v1/images/search)

![NOT_FOUND](./images/cat_output.png)

### Dog Feature

**Api Used:** [random.dog](https://random.dog/woof.json)

![NOT_FOUND](./images/dog_output.png)

### Chuck Feature

**Api Used:** [chucknorris.io](https://api.chucknorris.io/jokes/random)

![NOT_FOUND](./images/chuck_output.png)

### Meal Feature

**Api Used:** [themealdb.com](https://www.themealdb.com)

![NOT_FOUND](./images/meal_output.png)

### CSRv1000 Interfaces Feature

- Used an always on CSRv1000 instance: sandbox-iosxe-latest-1.cisco.com
- Used RestConf

![NOT_FOUND](./images/csr_output.png)