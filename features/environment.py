from unittest.mock import patch


def before_all(context):
    context.requests_patcher = patch('grabclient.client.requests', spec=True)
    context.requests_mock = context.requests_patcher.start()


def after_all(context):
    context.requests_patcher.stop()
