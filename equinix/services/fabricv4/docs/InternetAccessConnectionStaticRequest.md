# InternetAccessConnectionStaticRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the connection | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_connection_static_request import InternetAccessConnectionStaticRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessConnectionStaticRequest from a JSON string
internet_access_connection_static_request_instance = InternetAccessConnectionStaticRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessConnectionStaticRequest.to_json())

# convert the object into a dict
internet_access_connection_static_request_dict = internet_access_connection_static_request_instance.to_dict()
# create an instance of InternetAccessConnectionStaticRequest from a dict
internet_access_connection_static_request_from_dict = InternetAccessConnectionStaticRequest.from_dict(internet_access_connection_static_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


