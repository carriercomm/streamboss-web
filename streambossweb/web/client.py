import os

from dashi import DashiConnection

RMQHOST = os.environ.get('STREAMBOSS_RABBITMQ_HOST', 'localhost')
RMQPORT = os.environ.get('STREAMBOSS_RABBITMQ_PORT', 5672)
RABBITMQ_USER = os.environ.get('STREAMBOSS_RABBITMQ_USER', 'guest')
RABBITMQ_PASSWORD = os.environ.get('STREAMBOSS_RABBITMQ_PASSWORD', 'guest')
RABBITMQ_VHOST = os.environ.get('STREAMBOSS_RABBITMQ_VHOST', '/')
RABBITMQ_EXCHANGE = os.environ.get('STREAMBOSS_RABBITMQ_EXCHANGE', 'default_dashi_exchange')


class StreamBossClient(object):

    def __init__(self):
        self.topic = "streamboss"
        self.dashi = DashiConnection("streambossweb",
                'amqp://%s:%s@%s:%s//' % (
                    RABBITMQ_USER,
                    RABBITMQ_PASSWORD, RMQHOST,
                    RMQPORT),
                RABBITMQ_EXCHANGE, ssl=False, sysname=None)

    def get_streams(self):
        return self.dashi.call(self.topic, "get_all_streams")

    def create_stream(self, stream_name):
        self.dashi.call(self.topic, "create_stream", stream_name=stream_name)

    def create_operation(self, operation_name, process_definition_id, input_stream, output_stream):
        self.dashi.call(self.topic, "create_operation", operation_name=operation_name,
            process_definition_id=process_definition_id, input_stream=input_stream,
            output_stream=output_stream)

    def get_operations(self):
        return self.dashi.call(self.topic, "get_all_operations")
