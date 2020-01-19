# Ansible Roles

CentOS 7 and Debian 8/9/10 install software roles.

## Example Playbook

```yaml
- hosts: all
  remote_user: root
  roles:
    - ansible-role-aria2
```

