# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""
import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictStr
from typing_extensions import Annotated
from equinix.services.fabricv4.models.statistics import Statistics
from equinix.services.fabricv4.models.view_point import ViewPoint

from equinix.services.fabricv4.api_client import ApiClient, RequestSerialized
from equinix.services.fabricv4.api_response import ApiResponse
from equinix.services.fabricv4.rest import RESTResponseType


class StatisticsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_connection_stats_by_port_uuid(
        self,
        connection_id: Annotated[StrictStr, Field(description="Connection UUID")],
        start_date_time: Annotated[datetime, Field(description="startDateTime")],
        end_date_time: Annotated[datetime, Field(description="endDateTime")],
        view_point: Annotated[ViewPoint, Field(description="viewPoint")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Statistics:
        """Get Stats by uuid

        This API provides service-level metrics so that you can view access and gather key information required to manage service subscription sizing and capacity

        :param connection_id: Connection UUID (required)
        :type connection_id: str
        :param start_date_time: startDateTime (required)
        :type start_date_time: datetime
        :param end_date_time: endDateTime (required)
        :type end_date_time: datetime
        :param view_point: viewPoint (required)
        :type view_point: ViewPoint
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_connection_stats_by_port_uuid_serialize(
            connection_id=connection_id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            view_point=view_point,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Statistics",
            '401': "List[Error]",
            '403': "List[Error]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_connection_stats_by_port_uuid_with_http_info(
        self,
        connection_id: Annotated[StrictStr, Field(description="Connection UUID")],
        start_date_time: Annotated[datetime, Field(description="startDateTime")],
        end_date_time: Annotated[datetime, Field(description="endDateTime")],
        view_point: Annotated[ViewPoint, Field(description="viewPoint")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Statistics]:
        """Get Stats by uuid

        This API provides service-level metrics so that you can view access and gather key information required to manage service subscription sizing and capacity

        :param connection_id: Connection UUID (required)
        :type connection_id: str
        :param start_date_time: startDateTime (required)
        :type start_date_time: datetime
        :param end_date_time: endDateTime (required)
        :type end_date_time: datetime
        :param view_point: viewPoint (required)
        :type view_point: ViewPoint
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_connection_stats_by_port_uuid_serialize(
            connection_id=connection_id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            view_point=view_point,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Statistics",
            '401': "List[Error]",
            '403': "List[Error]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_connection_stats_by_port_uuid_without_preload_content(
        self,
        connection_id: Annotated[StrictStr, Field(description="Connection UUID")],
        start_date_time: Annotated[datetime, Field(description="startDateTime")],
        end_date_time: Annotated[datetime, Field(description="endDateTime")],
        view_point: Annotated[ViewPoint, Field(description="viewPoint")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Stats by uuid

        This API provides service-level metrics so that you can view access and gather key information required to manage service subscription sizing and capacity

        :param connection_id: Connection UUID (required)
        :type connection_id: str
        :param start_date_time: startDateTime (required)
        :type start_date_time: datetime
        :param end_date_time: endDateTime (required)
        :type end_date_time: datetime
        :param view_point: viewPoint (required)
        :type view_point: ViewPoint
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_connection_stats_by_port_uuid_serialize(
            connection_id=connection_id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            view_point=view_point,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Statistics",
            '401': "List[Error]",
            '403': "List[Error]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_connection_stats_by_port_uuid_serialize(
        self,
        connection_id,
        start_date_time,
        end_date_time,
        view_point,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if connection_id is not None:
            _path_params['connectionId'] = connection_id
        # process the query parameters
        if start_date_time is not None:
            if isinstance(start_date_time, datetime):
                _query_params.append(
                    (
                        'startDateTime',
                        start_date_time.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('startDateTime', start_date_time))
            
        if end_date_time is not None:
            if isinstance(end_date_time, datetime):
                _query_params.append(
                    (
                        'endDateTime',
                        end_date_time.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('endDateTime', end_date_time))
            
        if view_point is not None:
            
            _query_params.append(('viewPoint', view_point.value))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/fabric/v4/connections/{connectionId}/stats',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_port_stats_by_port_uuid(
        self,
        port_id: Annotated[StrictStr, Field(description="Port UUID")],
        start_date_time: Annotated[datetime, Field(description="startDateTime")],
        end_date_time: Annotated[datetime, Field(description="endDateTime")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Statistics:
        """Get Stats by uuid

        This API provides service-level traffic metrics so that you can view access and gather key information required to manage service subscription sizing and capacity.

        :param port_id: Port UUID (required)
        :type port_id: str
        :param start_date_time: startDateTime (required)
        :type start_date_time: datetime
        :param end_date_time: endDateTime (required)
        :type end_date_time: datetime
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_port_stats_by_port_uuid_serialize(
            port_id=port_id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Statistics",
            '401': "List[Error]",
            '403': "List[Error]",
            '500': "List[Error]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_port_stats_by_port_uuid_with_http_info(
        self,
        port_id: Annotated[StrictStr, Field(description="Port UUID")],
        start_date_time: Annotated[datetime, Field(description="startDateTime")],
        end_date_time: Annotated[datetime, Field(description="endDateTime")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Statistics]:
        """Get Stats by uuid

        This API provides service-level traffic metrics so that you can view access and gather key information required to manage service subscription sizing and capacity.

        :param port_id: Port UUID (required)
        :type port_id: str
        :param start_date_time: startDateTime (required)
        :type start_date_time: datetime
        :param end_date_time: endDateTime (required)
        :type end_date_time: datetime
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_port_stats_by_port_uuid_serialize(
            port_id=port_id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Statistics",
            '401': "List[Error]",
            '403': "List[Error]",
            '500': "List[Error]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_port_stats_by_port_uuid_without_preload_content(
        self,
        port_id: Annotated[StrictStr, Field(description="Port UUID")],
        start_date_time: Annotated[datetime, Field(description="startDateTime")],
        end_date_time: Annotated[datetime, Field(description="endDateTime")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Stats by uuid

        This API provides service-level traffic metrics so that you can view access and gather key information required to manage service subscription sizing and capacity.

        :param port_id: Port UUID (required)
        :type port_id: str
        :param start_date_time: startDateTime (required)
        :type start_date_time: datetime
        :param end_date_time: endDateTime (required)
        :type end_date_time: datetime
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_port_stats_by_port_uuid_serialize(
            port_id=port_id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Statistics",
            '401': "List[Error]",
            '403': "List[Error]",
            '500': "List[Error]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_port_stats_by_port_uuid_serialize(
        self,
        port_id,
        start_date_time,
        end_date_time,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if port_id is not None:
            _path_params['portId'] = port_id
        # process the query parameters
        if start_date_time is not None:
            if isinstance(start_date_time, datetime):
                _query_params.append(
                    (
                        'startDateTime',
                        start_date_time.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('startDateTime', start_date_time))
            
        if end_date_time is not None:
            if isinstance(end_date_time, datetime):
                _query_params.append(
                    (
                        'endDateTime',
                        end_date_time.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('endDateTime', end_date_time))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/fabric/v4/ports/{portId}/stats',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


