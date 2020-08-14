#!/usr/bin/env python
# coding: utf-8

'''
This is a friendly human-readable-easy to understand
curated list of functions created from the official Python UUID library.
The functions naming convention is carefully chosen
to reflect simple English while still fully describe what the
function does.
 '''
import uuid

# 1: make a UUID based on the host ID and current time
def create_uuid_based_on_my_host_and_current_time():
    return uuid.uuid1()


# 2: make a UUID using an MD5 hash of a namespace UUID and a name. Given same URL, it will always return same UUID
def create_uuid_based_on_url_and_md5(url):
    return uuid.uuid3(uuid.NAMESPACE_URL, url)

# 3. make a random UUID.
def create_random_uuid():
    return uuid.uuid4()


# 4: make a UUID from a string of hex digits (braces and hyphens ignored)
def create_uuid_from_hex_digits_string(hex_digits_string):
    return uuid.UUID(hex_digits_string)


# 5: make a UUID from a 16-byte string. Must be 16 bytes long
def create_uuid_from_16_byte_string(_16_byte_string):
    _16_byte_string=_16_byte_string.encode()
    return uuid.UUID(bytes=_16_byte_string)

# Examples:
print('Example 1: ', create_uuid_based_on_my_host_and_current_time())
print('Example 2: ', create_uuid_based_on_url_and_md5('google.com'))
print('Example 3: ', create_random_uuid())
print('Example 4: ', create_uuid_from_hex_digits_string('{00010203-0405-0607-0809-0a0b0c0d0e0f}'))
print('Example 5: ', create_uuid_from_16_byte_string('123456789abcdefg'))
