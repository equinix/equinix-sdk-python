# LoaReplaceOperation

Replace attribute value or sub-resource in the existing model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**LoaOpEnum**](LoaOpEnum.md) |  | 
**path** | **str** | ### A JSON Pointer path.   * &#x60;/name&#x60; - Name of the Loa   * &#x60;/description&#x60; - Description of the Loa   * &#x60;/requestor/email&#x60; - Email of the requestor contact   * &#x60;/requestor/orgName&#x60; - Organization name of the requestor   * &#x60;/issuer/email&#x60; - Email of the issuer contact   * &#x60;/issuer/orgName&#x60; - Organization name of the issuer   * &#x60;/demarcationPoint/patchPanelId&#x60; - Patch Panel Identifier   * &#x60;/demarcationPoint/patchPanelPortA&#x60; - Patch Panel Port A   * &#x60;/demarcationPoint/patchPanelPortB&#x60; - Patch Panel Port B   * &#x60;/demarcationPoint/connectorType&#x60; - Connector Type   * &#x60;/demarcationPoint/cageUniqueSpaceId&#x60; - Cage Unique Space Identifier   * &#x60;/expirationDateTime&#x60; - Expiration date and time of the Loa   * &#x60;/location/ibxCode&#x60; - IBX code of the Eligible location  | 
**value** | **object** | New value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.loa_replace_operation import LoaReplaceOperation

# TODO update the JSON string below
json = "{}"
# create an instance of LoaReplaceOperation from a JSON string
loa_replace_operation_instance = LoaReplaceOperation.from_json(json)
# print the JSON string representation of the object
print(LoaReplaceOperation.to_json())

# convert the object into a dict
loa_replace_operation_dict = loa_replace_operation_instance.to_dict()
# create an instance of LoaReplaceOperation from a dict
loa_replace_operation_from_dict = LoaReplaceOperation.from_dict(loa_replace_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


