import logging
from datetime import timedelta

import requests
from django.conf import settings
from django.utils.crypto import get_random_string


def send_verification_code(phone_number):
    url = "https://notify.eskiz.uz/api/message/sms/send"
    from utils.verification import get_sms_service_token

    code = "1234"  # get_random_string(length=6, allowed_chars="1234567890")
    text = f"GST.uz tasdiqlash kod: {code}"  # noqa
    msg_from = "4546"
    payload = {
        "mobile_phone": phone_number.lstrip("+"),
        "message": text,
        "from": msg_from,
    }
    token = get_sms_service_token()
    if not token:
        logging.error("Failed to obtain SMS service token. Aborting SMS send request.")
        return

    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.post(
            url=url, headers=headers, data=payload
        )
    except Exception as err:
        logging.error(err)
    else:
        return code


def update_expired_at_field(verification_code):
    verification_code.expired_at = verification_code.updated_at + timedelta(minutes=settings.VERIFICATION_CODE_LIFETIME)
    verification_code.save(update_fields=["expired_at"])
