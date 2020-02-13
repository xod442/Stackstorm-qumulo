# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# from qumulo.rest_client import RestClient
import requests
import json
from st2common.runners.base_action import Action

class QumuloBaseAction(Action):
    def __init__(self,config):
        super(QumuloBaseAction, self).__init__(config)
        self.root_url, self.default_header = self._get_login()

    def _get_login(self):
        ipaddress = self.config['ipaddress']
        username = self.config['username']
        password = self.config['password']
        # set root UriBuilder
        root_url = 'https://' + ipaddress + ':8000/'
        login_url = root_url + 'v1/session/login'
        default_header = {'content-type': 'application/json'}
        creds = {'username': username, 'password': password}
        response = requests.post(login_url,
                                  data=json.dumps(creds),
                                  headers=default_header,
                                  verify=False)

        resp_data = json.loads(response.text)
        default_header['Authorization'] = 'Bearer ' + resp_data['bearer_token']

        return (root_url, default_header)
