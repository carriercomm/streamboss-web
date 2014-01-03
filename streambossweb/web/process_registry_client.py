import os
import json
import requests
import logging

log = logging.getLogger(__name__)

PROCESS_REGISTRY_HOSTNAME = os.environ.get('PROCESS_REGISTRY_HOSTNAME', 'localhost')
PROCESS_REGISTRY_PORT = int(os.environ.get('PROCESS_REGISTRY_PORT', 8080))
PROCESS_REGISTRY_USERNAME = os.environ.get('PROCESS_REGISTRY_USERNAME', 'guest')
PROCESS_REGISTRY_PASSWORD = os.environ.get('PROCESS_REGISTRY_PASSWORD', 'guest')


class ProcessRegistryClient(object):

    def get_processes(self):
        try:
            r = requests.get('http://%s:%s/api/process_definition/' % (
                PROCESS_REGISTRY_HOSTNAME, PROCESS_REGISTRY_PORT),
                auth=(PROCESS_REGISTRY_USERNAME, PROCESS_REGISTRY_PASSWORD))
        except Exception:
            print "Problem connecting to process registry"
            return None

        if r.status_code == 200:
            if r.headers['content-type'] == "application/json":
                definitions = r.json()['objects']
            else:
                log.error("Definition %d not json: %s" % ("", r.text))
                return None
        else:
            log.error("Could not find definition %s" % "")
            return None

        return definitions

    def create_process(self, process_name, application, executable):
        data = json.dumps({
            'definition': {
                'process_name': process_name,
                'application': application,
                'exec': executable
            }
        })
        try:
            headers = {'content-type': 'application/json'}
            r = requests.post('http://%s:%s/api/process_definition/' % (
                PROCESS_REGISTRY_HOSTNAME, PROCESS_REGISTRY_PORT),
                data=data, headers=headers,
                auth=(PROCESS_REGISTRY_USERNAME, PROCESS_REGISTRY_PASSWORD))
        except Exception:
            print "Problem connecting to process registry"
            return None

        print r.content
        if r.status_code == 200:
            if r.headers['content-type'] == "application/json":
                definitions = r.json()['objects']
            else:
                log.error("Definition %d not json: %s" % ("", r.text))
                return None
        else:
            log.error("Could not find definition %s" % "")
            return None

        return definitions
