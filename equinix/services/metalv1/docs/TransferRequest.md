# TransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 
**target_organization** | [**Href**](Href.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from equinix_metal.models.transfer_request import TransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRequest from a JSON string
transfer_request_instance = TransferRequest.from_json(json)
# print the JSON string representation of the object
print(TransferRequest.to_json())

# convert the object into a dict
transfer_request_dict = transfer_request_instance.to_dict()
# create an instance of TransferRequest from a dict
transfer_request_form_dict = transfer_request.from_dict(transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


