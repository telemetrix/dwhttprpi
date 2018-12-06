from TR50 import TR50http

dw_config = {
        'endpoint': 'http://api-de.devicewise.com/api',
        'app_id': '0000001', # it has to be locked ID value for each logic device. (generating from serial numbers?)
        'app_token': 'hzFldHm60s4vaYzW',
        'thing_key': 'wmbus169_concentrator_01'
    }

tr50http = TR50http.TR50http(dw_config)
