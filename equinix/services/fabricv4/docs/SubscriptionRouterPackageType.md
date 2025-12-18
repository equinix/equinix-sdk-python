# SubscriptionRouterPackageType

Cloud Router Package Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Cloud Router package code | [optional] 

## Example

```python
from equinix.services.fabricv4.models.subscription_router_package_type import SubscriptionRouterPackageType

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRouterPackageType from a JSON string
subscription_router_package_type_instance = SubscriptionRouterPackageType.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRouterPackageType.to_json())

# convert the object into a dict
subscription_router_package_type_dict = subscription_router_package_type_instance.to_dict()
# create an instance of SubscriptionRouterPackageType from a dict
subscription_router_package_type_from_dict = SubscriptionRouterPackageType.from_dict(subscription_router_package_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


