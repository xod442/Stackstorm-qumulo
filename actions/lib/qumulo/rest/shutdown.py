# Copyright (c) 2012 Qumulo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import qumulo.lib.request as request

@request.request
def halt(conninfo, credentials):
    method = "POST"
    uri = "/v1/node/halt"

    return request.rest_request(conninfo, credentials, method, uri)

@request.request
def restart(conninfo, credentials):
    method = "POST"
    uri = "/v1/node/reboot"

    return request.rest_request(conninfo, credentials, method, uri)

@request.request
def halt_cluster(conninfo, credentials):
    method = "POST"
    uri = "/v1/cluster/halt"

    return request.rest_request(conninfo, credentials, method, uri)

@request.request
def restart_cluster(conninfo, credentials):
    method = "POST"
    uri = "/v1/cluster/reboot"

    return request.rest_request(conninfo, credentials, method, uri)
