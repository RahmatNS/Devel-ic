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


class PayInsBankwireApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pay_ins_bankwire_bankwire_get_payment(self, pay_in_id, **kwargs):  # noqa: E501
        """pay_ins_bankwire_bankwire_get_payment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pay_ins_bankwire_bankwire_get_payment(pay_in_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pay_in_id: (required)
        :return: PayInBankwireResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pay_ins_bankwire_bankwire_get_payment_with_http_info(pay_in_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pay_ins_bankwire_bankwire_get_payment_with_http_info(pay_in_id, **kwargs)  # noqa: E501
            return data

    def pay_ins_bankwire_bankwire_get_payment_with_http_info(self, pay_in_id, **kwargs):  # noqa: E501
        """pay_ins_bankwire_bankwire_get_payment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pay_ins_bankwire_bankwire_get_payment_with_http_info(pay_in_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pay_in_id: (required)
        :return: PayInBankwireResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pay_in_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pay_ins_bankwire_bankwire_get_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pay_in_id' is set
        if ('pay_in_id' not in params or
                params['pay_in_id'] is None):
            raise ValueError("Missing the required parameter `pay_in_id` when calling `pay_ins_bankwire_bankwire_get_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pay_in_id' in params:
            path_params['PayInId'] = params['pay_in_id']  # noqa: E501

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
            '/v2.1/PayInsBankwire/payments/{PayInId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayInBankwireResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pay_ins_bankwire_bankwire_payment_by_direct(self, **kwargs):  # noqa: E501
        """pay_ins_bankwire_bankwire_payment_by_direct  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pay_ins_bankwire_bankwire_payment_by_direct(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PayInBankwirePost bankwire_pay_in:
        :return: PayInBankwireResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pay_ins_bankwire_bankwire_payment_by_direct_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.pay_ins_bankwire_bankwire_payment_by_direct_with_http_info(**kwargs)  # noqa: E501
            return data

    def pay_ins_bankwire_bankwire_payment_by_direct_with_http_info(self, **kwargs):  # noqa: E501
        """pay_ins_bankwire_bankwire_payment_by_direct  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pay_ins_bankwire_bankwire_payment_by_direct_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PayInBankwirePost bankwire_pay_in:
        :return: PayInBankwireResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bankwire_pay_in']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pay_ins_bankwire_bankwire_payment_by_direct" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bankwire_pay_in' in params:
            body_params = params['bankwire_pay_in']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;odata.metadata=minimal;odata.streaming=true', 'application/json;odata.metadata=minimal;odata.streaming=false', 'application/json;odata.metadata=minimal', 'application/json;odata.metadata=full;odata.streaming=true', 'application/json;odata.metadata=full;odata.streaming=false', 'application/json;odata.metadata=full', 'application/json;odata.metadata=none;odata.streaming=true', 'application/json;odata.metadata=none;odata.streaming=false', 'application/json;odata.metadata=none', 'application/json;odata.streaming=true', 'application/json;odata.streaming=false', 'application/json', 'application/xml', 'application/prs.odatatestxx-odata', 'text/plain', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;odata.metadata=minimal;odata.streaming=true', 'application/json;odata.metadata=minimal;odata.streaming=false', 'application/json;odata.metadata=minimal', 'application/json;odata.metadata=full;odata.streaming=true', 'application/json;odata.metadata=full;odata.streaming=false', 'application/json;odata.metadata=full', 'application/json;odata.metadata=none;odata.streaming=true', 'application/json;odata.metadata=none;odata.streaming=false', 'application/json;odata.metadata=none', 'application/json;odata.streaming=true', 'application/json;odata.streaming=false', 'application/json', 'application/xml', 'application/prs.odatatestxx-odata', 'application/json;odata.metadata=minimal;odata.streaming=true', 'application/json;odata.metadata=minimal;odata.streaming=false', 'application/json;odata.metadata=minimal', 'application/json;odata.metadata=full;odata.streaming=true', 'application/json;odata.metadata=full;odata.streaming=false', 'application/json;odata.metadata=full', 'application/json;odata.metadata=none;odata.streaming=true', 'application/json;odata.metadata=none;odata.streaming=false', 'application/json;odata.metadata=none', 'application/json;odata.streaming=true', 'application/json;odata.streaming=false', 'application/json', 'application/xml', 'application/prs.odatatestxx-odata', 'application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/PayInsBankwire/payments/direct', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayInBankwireResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pay_ins_bankwire_bankwire_post_refund(self, pay_in_id, **kwargs):  # noqa: E501
        """pay_ins_bankwire_bankwire_post_refund  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pay_ins_bankwire_bankwire_post_refund(pay_in_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pay_in_id: (required)
        :param PayInBankwireRefundPost bankwire_refund:
        :return: PayInBankwireRefundResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pay_ins_bankwire_bankwire_post_refund_with_http_info(pay_in_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pay_ins_bankwire_bankwire_post_refund_with_http_info(pay_in_id, **kwargs)  # noqa: E501
            return data

    def pay_ins_bankwire_bankwire_post_refund_with_http_info(self, pay_in_id, **kwargs):  # noqa: E501
        """pay_ins_bankwire_bankwire_post_refund  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pay_ins_bankwire_bankwire_post_refund_with_http_info(pay_in_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int pay_in_id: (required)
        :param PayInBankwireRefundPost bankwire_refund:
        :return: PayInBankwireRefundResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pay_in_id', 'bankwire_refund']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pay_ins_bankwire_bankwire_post_refund" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pay_in_id' is set
        if ('pay_in_id' not in params or
                params['pay_in_id'] is None):
            raise ValueError("Missing the required parameter `pay_in_id` when calling `pay_ins_bankwire_bankwire_post_refund`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pay_in_id' in params:
            path_params['PayInId'] = params['pay_in_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bankwire_refund' in params:
            body_params = params['bankwire_refund']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;odata.metadata=minimal;odata.streaming=true', 'application/json;odata.metadata=minimal;odata.streaming=false', 'application/json;odata.metadata=minimal', 'application/json;odata.metadata=full;odata.streaming=true', 'application/json;odata.metadata=full;odata.streaming=false', 'application/json;odata.metadata=full', 'application/json;odata.metadata=none;odata.streaming=true', 'application/json;odata.metadata=none;odata.streaming=false', 'application/json;odata.metadata=none', 'application/json;odata.streaming=true', 'application/json;odata.streaming=false', 'application/json', 'application/xml', 'application/prs.odatatestxx-odata', 'text/plain', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;odata.metadata=minimal;odata.streaming=true', 'application/json;odata.metadata=minimal;odata.streaming=false', 'application/json;odata.metadata=minimal', 'application/json;odata.metadata=full;odata.streaming=true', 'application/json;odata.metadata=full;odata.streaming=false', 'application/json;odata.metadata=full', 'application/json;odata.metadata=none;odata.streaming=true', 'application/json;odata.metadata=none;odata.streaming=false', 'application/json;odata.metadata=none', 'application/json;odata.streaming=true', 'application/json;odata.streaming=false', 'application/json', 'application/xml', 'application/prs.odatatestxx-odata', 'application/json;odata.metadata=minimal;odata.streaming=true', 'application/json;odata.metadata=minimal;odata.streaming=false', 'application/json;odata.metadata=minimal', 'application/json;odata.metadata=full;odata.streaming=true', 'application/json;odata.metadata=full;odata.streaming=false', 'application/json;odata.metadata=full', 'application/json;odata.metadata=none;odata.streaming=true', 'application/json;odata.metadata=none;odata.streaming=false', 'application/json;odata.metadata=none', 'application/json;odata.streaming=true', 'application/json;odata.streaming=false', 'application/json', 'application/xml', 'application/prs.odatatestxx-odata', 'application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v2.1/PayInsBankwire/payments/{PayInId}/refunds', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayInBankwireRefundResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)