# Chancery
Chancery is a module for creating various represantations of a user.

## Usage
```python
from chancery import Catalog
catalog = Catalog(domain="example.com")
user = catalog.register("Fredrik Brännbacka")
```

The resulting user variable will be a User object with the following properties:
- user.name == "Fredrik Brännbacka"
- user.short_name == "frbr"
- user.ascii_name == "Fredrik Brannbacka"
- user.initials == "fb"
- user.login == "fredrik.brannbacka"
- user.email == "fredrik.brannbacka@example.com"
- user.id == "f800499b-9128-522d-a7f5-b1f3610354e2"

And user.as_json() will result in:

```json
{
  "name": "Fredrik Br\u00e4nnbacka", 
  "short_name": "frbr", 
  "email": "fredrik.brannbacka@example.com", 
  "ascii_name": "Fredrik Brannbacka", 
  "login": "fredrik.brannbacka", 
  "id": "f800499b-9128-522d-a7f5-b1f3610354e2", 
  "initials": "fb"
}
```
