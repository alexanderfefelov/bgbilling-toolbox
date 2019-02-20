#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import logging


# Требования к формату выгрузки данных о типах документов, удостоверяющих личность абонентов
# 1.1 (01.12.2016 12:48)
#
def export_DocTypes(config, connection):
    task_name = 'DocTypes'
    __export(task_name, config, connection)


# Требования к формату выгрузки данных по абонентам
# 3.4 (07.09.2017 19:49)
#
def export_Abonents(config, connection):
    task_name = 'Abonents'
    __export(task_name, config, connection)


# Требования к формату выгрузки данных по платежам абонентов
# 1.7 (19.09.2017 20:21)
#
def export_payments(config, connection):
    task_name = 'payments'
    __export(task_name, config, connection)


# Требования к формату выгрузки данных по точкам доступа WiFi
# 1.0 (01.09.2017 15:10)
#
def export_BaseStations(config, connection):
    task_name = 'BaseStations'
    __export(task_name, config, connection)


# Требования к формату выгрузки данных с планами IP-нумерации сети
# 1.1 (01.12.2016 13:13)
#
def export_IpNumberingPlan(config, connection):
    task_name = 'IpNumberingPlan'
    __export(task_name, config, connection)


# Требования к формату выгрузки идентификаторов точек подключения к сети передачи данных
# 1.1 (01.12.2016 11:58)
#
def export_IpDataPoints(config, connection):
    task_name = 'IpDataPoints'
    __export(task_name, config, connection)


# Требования к формату выгрузки справочника IP-шлюзов, с которых получены записи о соединениях абонентов
# 1.0 (04.09.2017 13:39)
#
def export_GatesRecords(config, connection):
    task_name = 'GatesRecords'
    __export(task_name, config, connection)


# Требования к формату выгрузки справочника способов оплаты
# 1.0 (04.09.2017 13:54)
#
def export_PayTypesRecords(config, connection):
    task_name = 'PayTypesRecords'
    __export(task_name, config, connection)


def __setup_encoding():
    import sys

    reload(sys)
    sys.setdefaultencoding('cp1251')


def __get_query(config, task_name):
    query = config.get('application', 'sql_%s' % task_name)
    return query


def __execute_query(connection, query):
    logging.debug('Executing SQL: %s', query)
    proxy = connection.execute(query)
    result = proxy.fetchall()
    logging.debug('%d row(s) found', len(result))
    return result


def __write_file(file_name, data):
    import csv

    with open(file_name, 'wb') as f:
        for record in data:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(record)


def __export(task_name, config, connection):
    logging.info('Processing %s', task_name)
    query = __get_query(config, task_name).strip()
    if len(query) > 0:
        data = __execute_query(connection, query)
        __write_file('%s.csv' % task_name, data)
    else:
        logging.info('%s not implemented', task_name)
    logging.info('%s done', task_name)


def main():
    import ConfigParser
    import logging.config
    from sqlalchemy import create_engine

    __setup_encoding()

    logging.config.fileConfig('logging.conf')

    config = ConfigParser.RawConfigParser()
    config.read('application.conf')

    database_connection_string = config.get('application', 'database_connection_string')
    engine = create_engine(database_connection_string)
    connection = engine.connect()

    export_DocTypes(config, connection)
    export_Abonents(config, connection)
    export_payments(config, connection)
    export_BaseStations(config, connection)
    export_IpNumberingPlan(config, connection)
    export_IpDataPoints(config, connection)
    export_GatesRecords(config, connection)
    export_PayTypesRecords(config, connection)

    connection.close()
    engine.dispose()


if __name__ == '__main__':
    main()
