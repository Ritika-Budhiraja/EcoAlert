import time
from twilio.rest import Client

# Your Twilio account credentials
account_sid = 'AC54dc289aae23297f31b290ef7f0d30e0'
auth_token =  '2de1e9e44e112cc00b2987080af029c8'

# Twilio phone number and recipient phone number
twilio_phone_number = +13344714627
recipient_phone_number = +918178714447

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Function to check weight and send SMS if weight is reducing constantly
def check_and_send_sms():
    # Code to get the current weight of the gas cylinder
    current_weight = get_current_weight()  # You need to implement this function

    # Assuming you have a previous weight stored somewhere
    previous_weight = get_previous_weight()  # You need to implement this function

    # Compare current weight with previous weight
    if current_weight < previous_weight:
        # Send SMS if weight is reducing
        message = client.messages.create(
            body="Warning: Gas cylinder weight is reducing constantly",
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        print("SMS Sent:", message.sid)
    else:
        print("Gas cylinder weight is not much stable.")

    # Update previous weight
    update_previous_weight(current_weight)  # You need to implement this function

# Function to simulate getting the current weight of the gas cylinder
def get_current_weight():
    # Replace this with your code to get the actual current weight
    # For demonstration purposes, I'm just returning a random number
    import random
    return random.randint(20, 50)  # Assuming weight is between 20 to 50

# Function to simulate getting the previous weight of the gas cylinder
def get_previous_weight():
    # Replace this with your code to get the actual previous weight
    # For demonstration purposes, I'm just returning a constant value
    return 30  # Assuming previous weight was 30

# Function to update the previous weight with the current weight
def update_previous_weight(current_weight):
    # Replace this with your code to update the previous weight
    # For demonstration purposes, I'm just printing the current weight
    print("Previous weight updated to:", current_weight)

# Main loop to continuously check and send SMS
while True:
    check_and_send_sms()
    # Sleep for some time before checking again (e.g., every hour)
    time.sleep(3600)  # Sleep for 1 hour
