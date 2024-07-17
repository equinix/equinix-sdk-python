# Direction

Directional statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **float** | Max bandwidth within request time range, represented in units specified by response \&quot;units\&quot; field | [optional] 
**mean** | **float** | Mean bandwidth within request time range, represented in units specified by response \&quot;units\&quot; field | [optional] 
**metrics** | [**List[Metrics]**](Metrics.md) | Bandwidth utilization statistics for a specified interval. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.direction import Direction

# TODO update the JSON string below
json = "{}"
# create an instance of Direction from a JSON string
direction_instance = Direction.from_json(json)
# print the JSON string representation of the object
print(Direction.to_json())

# convert the object into a dict
direction_dict = direction_instance.to_dict()
# create an instance of Direction from a dict
direction_form_dict = direction.from_dict(direction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


