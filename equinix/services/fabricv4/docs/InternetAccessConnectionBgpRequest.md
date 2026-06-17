# InternetAccessConnectionBgpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the connection | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_connection_bgp_request import InternetAccessConnectionBgpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessConnectionBgpRequest from a JSON string
internet_access_connection_bgp_request_instance = InternetAccessConnectionBgpRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessConnectionBgpRequest.to_json())

# convert the object into a dict
internet_access_connection_bgp_request_dict = internet_access_connection_bgp_request_instance.to_dict()
# create an instance of InternetAccessConnectionBgpRequest from a dict
internet_access_connection_bgp_request_from_dict = InternetAccessConnectionBgpRequest.from_dict(internet_access_connection_bgp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


