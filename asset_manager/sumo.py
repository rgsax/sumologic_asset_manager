import requests

endpoints = {
    'rules': {'q': '`ruleSource:"user"`'},
	'rule-tuning-expressions': {},
	'match-lists': {},
	'custom-insights': {}
}

def verify_asset(asset):
    return asset in endpoints

def _make_endpoint_url(url, asset): 
    return url + ('/' if not url.endswith('/') else '') + asset

def get_assets(instance, asset_type, **params):
    headers = {
        'accept': 'application/json',
        'Authorization': 'Basic ' + instance.key
    }    
    url = _make_endpoint_url(instance.url, asset_type)

    results_limit = 50
    current_offset = 0
    hasNextPage = True

    assets = []
    while hasNextPage:
        params = {
            'offset': current_offset, 
            'limit': results_limit
        }
        params.update(endpoints[asset_type])

        data = requests.get(url, headers=headers, params=params)
        try:
            if data.ok:
                data = data.json()["data"]
                assets.extend(data["objects"])

                if "hasNextPage" in data:
                    hasNextPage = data["hasNextPage"]
                    current_offset += results_limit
                else:
                    hasNextPage = False
            else:
                data = data.json()["errors"]
        except:
            hasNextPage = False

    return assets
