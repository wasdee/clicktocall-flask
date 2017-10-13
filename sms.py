from twilio.rest import Client
import clicktocall.local_settings as settings


# Voice Request URL
def sms(phone_number="+66949949529"):

    try:
        twilio_client = Client(settings.TWILIO_ACCOUNT_SID,
                               settings.TWILIO_AUTH_TOKEN)
    except Exception as e:
        msg = 'Missing configuration variable: {0}'.format(e)
        print({'error': msg})

    try:
        twilio_client.messages.create(from_=settings.TWILIO_CALLER_ID,
                                   to=phone_number,
                                   body="Jack the ripper")
    except Exception as e:
        print(e)

    return

if __name__ == '__main__':
    sms("+66956241997")