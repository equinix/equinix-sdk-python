# InternetAccessPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InternetAccessServiceType**](InternetAccessServiceType.md) |  | 
**name** | **str** | The name of the EIA Service | 
**bandwidth** | **int** | Bandwidth of the service | [optional] 
**bandwidth_commit** | **int** | Minimum bandwidth commit for burst billing variant of the service | [optional] 
**routing_protocol** | [**InternetAccessRoutingProtocolRequest**](InternetAccessRoutingProtocolRequest.md) |  | 
**order** | [**InternetAccessOrderRequest**](InternetAccessOrderRequest.md) |  | [optional] 
**billing** | [**InternetAccessPostRequestBilling**](InternetAccessPostRequestBilling.md) |  | 
**project** | [**Project**](Project.md) |  | 
**account** | [**InternetAccessAccount**](InternetAccessAccount.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_post_request import InternetAccessPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessPostRequest from a JSON string
internet_access_post_request_instance = InternetAccessPostRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessPostRequest.to_json())

# convert the object into a dict
internet_access_post_request_dict = internet_access_post_request_instance.to_dict()
# create an instance of InternetAccessPostRequest from a dict
internet_access_post_request_from_dict = InternetAccessPostRequest.from_dict(internet_access_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


