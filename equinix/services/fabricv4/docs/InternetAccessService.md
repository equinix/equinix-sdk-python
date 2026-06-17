# InternetAccessService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Service URL path | 
**type** | [**InternetAccessServiceType**](InternetAccessServiceType.md) |  | 
**uuid** | **str** | Unique identifier for the EIA Service | 
**name** | **str** | The name of the EIA Service | 
**bandwidth** | **int** | Bandwidth of the service | [optional] 
**bandwidth_commit** | **int** | Minimum bandwidth commit for burst billing variant of the service | [optional] 
**state** | [**InternetAccessServiceState**](InternetAccessServiceState.md) |  | 
**change** | [**InternetAccessChange**](InternetAccessChange.md) |  | 
**locations** | [**List[InternetAccessLocation]**](InternetAccessLocation.md) | List of locations associated with the service | [optional] 
**routing_protocol** | [**InternetAccessRoutingProtocol**](InternetAccessRoutingProtocol.md) |  | 
**billing** | [**InternetAccessBilling**](InternetAccessBilling.md) |  | 
**account** | [**InternetAccessAccount**](InternetAccessAccount.md) |  | 
**project** | [**Project**](Project.md) |  | 
**order** | [**InternetAccessOrder**](InternetAccessOrder.md) |  | 
**change_log** | [**Changelog**](Changelog.md) |  | 
**use_case** | [**InternetAccessUseCase**](InternetAccessUseCase.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_service import InternetAccessService

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessService from a JSON string
internet_access_service_instance = InternetAccessService.from_json(json)
# print the JSON string representation of the object
print(InternetAccessService.to_json())

# convert the object into a dict
internet_access_service_dict = internet_access_service_instance.to_dict()
# create an instance of InternetAccessService from a dict
internet_access_service_from_dict = InternetAccessService.from_dict(internet_access_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


