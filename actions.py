from typing import Dict, Text, Any, List, Union
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from rasa_sdk import Tracker, Action
from rasa_sdk.events import AllSlotsReset, SlotSet, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import re
import smtplib

carInfo = {
    "BMW": [{"model": "320D GRAN TURISMO", "variant": "320D GT SPORT LINE ", "year": "2016", "type": "petrol",
             "mileage": "23000"},
            {"model": "320I", "variant": "LUXURY LINE ", "type": "diesel", "year": "2014",
             "mileage": "13000"},
            {"model": "5 SERIES", "variant": "5 SERIES 530D M SPORT", "type": "diesel", "year": "2010",
             "mileage": "14000"}],
    "Audi": [
        {"model": "A4", "variant": "1.8 TFSI NAVI EDITION", "type": "diesel", "year": "2000", "mileage": "4000"},
        {"model": "A6", "variant": "2.0 TDI NAVIGATION EDITION", "type": "petrol", "year": "2002", "mileage": "44000"},
        {"model": "A8", "variant": "3.0 TDI QUATTRO PANORAMIC SUNROOF", "type": "diesel", "year": "2020",
         "mileage": "34000"}]
}


class SendMail(Action):
    def name(self) -> Text:
        return "action_send_mail"

    @staticmethod
    def send_email(message, senderEmail, carMake, carModel, carVariant, carYear, carType,
                   carMileage):
        fromaddr = 'hemanth@krtrimaiq.ai'
        password = '5?4-uHo%_7o_'
        toaddrs = 'gantahemanth1995@gmail.com'
        server_smtp = 'mail.krtrimaiq.ai'
        port_smtp = 465

        try:
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddrs
            msg['Subject'] = "Your car Quote"
            body = "The price of {} -- {} -- {} -- {} -- {} -- {} is 5000 dollars".format(carMake, carModel, carVariant,
                                                                                          carYear,
                                                                                          carType, carMileage)
            msg.attach(MIMEText(body, 'plain'))
            # filename = "test.pdf"
            # attachment = open("./data/test.pdf", "rb")
            # p = MIMEBase('application', 'octet-stream')
            # p.set_payload((attachment).read())
            # encoders.encode_base64(p)
            # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            # msg.attach(p)
            s = 
            s.set_debuglevel(True)
            s.esmtp_features['auth'] = 'LOGIN PLAIN'
            s.login()

            text = msg.as_string()

            # sending the mail
            s.sendmail(fromaddr, toaddrs, text)
            s.quit()
            print("Mail successful")
        except smtplib.SMTPServerDisconnected:
            print("smtplib.SMTPServerDisconnected")
        except smtplib.SMTPResponseException as e:
            print("smtplib.SMTPResponseException: " + str(e.smtp_code) + " " + str(e.smtp_error))
        except smtplib.SMTPSenderRefused:
            print("smtplib.SMTPSenderRefused")
        except smtplib.SMTPRecipientsRefused:
            print("smtplib.SMTPRecipientsRefused")
        except smtplib.SMTPDataError:
            print("smtplib.SMTPDataError")
        except smtplib.SMTPConnectError:
            print("smtplib.SMTPConnectError")
        except smtplib.SMTPHeloError:
            print("smtplib.SMTPHeloError")
        except smtplib.SMTPAuthenticationError:
            print("smtplib.SMTPAuthenticationError")

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        senderEmail = tracker.get_slot('email_id')
        carMake = tracker.get_slot('slot_car_make')
        carModel = tracker.get_slot('slot_car_model')
        carVariant = tracker.get_slot('slot_car_variant')
        carYear = tracker.get_slot('slot_car_year')
        carType = tracker.get_slot('slot_car_type')
        carMileage = tracker.get_slot('slot_car_mileage')
        self.send_email("this is a test message", senderEmail, carMake, carModel, carVariant, carYear, carType,
                        carMileage)
        dispatcher.utter_message(template="utter_mail_send")
        return []


class CarMake(Action):
    def name(self) -> Text:
        return "action_car_make"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = []
        for value in carInfo.keys():  # dynamic buttons
            buttons.append(
                {"title": value,
                 "payload": "/car_model_intent" + '{' + '"slot_car_make"' + ': ' + '"' + value + '"' + '}'})

        dispatcher.utter_button_message("Please select the make:", buttons)
        return []


class CarModel(Action):
    def name(self) -> Text:
        return "action_car_model"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = []
        for modelValue in carInfo[tracker.get_slot('slot_car_make')]:
            buttons.append(
                {"title": modelValue['model'],
                 "payload": "/car_variant_intent" + '{' + '"slot_car_model"' + ': ' + '"' + modelValue[
                     'model'] + '"' + '}'})

        dispatcher.utter_button_message("Please select the Model:", buttons)
        return []


class CarVariant(Action):
    def name(self) -> Text:
        return "action_car_variant"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = []
        for modelValue in carInfo[tracker.get_slot('slot_car_make')]:
            if (modelValue['model'] == tracker.get_slot('slot_car_model')):
                buttons.append(
                    {"title": modelValue['variant'],
                     "payload": "/car_year_intent" + '{' + '"slot_car_variant"' + ': ' + '"' + modelValue[
                         'variant'] + '"' + '}'})

        dispatcher.utter_button_message("Please select the variant:", buttons)
        return []


class CarYear(Action):
    def name(self) -> Text:
        return "action_car_year"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = []
        for modelValue in carInfo[tracker.get_slot('slot_car_make')]:
            if (modelValue['model'] == tracker.get_slot('slot_car_model') and modelValue['variant'] == tracker.get_slot(
                    'slot_car_variant')):
                buttons.append(
                    {"title": modelValue['year'],
                     "payload": "/car_type_intent" + '{' + '"slot_car_year"' + ': ' + '"' + modelValue[
                         'year'] + '"' + '}'})

        dispatcher.utter_button_message("Please select the year:", buttons)
        return []


class CarType(Action):
    def name(self) -> Text:
        return "action_car_type"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = []
        for modelValue in carInfo[tracker.get_slot('slot_car_make')]:
            if (modelValue['model'] == tracker.get_slot('slot_car_model') and modelValue['variant'] == tracker.get_slot(
                    'slot_car_variant')):
                buttons.append(
                    {"title": modelValue['type'],
                     "payload": "/car_mileage_intent" + '{' + '"slot_car_type"' + ': ' + '"' + modelValue[
                         'type'] + '"' + '}'})

        dispatcher.utter_button_message("Please select the type:", buttons)
        return []


class CarMileage(Action):
    def name(self) -> Text:
        return "action_car_mileage"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = []
        for modelValue in carInfo[tracker.get_slot('slot_car_make')]:
            if (modelValue['model'] == tracker.get_slot('slot_car_model') and modelValue['variant'] == tracker.get_slot(
                    'slot_car_variant')):
                buttons.append(
                    {"title": modelValue['mileage'],
                     "payload": "/car_info_review_intent" + '{' + '"slot_car_mileage"' + ': ' + '"' + modelValue[
                         'mileage'] + '"' + '}'})

        dispatcher.utter_button_message("Please select the Mileage:", buttons)
        return []


class NewCarForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "new_car_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["customer_name", "phone_no", "email_id"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "customer_name": self.from_entity(entity="customer_name", intent="inform"),
            "email_id": [self.from_entity(entity="email", intent="inform"), self.from_text()],
            "phone_no": [
                self.from_entity(
                    entity="phone", intent=["inform"]
                ),
            ]
        }

    # USED FOR DOCS: do not rename without updating in docs

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_phone_no(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        regexNum = "\+?\d[\d -]{8,12}\d"
        if re.search(regexNum, value):
            return {"phone_no": value}
        else:
            # dispatcher.utter_message(template="utter_wrong_phone_no")
            # validation failed, set slot to None
            return {"phone_no": None}

    def validate_customer_name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        regexName = "^[a-zA-Z]{3,}(?: [a-zA-Z]+){0,2}$"
        if re.search(regexName, value):
            return {"customer_name": value}
        else:
            # dispatcher.utter_message(template="utter_wrong_customer_name")
            # validation failed, set slot to None
            return {"customer_name": None}

    def validate_email_id(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        print(value)
        if re.search(regex, value):
            return {"email_id": value}
        else:
            # dispatcher.utter_message(template="utter_wrong_email_id")
            # validation failed, set slot to None
            return {"email_id": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []


class CorrectCusInfo(Action):

    def name(self) -> Text:
        return "action_correct_cus_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("customer_name", None), SlotSet("email_id", None), SlotSet("phone_no", None)]


class CorrectCarInfo(Action):

    def name(self) -> Text:
        return "action_correct_car_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("slot_car_make", None), SlotSet("slot_car_model", None), SlotSet("slot_car_variant", None),
                SlotSet("slot_car_year", None), SlotSet("slot_car_mileage", None), SlotSet("slot_car_type", None)]


class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]


class ActionOutOfScope(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_out_of_scope"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_out_of_scope", tracker)
        return [UserUtteranceReverted()]


class ActionThank(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_thankyou"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_noworries", tracker)
        return [UserUtteranceReverted()]
