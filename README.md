# Docker

Install docker. Not available for arm7, as it still doesn't support
repositories, follow [this link](https://docs.docker.com/engine/installation/linux/docker-ce/debian/#install-using-the-convenience-script)

## Requirements

In your local machine:

```bash
pip install -r requirements.txt
```

## Role Variables

* `install_docker_pip`: (Default: `True`) Set if you want to install the
   `docker` pip package.


## Dependencies

`sudo` and `python` in the target host(s).

## Example Playbook

```yaml
- hosts: servers
  roles:
    - { role: docker }
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/),
**vagrant**, **virtualbox** and some python requirements that can be installed wwith
`pip install -r requirements-dev.txt`.

```bash
molecule test
```

or

```bash
make test
```

There is more documentation about the installation and configuration of the
required tools at
[Testing - Anarres documentation](https://anarres-org.github.io/anarres/testing/).

## License

GPLv3

## Author Information

* drymer: drymer [EN] autistici.org
* lyz: lyz [EN] riseup.net
* m0wer: m0wer (at) autistici (dot) org
