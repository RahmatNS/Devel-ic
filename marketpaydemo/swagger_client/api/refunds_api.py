# coding: utf-8

"""
    MarketPay API

    API for Smart Contracts and Payments  # noqa: E501

    OpenAPI spec version: v2.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class RefundsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def refunds_refund_get(self, refund_id, **kwargs):  # noqa: E501
        """refunds_refund_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refunds_refund_get(refund_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int refund_id: (required)
        :return: WebPayRefundResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refunds_refund_get_with_http_info(refund_id, **kwargs)  # noqa: E501
        else:
            (data) = self.refunds_refund_get_with_http_info(refund_id, **kwargs)  # noqa: E501
            return data

    def refunds_refund_get_with_http_info(self, refund_id, **kwargs):  # noqa: E501
        """refunds_refund_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refunds_refund_get_with_http_info(refund_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int refund_id: (required)
        :return: WebPayRefundResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refund_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refunds_refund_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'refund_id' is set
        if ('refund_id' not in params or
                params['refund_id'] is None):
            raise ValueError("Missing the required parameter `refund_id` when calling `refunds_refund_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'refund_id' in params:
            path_params['RefundId'] = params['refund_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;odata.metadata=minimal;odata.streaming=true', 'application/json;odata.metadata=minimal;odata.streaming=false', 'application/json;odata.metadata=minimal', 'application/json;odata.metadata=full;odata.streaming=true', 'application/json;odata.metadata=full;odata.streaming=false', 'application/json;odata.metadata=full', 'application/json;odata.metadata=none;odata.streaming=true', 'application/json;odata.metadata=none;odata.streaming=false', 'application/json;odata.metadata=none', 'application/json;odata.streaming=true', 'application/json;odata.streaming=false', 'application/json', 'application/xml', 'application/prs.odatatestxx-odata', 'text/plain', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/Refunds/{RefundId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebPayRefundResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)