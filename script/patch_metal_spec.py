#!/usr/bin/env python3

import yaml
import os
from yaml.loader import FullLoader
import copy
import sys
from collections import OrderedDict

if len(sys.argv) != 3:
    print("Usage: {} <input file> <output file>".format(sys.argv[0]))
    sys.exit(1)

INFILE = sys.argv[1]
OUTFILE = sys.argv[2]


def setup_yaml():
    """ https://stackoverflow.com/a/8661021 """

    def represent_dict_order(self, data): return self.represent_mapping(
        'tag:yaml.org,2002:map', data.items())
    yaml.add_representer(OrderedDict, represent_dict_order)


setup_yaml()

def loadYaml(fn):
    with open(fn) as f:
        return yaml.load(f, Loader=FullLoader)


originalSpec = loadYaml(INFILE)

fixedSpec = copy.deepcopy(originalSpec)

# FIX 0. organization href to project
fixedSpec['components']['schemas']['Project']['properties']['organization'] = {
    "$ref": "#/components/schemas/Href"
}

# FIX 1. href property to all schemas if they have "properties" and don't already have "href"
for s in fixedSpec['components']['schemas']:
    if 'properties' in fixedSpec['components']['schemas'][s]:
        if 'href' not in fixedSpec['components']['schemas'][s]['properties']:
            fixedSpec['components']['schemas'][s]['properties']['href'] = {
                "type": "string",
                "format": "uri"
            }

# FIX 2. remove defaults for always_pxe and hardware_reservation_id
fixSchemas = ["DeviceCreateInput"]
removeProperties = ["always_pxe", "hardware_reservation_id"]
for s in fixSchemas:
    for p in removeProperties:
        if p in fixedSpec['components']['schemas'][s]['properties']:
            del fixedSpec['components']['schemas'][s]['properties'][p]['default']


# FIX 5. add backend_transfer_enabled to Project Schema
project_props = fixedSpec['components']['schemas']['Project']['properties']
project_props['backend_transfer_enabled'] = {'type': 'boolean'}

# FIX 8. make requested_by mandatory for parsing ip reservation
# .. in order to distinguish from ip assignment and vrf

fixedSpec['components']['schemas']['IPAssignment']['required'] = [
    'assigned_to']

# FIX 9. make  IPReservation assignments href, instead of IPAssignment,
# .. so that it's not parsed as a list of IPAssignments which has mandatory fields

fixedSpec['components']['schemas']['IPReservation']['properties']['assignments']['items'] = {
    "$ref": "#/components/schemas/Href"
}

# FIX 11. Make all Address parameters non-mandatory

del fixedSpec['components']['schemas']['Address']['required']

# FIX 13. rename query attribute categories to "categories[]"

plans_get_params = fixedSpec['paths']['/plans']['get']['parameters']

for i, p in enumerate(plans_get_params):
    if p['name'] == 'categories':
        fixedSpec['paths']['/plans']['get']['parameters'][i]['name'] = "categories[]"
        break



# Mark paginated operation with `x-equinix-metal-paginated-property`

refkey = "$ref"

page_param_marker = 'x-equinix-metal-page-param'

for opPath, methods in fixedSpec['paths'].items():
    if 'get' not in methods:
        continue
    getOp = methods['get']
    if 'parameters' not in getOp:
        continue
    getOpParams = getOp['parameters']
    for i, p in enumerate(getOpParams):
        if p['name'] == 'page':
            fixedSpec['paths'][opPath]['get']['parameters'][i][page_param_marker] = True
            respSchemaPath = getOp['responses']['200']['content']['application/json']['schema'][refkey]
            respSchemaName = os.path.basename(respSchemaPath)
            oid = getOp['operationId']
            respSchemaProperties = set(fixedSpec['components']['schemas'][respSchemaName]['properties'].keys())
            if 'href' in respSchemaProperties:
                respSchemaProperties.remove("href")
            if 'meta' in respSchemaProperties:
                respSchemaProperties.remove("meta")
            else:
                print("%s => %s doesn't have 'meta', and therefore no PageNum etc" % (oid, respSchemaName))
                break
            if len(respSchemaProperties) > 1:
                print("%s => %s has 'page' but ambiguous response type with args %s" %
                      (oid, respSchemaName, respSchemaProperties))
                break
            print("marking %s as paginated" % oid)
            fixedSpec['paths'][opPath]['get']['x-equinix-metal-paginated-property'] = respSchemaProperties.pop()
            fixedSpec['paths'][opPath]['get']['parameters'][i] 

with open(OUTFILE, 'w') as f:
    originalSpec = yaml.dump(
        fixedSpec, f, default_flow_style=False)


print(INFILE, "was fixed into", OUTFILE)
