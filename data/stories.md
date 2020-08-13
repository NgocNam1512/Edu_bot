## path 1
* ask_fee
  - utter_return_fee

## path 2
* ask_food
  - utter_return_menu
* goodbye
  - utter_goodbye

## path 3
* ask_food
  - utter_return_menu
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## happy path 2
* ask_fee
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

## ask fee
* ask_fee
  - respond_fee

## student form
* contact_inform
  - student_form   <!--Run the form action-->
  - form{"name": "student_form"} <!--Activate form-->
  - form{"name": null}  <!--Deactivate form-->

## student form2
* contact_inform
  - student_form   <!--Run the form action-->
  - form{"name": "student_form"} <!--Activate form-->
* ask_fee
  - respond_fee
  - utter_ask_to_continue_form
* confirm
  - student_form
  - form{"name": null}

## explain name
* contact_inform
  - student_form
  - form{"name": "student_form"}
  - slot{"requested_slot": "student_name"}
* need_explain
  - utter_explain_name
  - utter_ask_to_continue_form
* confirm
  - student_form
  - form{"name": null}

## explain name
* contact_inform
  - student_form
  - form{"name": "student_form"}
  - slot{"requested_slot": "student_id"}
* need_explain
  - utter_explain_id
  - utter_ask_to_continue_form
* confirm
  - student_form
  - form{"name": null}

## out of scope
* out_of_scope
  - utter_out_of_scope