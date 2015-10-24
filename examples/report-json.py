#!/usr/bin/env python3

import json
import jsonschema

filename = 'somafm.json'
data = json.loads(open(filename).read())
schema = json.loads(open('../channels.json').read())
try:
    jsonschema.validate(data, schema)
except jsonschema.ValidationError as e:
    print('ERROR: {} does not validate against schema'.format(filename))
    print(e.message)
    exit(1)
except jsonschema.SchemaError as e:
    print('ERROR: schema does not validate')
    print(e.message)
    exit(1)

print('channels {}:'.format(filename))
channels = data['channels']
for channel in channels:
    print('  channel id: {}'.format(channel['id']))
    for detail in sorted(channel.keys()):
        if detail == 'playlists':
            print('    {}:'.format(detail))
            for playlist in channel[detail]:
                print('      format:{} quality:{} url:{}'.format(playlist['format'], playlist['quality'], playlist['url']))
        else:
            print('    {}: {}'.format(detail, channel[detail]))
