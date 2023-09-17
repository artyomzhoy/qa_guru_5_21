import json
import allure
from allure_commons.types import AttachmentType


def add_curl(message):
    allure.attach(
        body=message.encode('utf8'),
        name='Curl',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )


def add_response_json(response):
    allure.attach(
        body=json.dumps(response.json(), indent=4).encode('utf8'),
        name='Response JSON',
        attachment_type=AttachmentType.JSON,
        extension='json')


def add_empty_response(response):
    allure.attach(
        body='Empty response',
        name='Empty response',
        attachment_type=AttachmentType.TEXT,
        extension='txt')

