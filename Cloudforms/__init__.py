'''DO NOT REMOVE'''
from Cloudforms.API import Client

from Cloudforms.managers.provider import ProviderManager
from Cloudforms.managers.provision_request import ProvisionRequestManager
from Cloudforms.managers.tag import TagManager
from Cloudforms.managers.task import TaskManager
from Cloudforms.managers.vs import VSManager

assert Client
assert ProviderManager
assert ProvisionRequestManager
assert TagManager
assert TaskManager
assert VSManager
