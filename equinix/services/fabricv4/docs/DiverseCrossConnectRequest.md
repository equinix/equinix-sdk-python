# DiverseCrossConnectRequest

Request to create several Cross Connects in a single order. Use it to order a diverse pair - one PRIMARY and one SECONDARY entry provisioned at the same time on separate paths - or to order multiple Cross Connects at once by sending one entry per Cross Connect. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreateCrossConnect]**](CreateCrossConnect.md) | For a diverse pair, send two entries - one with redundancy.priority PRIMARY and one with SECONDARY - and omit redundancy.group, which Equinix assigns.  | 

## Example

```python
from equinix.services.fabricv4.models.diverse_cross_connect_request import DiverseCrossConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiverseCrossConnectRequest from a JSON string
diverse_cross_connect_request_instance = DiverseCrossConnectRequest.from_json(json)
# print the JSON string representation of the object
print(DiverseCrossConnectRequest.to_json())

# convert the object into a dict
diverse_cross_connect_request_dict = diverse_cross_connect_request_instance.to_dict()
# create an instance of DiverseCrossConnectRequest from a dict
diverse_cross_connect_request_from_dict = DiverseCrossConnectRequest.from_dict(diverse_cross_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


