#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## path 1
* greet
  - utter_greet
* ask_fee
  - utter_return_fee

## path 2
* greet
  - utter_greet
* ask_food
  - utter_return_menu
* goodbye
  - utter_goodbye

## path 3
* greet
  - utter_greet
* ask_food
  - utter_return_menu
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## happy path 2
* greet
  - utter_greet
* ask_fee:
  - utter_return_fee
* ask_food
  - utter_return_menu
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## greet
* greet
  - utter_greet

