# InstancesBatchCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[InstancesBatchCreateInputBatchesInner]**](InstancesBatchCreateInputBatchesInner.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.instances_batch_create_input import InstancesBatchCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesBatchCreateInput from a JSON string
instances_batch_create_input_instance = InstancesBatchCreateInput.from_json(json)
# print the JSON string representation of the object
print(InstancesBatchCreateInput.to_json())

# convert the object into a dict
instances_batch_create_input_dict = instances_batch_create_input_instance.to_dict()
# create an instance of InstancesBatchCreateInput from a dict
instances_batch_create_input_form_dict = instances_batch_create_input.from_dict(instances_batch_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


