# TransferRequestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**target_organization_id** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.transfer_request_input import TransferRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRequestInput from a JSON string
transfer_request_input_instance = TransferRequestInput.from_json(json)
# print the JSON string representation of the object
print(TransferRequestInput.to_json())

# convert the object into a dict
transfer_request_input_dict = transfer_request_input_instance.to_dict()
# create an instance of TransferRequestInput from a dict
transfer_request_input_form_dict = transfer_request_input.from_dict(transfer_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


