# BulkOpticalConnectRequest

Request to create a dual diverse pair of Optical Connect connections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OpticalConnectPostRequest]**](OpticalConnectPostRequest.md) | The two connections forming the diverse pair — one PRIMARY and one             SECONDARY.  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bulk_optical_connect_request import BulkOpticalConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOpticalConnectRequest from a JSON string
bulk_optical_connect_request_instance = BulkOpticalConnectRequest.from_json(json)
# print the JSON string representation of the object
print(BulkOpticalConnectRequest.to_json())

# convert the object into a dict
bulk_optical_connect_request_dict = bulk_optical_connect_request_instance.to_dict()
# create an instance of BulkOpticalConnectRequest from a dict
bulk_optical_connect_request_from_dict = BulkOpticalConnectRequest.from_dict(bulk_optical_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


