import json
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect, \
    HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from streambossweb.web.client import StreamBossClient

js_mimetype = "application/javascript"


def _get_client():
    return StreamBossClient()


def has_all_required_params(params, content):
    for param in params:
        if param not in content:
            return False

    return True


@csrf_exempt
@require_http_methods(['GET'])
def stream_resource(request, stream_name):

    stream = {}
    h = HttpResponse(json.dumps(stream), mimetype=js_mimetype)
    return h


@csrf_exempt
@require_http_methods(['GET', 'POST', 'DELETE'])
def streams(request):

    if request.method == 'GET':
        sb = _get_client()
        streams = sb.get_streams()
        h = HttpResponse(json.dumps(streams), mimetype=js_mimetype)
        return h

    elif request.method == 'POST':
        sb = _get_client()
        try:
            content = json.loads(request.body)
        except:
            msg = "Bad request (%s). No JSON." % request.body
            return HttpResponseBadRequest(msg)

        required_params = ['stream_name', ]
        if not has_all_required_params(required_params, content):
            return HttpResponseBadRequest("Bad request. Do not have all required parameters (%s)" % required_params)

        name = content['stream_name']

        sb.create_stream(name)
        ret = {
            'stream_name': name
        }
        h = HttpResponse(json.dumps(ret), mimetype=js_mimetype)
        return h

    elif request.method == 'DELETE':
        pass


@csrf_exempt
@require_http_methods(['GET'])
def operation_resource(request, operation_name):

    operation = {}
    h = HttpResponse(json.dumps(operation), mimetype=js_mimetype)
    return h


@csrf_exempt
@require_http_methods(['GET', 'POST', 'DELETE'])
def operations(request):

    if request.method == 'GET':
        sb = _get_client()
        operations = sb.get_operations()

        h = HttpResponse(json.dumps(operations), mimetype=js_mimetype)
        return h

    elif request.method == 'POST':
        sb = _get_client()
        try:
            content = json.loads(request.body)
        except:
            msg = "Bad request (%s). No JSON." % request.body
            return HttpResponseBadRequest(msg)

        required_params = ['operation_name', 'process_definition_id', 'input_stream', 'output_stream']
        if not has_all_required_params(required_params, content):
            return HttpResponseBadRequest("Bad request. Do not have all required parameters (%s)" % required_params)

        name = content['operation_name']
        process_definition_id = content['process_definition_id']
        input_stream = content['input_stream']
        output_stream = content['output_stream']

        sb.create_operation(name, process_definition_id, input_stream, output_stream)
        ret = {
            'operation_name': name,
            'process_definition_id': process_definition_id,
            'input_stream': input_stream,
            'output_stream': output_stream,
        }
        h = HttpResponse(json.dumps(ret), mimetype=js_mimetype)
        return h
    elif request.method == 'DELETE':
        pass
