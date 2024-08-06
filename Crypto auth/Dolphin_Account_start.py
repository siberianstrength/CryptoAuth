import requests
from Google_Acc_Auth import run_chrome


def get_profile_ids(bearer_token: str) -> dict:
    """
    Recieves bearer's token and returns all profile accounts.

    Parameters
    ----------
    bearer_token : str

    Returns
    -------
    json dictionary

    test token :
    bearer_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNzI0MGNiYjRlNmY2OWQyY2I0ZmQzMWU2MTExMTQ0ODRhN2Y3MWFhOGNmZjQ5M2JkN2RlYjFjZjdmNmU2ZDM0MDcyNGQ3YjQwZGYyNjM2YWMiLCJpYXQiOjE3MjIxNjcxMTkuNTU2OTc5LCJuYmYiOjE3MjIxNjcxMTkuNTU2OTgyLCJleHAiOjE3MjQ3NTkxMTkuNTQyMDQ1LCJzdWIiOiIzNTk2NjEyIiwic2NvcGVzIjpbXX0.n8Ms4OBl6F_uvR5MreQgnx96J1Nm8quPb4XdnpC70oJAb8t0_kJltE0kfcelIlu0WJfg-ZjazAWZ9V0oGuXaHXblp6SRegMWl_sCY7a6SI_TRRki4fsMxKRI4gq9dfLz9ot8FEVvb7hs5GFC0r-6Wm6qZXoi8r0ZRJXin7BneNQxQr6nunr8K-C45qmmKcGb2fqQzxAvT8EJa4BVSRwnV1ra9nyea5FJQTqBADLZi2oHFW4uEHWFtqnj4WWMgLTblL0IHXCYIM4n5rh1ZJK8jPkrnm4pD_kVaVOB4Jkzi_WPVEdMtzA4VbViK6xn2AhB3Um3XtxoLovbty1H9EQy1OWR4lz9V0ExDCcZryjZVpXBzfKroaTN__4xPX7baeVoxr8tFQp9tPtd1Gv1MxJWIphIYP5KR9JLwu1uJBwJaE3WztWkPb5LkZga6_uYogGgC7e-Csuwyqs4LKxfeKamInSYQsYdKwRdL5v602B7dKHlnRe8KUgYZr9EJpsT9DJ9uAy7KzaZc9xW6xu6lC8l8S13EZQplnImre13Zicy6lBs1vSkBYhtQlkVSG6cxzIUXlyrpKyNl035RWq0C5_TqLckhe7jH59KpPavmO9EDdPXBjN8qMxnH6RsYHKRhg28-L5CF6Evs2qP7LrjELIit5qshrMNdKTcn9uxaaievB0'
    """
    url = "https://dolphin-anty-api.com/browser_profiles"

    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)
    return response


def start_profile(bearer_token: str) -> None:
    """
    Recieves bearer's token and starts all accounts linked to bearer's profile.

    Parameters
    ----------
    bearer_token : str


    Returns
    -------
    None

    """
    json_profile_ids = get_profile_ids(bearer_token).json()['data']
    ids = [ids['id'] for ids in json_profile_ids]
    request_data = {
        'token': bearer_token}
    
    headers = {
        'Content-Type': 'application/json'}
    
    for profile_id in ids:
        api_url = f'http://localhost:3001/v1.0/browser_profiles/{profile_id}/start?automation=1'
        
        response = requests.post(api_url, json = request_data, headers = headers)
        
        if response.status_code == 200:
            print('succ', response.json())
        else:
            print('error', response.status_code)
        run_chrome(response.json()['automation']['port'], 'tent.txt')
        
if __name__ == '__main__':
    bearer_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNzI0MGNiYjRlNmY2OWQyY2I0ZmQzMWU2MTExMTQ0ODRhN2Y3MWFhOGNmZjQ5M2JkN2RlYjFjZjdmNmU2ZDM0MDcyNGQ3YjQwZGYyNjM2YWMiLCJpYXQiOjE3MjIxNjcxMTkuNTU2OTc5LCJuYmYiOjE3MjIxNjcxMTkuNTU2OTgyLCJleHAiOjE3MjQ3NTkxMTkuNTQyMDQ1LCJzdWIiOiIzNTk2NjEyIiwic2NvcGVzIjpbXX0.n8Ms4OBl6F_uvR5MreQgnx96J1Nm8quPb4XdnpC70oJAb8t0_kJltE0kfcelIlu0WJfg-ZjazAWZ9V0oGuXaHXblp6SRegMWl_sCY7a6SI_TRRki4fsMxKRI4gq9dfLz9ot8FEVvb7hs5GFC0r-6Wm6qZXoi8r0ZRJXin7BneNQxQr6nunr8K-C45qmmKcGb2fqQzxAvT8EJa4BVSRwnV1ra9nyea5FJQTqBADLZi2oHFW4uEHWFtqnj4WWMgLTblL0IHXCYIM4n5rh1ZJK8jPkrnm4pD_kVaVOB4Jkzi_WPVEdMtzA4VbViK6xn2AhB3Um3XtxoLovbty1H9EQy1OWR4lz9V0ExDCcZryjZVpXBzfKroaTN__4xPX7baeVoxr8tFQp9tPtd1Gv1MxJWIphIYP5KR9JLwu1uJBwJaE3WztWkPb5LkZga6_uYogGgC7e-Csuwyqs4LKxfeKamInSYQsYdKwRdL5v602B7dKHlnRe8KUgYZr9EJpsT9DJ9uAy7KzaZc9xW6xu6lC8l8S13EZQplnImre13Zicy6lBs1vSkBYhtQlkVSG6cxzIUXlyrpKyNl035RWq0C5_TqLckhe7jH59KpPavmO9EDdPXBjN8qMxnH6RsYHKRhg28-L5CF6Evs2qP7LrjELIit5qshrMNdKTcn9uxaaievB0'
    start_profile(bearer_token)