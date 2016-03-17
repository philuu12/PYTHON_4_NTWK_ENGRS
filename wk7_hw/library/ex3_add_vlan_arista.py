#!/usr/bin/env python
# Symbolically linked to this real file: /home/pluu/ANSIBLE/library/ex3_add_vlan_arista.py
import pyeapi
from ansible.module_utils.basic import *

def check_vlan_exists(eapi_conn, vlan_id):
    '''
    Check if the given VLAN exists
    Return either vlan_name or False
    '''
    vlan_id = str(vlan_id)
    cmd = 'show vlan id {}'.format(vlan_id)
    try:
        response = eapi_conn.enable(cmd)
        check_vlan = response[0]['result']['vlans']
        return check_vlan[vlan_id]['name']
    except (pyeapi.eapilib.CommandError, KeyError):
        pass

    return False

def configure_vlan(eapi_conn, vlan_id, vlan_name=None):
    cmd = ['vlan {}'.format(vlan_id)]
    if vlan_name:
        cmd.append('name {}'.format(vlan_name))
    return eapi_conn.config(cmd)

def check_if_system_state_would_be_changed(old_vlan_name, new_vlan_name):
    if old_vlan_name:
        # VLAN name needs to be set if new vlan name different from old vlan name
        if new_vlan_name is not None and new_vlan_name != old_vlan_name:
            return True
        else:
            return False

    else:   # Vlan does not exist 
            return True

# ===========================================
def main():
    module = AnsibleModule(
        argument_spec = dict(
            arista_sw=dict(required=True),
            vlan_id=dict(required=True),
            vlan_name=dict(required=False),
        ),
        supports_check_mode=True
    )

    vlan_id = module.params['vlan_id']
    vlan_name = module.params.get('vlan_name')
    arista_sw = module.params.get('arista_sw')

    eapi_conn = pyeapi.connect_to(arista_sw)
    check_vlan = check_vlan_exists(eapi_conn, vlan_id)

    if module.check_mode:
        # Check if any changes would be made but don't actually make those changes
        module.exit_json(changed=
                         check_if_system_state_would_be_changed(check_vlan, vlan_name))

    if check_vlan:
        # VLAN name needs to be set 
        if vlan_name is not None and vlan_name != check_vlan:
            configure_vlan(eapi_conn, vlan_id, vlan_name)
            module.exit_json(msg="VLAN already exists, VLAN name set.", changed=True)
        else:
            module.exit_json(msg="VLAN already exists, no action.", changed=False)

    else:   # Vlan does not exist 
        configure_vlan(eapi_conn, vlan_id, vlan_name)
        module.exit_json(msg="Add VLAN including vlan_name (if present)", changed=True)
            
#----------------------------------------
if __name__ == "__main__":
    main()


