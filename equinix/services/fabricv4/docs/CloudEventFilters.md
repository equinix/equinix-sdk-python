# CloudEventFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CloudEventSimpleExpression]**](CloudEventSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_event_filters import CloudEventFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CloudEventFilters from a JSON string
cloud_event_filters_instance = CloudEventFilters.from_json(json)
# print the JSON string representation of the object
print(CloudEventFilters.to_json())

# convert the object into a dict
cloud_event_filters_dict = cloud_event_filters_instance.to_dict()
# create an instance of CloudEventFilters from a dict
cloud_event_filters_from_dict = CloudEventFilters.from_dict(cloud_event_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


