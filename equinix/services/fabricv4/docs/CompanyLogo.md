# CompanyLogo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**extension_type** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_logo import CompanyLogo

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyLogo from a JSON string
company_logo_instance = CompanyLogo.from_json(json)
# print the JSON string representation of the object
print(CompanyLogo.to_json())

# convert the object into a dict
company_logo_dict = company_logo_instance.to_dict()
# create an instance of CompanyLogo from a dict
company_logo_from_dict = CompanyLogo.from_dict(company_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


