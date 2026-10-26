# CrossConnectActionType

Action to perform on the Cross Connect. The applicable action types are listed in the allowedActions of the Cross Connect. <br> XC_SIGNATURE_SUBMISSION - resend the quote to the customer email for signature. <br> XC_PROPOSED_DATE_TIME_ACCEPTANCE - accept the date and time proposed by Equinix. <br> XC_PROPOSED_DATE_TIME_REJECTION - reject the date and time proposed by Equinix. The expedite is cancelled and the Cross Connect is scheduled as STANDARD. <br> XC_CANCEL - cancel the Cross Connect before it is provisioned. <br> XC_DEINSTALL - remove a provisioned Cross Connect. Provide the removal schedule, and optionally the services, the notification contacts and the order details, in data. <br> XC_INFORMATION_UPDATE - provide the requested information as a note and an attachment. 

## Enum

* `XC_SIGNATURE_SUBMISSION` (value: `'XC_SIGNATURE_SUBMISSION'`)

* `XC_PROPOSED_DATE_TIME_ACCEPTANCE` (value: `'XC_PROPOSED_DATE_TIME_ACCEPTANCE'`)

* `XC_PROPOSED_DATE_TIME_REJECTION` (value: `'XC_PROPOSED_DATE_TIME_REJECTION'`)

* `XC_CANCEL` (value: `'XC_CANCEL'`)

* `XC_DEINSTALL` (value: `'XC_DEINSTALL'`)

* `XC_INFORMATION_UPDATE` (value: `'XC_INFORMATION_UPDATE'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


