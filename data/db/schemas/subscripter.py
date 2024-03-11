### SCHEMA SUBSCRIPTERS ###

def subscripter_schema(subscripter) -> dict:
    return {
        'id': str(subscripter['_id']),
        'email': subscripter['email'],
        'activated': subscripter['activated'],
        'date_activated': subscripter['date_activated'],
        'cancelated': subscripter['cancelated'],
        'date_cancelated': subscripter['date_cancelated']
    }
    
def subscripters_schema_list(subscripters) -> list:
    return [subscripter_schema(subscripter) for subscripter in subscripters]
