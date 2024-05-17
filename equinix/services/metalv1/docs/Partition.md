# Partition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**size** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.partition import Partition

# TODO update the JSON string below
json = "{}"
# create an instance of Partition from a JSON string
partition_instance = Partition.from_json(json)
# print the JSON string representation of the object
print(Partition.to_json())

# convert the object into a dict
partition_dict = partition_instance.to_dict()
# create an instance of Partition from a dict
partition_form_dict = partition.from_dict(partition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


