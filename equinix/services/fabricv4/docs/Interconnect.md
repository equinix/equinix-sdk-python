# Interconnect

Interconnect specification <font color=\"red\"> <sup color='red'>Beta</sup></font>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Interconnect URI | [optional] 
**uuid** | **str** | Equinix-assigned interconnect identifier | [optional] 
**type** | [**InterconnectPostRequestType**](InterconnectPostRequestType.md) |  | [optional] 
**name** | **str** | Interconnect name | [optional] 
**description** | **str** | Interconnect description | [optional] 
**state** | [**InterconnectState**](InterconnectState.md) |  | [optional] 
**location** | [**InterconnectLocation**](InterconnectLocation.md) |  | [optional] 
**used_bandwidth** | **int** | Interconnect used bandwidth in Mbps | [optional] 
**package** | [**InterconnectPackage**](InterconnectPackage.md) |  | [optional] 
**router** | [**InterconnectRouter**](InterconnectRouter.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**notifications** | [**List[InterconnectNotification]**](InterconnectNotification.md) | Interconnect notification preferences | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interconnect import Interconnect

# TODO update the JSON string below
json = "{}"
# create an instance of Interconnect from a JSON string
interconnect_instance = Interconnect.from_json(json)
# print the JSON string representation of the object
print(Interconnect.to_json())

# convert the object into a dict
interconnect_dict = interconnect_instance.to_dict()
# create an instance of Interconnect from a dict
interconnect_from_dict = Interconnect.from_dict(interconnect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


