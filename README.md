# Django-Test

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt

```bash
pip install -r requirements.txt
```
## Setup Database

Change DATABASES on [setting.py](https://github.com/Nacho7S/Django-Test/blob/main/apps/apps/settings.py)
or 
Change .env.example which has been given

## Setup(migrate and seeding)
Migrate
```bash
py manage.py migrate
```
Seeding
```bash
py manage.py seedJson
```
https://github.com/Nacho7S/Django-Test/assets/105483135/5ef9b0ca-6b80-4e31-a1e3-1b3ec68032b4

## CRUD Implemantation
product list endpoint
```bash
http://127.0.0.1:8000/product/
```
create product form endpoint
```bash
http://127.0.0.1:8000/product/add-product/
```
edit product form endpoint
```bash
http://127.0.0.1:8000/product/edit-product/<int:id_product>/
```
https://github.com/Nacho7S/Django-Test/assets/105483135/e1a0ae22-02ca-4d17-840d-fa8a01da1aec
