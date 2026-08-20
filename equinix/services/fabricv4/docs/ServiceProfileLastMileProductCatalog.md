# ServiceProfileLastMileProductCatalog

Last-mile provider catalog details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Last-mile provider or catalog name. | [optional] 
**id** | **str** | Last-mile provider or catalog identifier. | [optional] 
**web_url** | **str** | Last-mile catalog or provider website URL. | [optional] 
**delivery_date** | [**ServiceProfileLastMileDeliveryDateRange**](ServiceProfileLastMileDeliveryDateRange.md) |  | [optional] 
**offerings** | [**List[ServiceProfileLastMileOffering]**](ServiceProfileLastMileOffering.md) | Available last-mile offerings. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_last_mile_product_catalog import ServiceProfileLastMileProductCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLastMileProductCatalog from a JSON string
service_profile_last_mile_product_catalog_instance = ServiceProfileLastMileProductCatalog.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLastMileProductCatalog.to_json())

# convert the object into a dict
service_profile_last_mile_product_catalog_dict = service_profile_last_mile_product_catalog_instance.to_dict()
# create an instance of ServiceProfileLastMileProductCatalog from a dict
service_profile_last_mile_product_catalog_from_dict = ServiceProfileLastMileProductCatalog.from_dict(service_profile_last_mile_product_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


