# GatewaySortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**GatewaySortDirection**](GatewaySortDirection.md) |  | [optional] [default to GatewaySortDirection.DESC]
**var_property** | **str** | Possible field names to use on sorting:   * &#x60;/name&#x60; - Gateway name   * &#x60;/uuid&#x60; - Gateway uuid   * &#x60;/state&#x60; - Gateway status   * &#x60;/changeLog/createdDateTime&#x60; - Date and time when change flow starts   * &#x60;/changeLog/updatedDateTime&#x60; - Date and time when change object is updated  | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.gateway_sort_criteria import GatewaySortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of GatewaySortCriteria from a JSON string
gateway_sort_criteria_instance = GatewaySortCriteria.from_json(json)
# print the JSON string representation of the object
print(GatewaySortCriteria.to_json())

# convert the object into a dict
gateway_sort_criteria_dict = gateway_sort_criteria_instance.to_dict()
# create an instance of GatewaySortCriteria from a dict
gateway_sort_criteria_from_dict = GatewaySortCriteria.from_dict(gateway_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


