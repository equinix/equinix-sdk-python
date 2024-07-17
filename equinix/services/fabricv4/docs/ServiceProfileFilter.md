# ServiceProfileFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/name&#x60; - Service Profile name  * &#x60;/uuid&#x60; - Service Profile uuid  * &#x60;/state&#x60; - Service Profile status  * &#x60;/metros/code&#x60; - Service Profile metro code  * &#x60;/visibility&#x60; - Service Profile package  * &#x60;/type&#x60; - Service Profile package  * &#x60;/project/projectId&#x60; - Service Profile project id  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_and** | [**List[ServiceProfileSimpleExpression]**](ServiceProfileSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_filter import ServiceProfileFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileFilter from a JSON string
service_profile_filter_instance = ServiceProfileFilter.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileFilter.to_json())

# convert the object into a dict
service_profile_filter_dict = service_profile_filter_instance.to_dict()
# create an instance of ServiceProfileFilter from a dict
service_profile_filter_form_dict = service_profile_filter.from_dict(service_profile_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


