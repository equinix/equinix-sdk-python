# LinkAggregationGroup

Link aggregation group (LAG) preferences and settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Parameter showing whether LAG configuration is mandatory. The default is false. | [optional] [default to False]

## Example

```python
from equinix.services.fabricv4.models.link_aggregation_group import LinkAggregationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LinkAggregationGroup from a JSON string
link_aggregation_group_instance = LinkAggregationGroup.from_json(json)
# print the JSON string representation of the object
print(LinkAggregationGroup.to_json())

# convert the object into a dict
link_aggregation_group_dict = link_aggregation_group_instance.to_dict()
# create an instance of LinkAggregationGroup from a dict
link_aggregation_group_form_dict = link_aggregation_group.from_dict(link_aggregation_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


