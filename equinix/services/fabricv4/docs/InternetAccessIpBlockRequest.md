# InternetAccessIpBlockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the IP Block | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_ip_block_request import InternetAccessIpBlockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessIpBlockRequest from a JSON string
internet_access_ip_block_request_instance = InternetAccessIpBlockRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessIpBlockRequest.to_json())

# convert the object into a dict
internet_access_ip_block_request_dict = internet_access_ip_block_request_instance.to_dict()
# create an instance of InternetAccessIpBlockRequest from a dict
internet_access_ip_block_request_from_dict = InternetAccessIpBlockRequest.from_dict(internet_access_ip_block_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


