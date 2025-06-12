# Md5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Md5Type**](Md5Type.md) |  | [optional] 
**key_number** | **int** | The authentication Key ID. | [optional] 
**key** | **bytearray** | The plaintext authentication key. Must be Base64 encoded. For ASCII type, the key must contain printable ASCII characters, range 10-20 characters. For HEX type, range should be 10-40 characters. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.md5 import Md5

# TODO update the JSON string below
json = "{}"
# create an instance of Md5 from a JSON string
md5_instance = Md5.from_json(json)
# print the JSON string representation of the object
print(Md5.to_json())

# convert the object into a dict
md5_dict = md5_instance.to_dict()
# create an instance of Md5 from a dict
md5_from_dict = Md5.from_dict(md5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


