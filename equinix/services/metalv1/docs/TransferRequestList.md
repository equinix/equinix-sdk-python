# TransferRequestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**transfers** | [**List[TransferRequest]**](TransferRequest.md) |  | [optional] 

## Example

```python
from equinix_metal.models.transfer_request_list import TransferRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRequestList from a JSON string
transfer_request_list_instance = TransferRequestList.from_json(json)
# print the JSON string representation of the object
print(TransferRequestList.to_json())

# convert the object into a dict
transfer_request_list_dict = transfer_request_list_instance.to_dict()
# create an instance of TransferRequestList from a dict
transfer_request_list_form_dict = transfer_request_list.from_dict(transfer_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


