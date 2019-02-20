#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import xml.etree.ElementTree


def main():
    if len(sys.argv) != 2:
        print('Usage:\n\t{0} PATH/TO/MODULE.xml'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    module_xml = sys.argv[1]
    if not os.path.isfile(module_xml):
        print('No such file: {0}'.format(module_xml))
        sys.exit(1)
    if not os.access(module_xml, os.R_OK):
        print('File is not readable: {0}'.format(module_xml))
        sys.exit(1)

    root_elem = xml.etree.ElementTree.parse(module_xml).getroot()

    all_nodes = []
    for node_elem in root_elem.findall('tree/node'):
        name = node_elem.get('title')
        if len(name.strip()) > 0:
            container = (node_elem.get('category') == 'directory') or (len(node_elem.findall('node')) > 0)
            node = (name, container)
            all_nodes.append(node)

    unique_nodes = []
    [unique_nodes.append(node) for node in all_nodes if node not in unique_nodes]

    print(u'||Название||Контейнер?||')
    for node in unique_nodes:
        print(u'|{0}|{1}|'.format(node[0], u'Да' if node[1] else u'Нет'))


if __name__ == '__main__':
    main()
