# Batch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**devices** | [**List[Href]**](Href.md) |  | [optional] 
**error_messages** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 
**quantity** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from equinix_metal.models.batch import Batch

# TODO update the JSON string below
json = "{}"
# create an instance of Batch from a JSON string
batch_instance = Batch.from_json(json)
# print the JSON string representation of the object
print(Batch.to_json())

# convert the object into a dict
batch_dict = batch_instance.to_dict()
# create an instance of Batch from a dict
batch_form_dict = batch.from_dict(batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


