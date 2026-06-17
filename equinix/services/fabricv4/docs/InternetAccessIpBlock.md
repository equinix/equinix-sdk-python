# InternetAccessIpBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URI of the IP block | 
**uuid** | **str** | Unique identifier for the IP block | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_ip_block import InternetAccessIpBlock

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessIpBlock from a JSON string
internet_access_ip_block_instance = InternetAccessIpBlock.from_json(json)
# print the JSON string representation of the object
print(InternetAccessIpBlock.to_json())

# convert the object into a dict
internet_access_ip_block_dict = internet_access_ip_block_instance.to_dict()
# create an instance of InternetAccessIpBlock from a dict
internet_access_ip_block_from_dict = InternetAccessIpBlock.from_dict(internet_access_ip_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


