# CompanyMetro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**metro_code** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_metro import CompanyMetro

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyMetro from a JSON string
company_metro_instance = CompanyMetro.from_json(json)
# print the JSON string representation of the object
print(CompanyMetro.to_json())

# convert the object into a dict
company_metro_dict = company_metro_instance.to_dict()
# create an instance of CompanyMetro from a dict
company_metro_from_dict = CompanyMetro.from_dict(company_metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


