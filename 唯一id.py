#coding=utf-8

import uuid

name = 'weiyi_id'
namespace = uuid.NAMESPACE_URL

print(uuid.uuid1())
print(uuid.uuid3(namespace,name))
print(uuid.uuid4())
print(uuid.uuid5(namespace,name))