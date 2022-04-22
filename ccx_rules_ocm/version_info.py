"""
Get the cluster version.
======================================================

Trigger conditions:
    - always

* Author     : Juan Díaz <jdiazsua@redhat.com>
* JIRA card  : https://issues.redhat.com/browse/CCXDEV-6957
"""
from ccx_ocp_core.models import Version
from insights.core.plugins import make_info
from insights.core.plugins import rule


INFO_KEY = "CLUSTER_VERSION_INFO"

LINKS = {}

CONTENT = """
Cluster Version: {{version}}

""".strip()


@rule(Version, links=LINKS)
def report(version):
    return make_info(INFO_KEY, version=version.current)
