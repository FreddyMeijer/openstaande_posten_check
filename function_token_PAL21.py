def token():
    import requests
    import pandas as pd
    import json
    import math
    import config

    url = config.url

    queryBearer = '''
    mutation login {
    login(
        authProfileUuid: "''' + config.authProfileUuid + '''"
        username: "''' + config.username + '''"
        password: "''' + config.password + '''"
    ) {
        jwtToken
        refreshToken
    }
    }
    '''
    response = requests.post(url, json={'query': queryBearer})
    responseParsed = json.loads(response.text)
    bearer = 'Bearer ' + responseParsed['data']['login']['jwtToken']
    headers = {'Authorization': bearer}
    return headers

