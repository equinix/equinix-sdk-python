# SearchSimpleExpressionOperator

\"~*\" is a case-insensitive glob match, equivalent to ILIKE - the same single \"*\" wildcard, not POSIX regex - kept as its own operator only because existing callers already send it. 

## Enum

* `EQUAL` (value: `'='`)

* `EXCLAMATION_EQUAL` (value: `'!='`)

* `IN` (value: `'IN'`)

* `NOT_IN` (value: `'NOT IN'`)

* `LIKE` (value: `'LIKE'`)

* `ILIKE` (value: `'ILIKE'`)

* `BETWEEN` (value: `'BETWEEN'`)

* `GREATER_THAN` (value: `'>'`)

* `GREATER_THAN_EQUAL` (value: `'>='`)

* `LESS_THAN` (value: `'<'`)

* `LESS_THAN_EQUAL` (value: `'<='`)

* `TILDE_STAR` (value: `'~*'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


