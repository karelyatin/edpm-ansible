# Copyright 2019 Red Hat, Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssh_host_keys(host):
    expected = [
        '[10.0.0.1]:2222,[centos.ctlplane.localdomain]:2222,[10.0.1.1]:2222,[centos.internalapi.localdomain]:2222,[centos.localdomain]:2222,[instance*]:2222 ssh-rsa AAAATESTRSA',
        '[10.0.0.1]:2222,[centos.ctlplane.localdomain]:2222,[10.0.1.1]:2222,[centos.internalapi.localdomain]:2222,[centos.localdomain]:2222,[instance*]:2222 ssh-ed25519 AAAATESTED',
        '[10.0.0.1]:2222,[centos.ctlplane.localdomain]:2222,[10.0.1.1]:2222,[centos.internalapi.localdomain]:2222,[centos.localdomain]:2222,[instance*]:2222 ecdsa-sha2-nistp256 AAAATESTECDSA',
    ]

    for line in expected:
        assert line in host.file("/etc/ssh/ssh_known_hosts").content_string
