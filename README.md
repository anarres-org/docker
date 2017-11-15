# Docker

Install docker. Not available for arm7, as it still doesn't support
repositories, follow [this link](https://docs.docker.com/engine/installation/linux/docker-ce/debian/#install-using-the-convenience-script)

## Requirements

None.

## Role Variables

None.

## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - { role: docker }
```

## Compatible

With:
  - Debian 9

## License

GPL3

## Author Information

drymer [ EN ] autistici.org
