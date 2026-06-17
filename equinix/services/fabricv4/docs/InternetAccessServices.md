# InternetAccessServices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**sort** | [**List[SearchSortItem]**](SearchSortItem.md) |  | 
**data** | [**List[InternetAccessService]**](InternetAccessService.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_services import InternetAccessServices

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessServices from a JSON string
internet_access_services_instance = InternetAccessServices.from_json(json)
# print the JSON string representation of the object
print(InternetAccessServices.to_json())

# convert the object into a dict
internet_access_services_dict = internet_access_services_instance.to_dict()
# create an instance of InternetAccessServices from a dict
internet_access_services_from_dict = InternetAccessServices.from_dict(internet_access_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


