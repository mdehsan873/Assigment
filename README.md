# Assignment

This is basic api i have created using django.

## Installation

- First install requirements.txt before using it
- pip install -r requirements.txt

## Paths

- get/superuser/token/ for getting super admin access and refresh token take email and password as argument
- token/verify/ for verify the access token
- // Note all this following end points take jwt token for access
- company/create/ for creating company its will take uuid ,name,ceo_name and address
- team/create/<companyID>/  for creating team takes companyID ,uuid , lead_name
- get/all/team/ its return array of teams 
- company/search/ this path for searching company by its name or uid

