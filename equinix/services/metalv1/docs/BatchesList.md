# BatchesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[Batch]**](Batch.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.batches_list import BatchesList

# TODO update the JSON string below
json = "{}"
# create an instance of BatchesList from a JSON string
batches_list_instance = BatchesList.from_json(json)
# print the JSON string representation of the object
print(BatchesList.to_json())

# convert the object into a dict
batches_list_dict = batches_list_instance.to_dict()
# create an instance of BatchesList from a dict
batches_list_form_dict = batches_list.from_dict(batches_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


