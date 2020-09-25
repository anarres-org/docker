# Docker

Install docker. Not available for arm7, as it still doesn't support
repositories, follow [this link](https://docs.docker.com/engine/installation/linux/docker-ce/debian/#install-using-the-convenience-script)

## Requirements

To run this role you must have installed:

* pip

## Role Variables

* `install_docker_pip`: (Default: `True`) Set if you want to install the
   `docker` pip package.


## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - { role: docker }
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/).

And `vagrant` installed with `virtualbox`.

```bash
molecule test
```

## License

GPLv3

## Author Information

* drymer: drymer [EN] autistici.org
* lyz: lyz [EN] riseup.net
* m0wer: m0wer (at) autistici (dot) org
