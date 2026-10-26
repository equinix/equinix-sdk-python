# ExchangeServiceAdditionalInfo

Additional information regarding the specified Exchange Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Error code shown if an operation on the Exchange Service fails | [optional] 
**error_message** | **str** | Generic message shown if an operation on the Exchange Service fails | [optional] 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_additional_info import ExchangeServiceAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceAdditionalInfo from a JSON string
exchange_service_additional_info_instance = ExchangeServiceAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceAdditionalInfo.to_json())

# convert the object into a dict
exchange_service_additional_info_dict = exchange_service_additional_info_instance.to_dict()
# create an instance of ExchangeServiceAdditionalInfo from a dict
exchange_service_additional_info_from_dict = ExchangeServiceAdditionalInfo.from_dict(exchange_service_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


