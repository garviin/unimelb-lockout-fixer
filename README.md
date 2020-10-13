# Unimelb Wifi Lockout Fixer

Python script to clear a classic wifi lockout at Unimelb. 

## Dependencies
- Firefox ver. 46 and newer
- Selenium
- Cisco Anyconnect (ver. 4.x and above)


## Usage
1. Clone this repo.
2. Create an 'env.json' file in the root directory, fill out this json object with the relevant details:
```
{
    "USERNAME":"USERNAME",
    "PASSWORD":"PASSWORD",
    "SITE_LINK": "link_to_identity_services_engine_portal",
    "VPN_HOST": "site_host_address"
}
```
3. Run:
```
python3 fixer.py
```
