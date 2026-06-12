import requests

def get_obgyn_practices(zip_code, state="NY"):
    # NPPES API v2.1 Endpoint
    url = "https://npiregistry.cms.hhs.gov/api/"
    
    # Payload: Taxonomy 207V00000X is OB/GYN
    params = {
        "version": "2.1",
        "postal_code": zip_code,
        "state": state,
        "taxonomy_description": "Obstetrics & Gynecology",
        "enumeration_type": "NPI-2", # Focus on Organizations, not individuals
        "limit": 20
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        practices = []
        for result in data.get('results', []):
            practices.append({
                "name": result['basic']['organization_name'],
                "address": f"{result['addresses'][0]['address_1']}, {result['addresses'][0]['city']}",
                "npi": result['number']
            })
        return practices
    else:
        return {"error": "API Request failed"}

# Example: Run this for a high-volume ZIP code in Brooklyn (e.g., 11201)
brooklyn_targets = get_obgyn_practices("11201")
print(brooklyn_targets)