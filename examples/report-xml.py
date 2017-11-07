#!/usr/bin/env python3

from lxml import etree

filename = 'intergalacticfm.xml'
datafile = etree.parse(filename)
schema_doc = etree.parse('../channels.xsd')
schema = etree.XMLSchema(schema_doc)
schema.assertValid(datafile)
#if not schema.validate(datafile):
#    print('ERROR: {} does not validate against schema'.format(filename))
#    exit(1)

output = open(filename[:-3] + 'md', 'w')
output.write('# file: {}\n\n'.format(filename))
root = datafile.getroot()
for channel in root.iterfind('./channel'):
    print(channel.tag)
    print('  {} id: {}'.format(channel.tag, channel.attrib['id']))
    output.write('## {} id: {}\n'.format(channel.tag, channel.attrib['id']))
    for detail in channel:
        if str(type(detail)) == "<class 'lxml.etree._Comment'>":
            continue
        if detail.tag[-3:] == 'pls':
            print('    {} format:{} {}'.format(
                detail.tag, detail.attrib['format'], detail.text))
            output.write('\n\n{}: {} {}\n'.format(detail.tag, detail.attrib['format'], detail.text))
        else:
            if detail.tag in ('title', 'description', ):
                output.write('\n\n{}: {}\n'.format(detail.tag, detail.text))
            elif 'image' in detail.tag:
                output.write('\n\n{}: {}\n'.format(detail.tag, detail.text))
                output.write('\n[![{}]({})]({})\n'.format(detail.text, detail.text, detail.text))
            print('    {}: {}'.format(detail.tag, detail.text))