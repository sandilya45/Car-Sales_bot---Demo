## happy path
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* out_of_scope
    - utter_out_of_scope
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
   - utter_car_info
   - utter_check_car_info
* get_quote
   - utter_get_quote
   - utter_send_email
* get_correct_car_info
    - action_correct_car_info
    - utter_correct_car_details
    - action_car_make
* send_email
    - action_send_mail
* restart
    - action_restart
* thankyou
    - utter_noworries


## happy path with existing policy   
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* existing_policy
    - utter_existing_policy
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* out_of_scope
    - utter_out_of_scope
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
   - utter_car_info
   - utter_check_car_info
* get_quote
   - utter_get_quote
   - utter_send_email
* send_email
    - action_send_mail
* thankyou
    - utter_noworries
* restart
    - action_restart
* out_of_scope
    - utter_out_of_scope

## unhappy path
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
* out_of_scope
    - utter_out_of_scope
    - new_car_form
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* out_of_scope
    - utter_out_of_scope
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
    - utter_car_info
   - utter_check_car_info
* get_correct_car_info
    - action_correct_car_info
    - utter_correct_car_details
    - action_car_make
* restart
    - action_restart
* get_quote
   - utter_get_quote
   - utter_send_email
* send_email
    - action_send_mail
* thankyou
    - utter_noworries

## unhappy path with existing policy
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* out_of_scope
    - utter_out_of_scope
* existing_policy
    - utter_existing_policy
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
* out_of_scope
    - utter_out_of_scope
    - new_car_form
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
   - utter_car_info
   - utter_check_car_info
* get_quote
   - utter_get_quote
   - utter_send_email
* send_email
    - action_send_mail
* restart
    - action_restart
* thankyou
    - utter_noworries

## very unhappy path
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
* out_of_scope
    - utter_out_of_scope
    - new_car_form
* out_of_scope
    - utter_out_of_scope
    - new_car_form
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
   - utter_car_info
   - utter_check_car_info
* get_correct_car_info
    - action_correct_car_info
    - utter_correct_car_details
    - action_car_make
* get_quote
   - utter_get_quote
   - utter_send_email
* send_email
    - action_send_mail
* thankyou
    - utter_noworries

## very unhappy path with existing policy
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
* existing_policy
    - utter_existing_policy
* out_of_scope
    - utter_out_of_scope
    - new_car_form
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
   - utter_car_info
   - utter_check_car_info
* get_quote
   - utter_get_quote
   - utter_send_email
* send_email
    - action_send_mail
* restart
    - action_restart
* thankyou
    - utter_noworries

## stop but continue path
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
* stop
    - utter_ask_continue
* affirm
    - new_car_form
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* restart
    - action_restart
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
   - utter_car_info
   - utter_check_car_info
* get_correct_car_info
    - action_correct_car_info
    - utter_correct_car_details
    - action_car_make
* get_quote
   - utter_get_quote
   - utter_send_email
* send_email
    - action_send_mail
* thankyou
    - utter_noworries


## out_of_scope stop but continue path
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
* out_of_scope
    - utter_out_of_scope
    - new_car_form
* stop
    - new_car_form 
* affirm
    - new_car_form
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* restart
    - action_restart
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
   - utter_car_info
   - utter_check_car_info
* get_quote
   - utter_get_quote
   - utter_send_email
* send_email
    - action_send_mail
* thankyou
    - utter_noworries

## stop but continue and out_of_scope path
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
* stop
    - new_car_form
* affirm
    - new_car_form
* restart
    - action_restart
* out_of_scope
    - utter_out_of_scope
    - new_car_form
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
   - utter_car_info
   - utter_check_car_info
* get_correct_car_info
    - action_correct_car_info
    - utter_correct_car_details
    - action_car_make
* get_quote
   - utter_get_quote
   - utter_send_email
* send_email
    - action_send_mail
* thankyou
    - utter_noworries

## out_of_scope stop but continue and out_of_scope path
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
* existing_policy
    - utter_existing_policy
* out_of_scope
    - utter_out_of_scope
    - new_car_form
* stop
    - new_car_form
* restart
    - action_restart
* affirm
    - new_car_form
* existing_policy
    - utter_existing_policy
* out_of_scope
    - utter_out_of_scope
    - new_car_form
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* get_correct_cus_info
    - action_correct_cus_info
    - utter_cus_info
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* car_info
    - action_car_make
* car_model_intent
    - action_car_model
* car_variant_intent
    - action_car_variant
* car_year_intent
    - action_car_year
* car_type_intent
    - action_car_type
* car_mileage_intent
    - action_car_mileage
* car_info_review_intent
   - utter_car_info
   - utter_check_car_info
* get_correct_car_info
    - action_correct_car_info
    - utter_correct_car_details
    - action_car_make
* get_quote
   - utter_get_quote
   - utter_send_email
* send_email
    - action_send_mail
* thankyou
    - utter_noworries

## out_of_scope, stop and really stop path
* greet
    - utter_greet
    - utter_type_customer
    - new_car_form
    - form{"name": "new_car_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue
* new_car
    - new_car_form
    - form{"name": "new_car_form"}
* out_of_scope
    - utter_out_of_scope
    - new_car_form
* stop
    - new_car_form
* out_of_scope
    - utter_out_of_scope
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_existing_policy
* restart
    - action_restart

## bot challenge
* bot_challenge
  - utter_iamabot
