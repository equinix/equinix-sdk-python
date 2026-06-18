# InternetAccessLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metro_href** | **str** | Metro URL path for the linked resource | 
**metro_code** | **str** | Code representing the metro | 
**region** | [**InternetAccessLocationRegion**](InternetAccessLocationRegion.md) |  | 
**ibx** | **str** | IBX data center code | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_location import InternetAccessLocation

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessLocation from a JSON string
internet_access_location_instance = InternetAccessLocation.from_json(json)
# print the JSON string representation of the object
print(InternetAccessLocation.to_json())

# convert the object into a dict
internet_access_location_dict = internet_access_location_instance.to_dict()
# create an instance of InternetAccessLocation from a dict
internet_access_location_from_dict = InternetAccessLocation.from_dict(internet_access_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


