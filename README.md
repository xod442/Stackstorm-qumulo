# Stackstorm-qumulo
Qumulo stackstorm integration pack

This pack allows you to integrate with
[Qumulo](https://www.hpe.com/us/en/integrated-systems/composable-fabric.html).

## Configuration
Copy the example configuration in [qumulo.yaml.example](./qumulo.yaml.example) to
`/opt/stackstorm/configs/qumulo.yaml` and edit as required.

It must contain:

```
ipaddress - Your qumulo cluster IP address
username - Qumulo Username
password - Qumulo Password
```

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

Example configuration:

```yaml
---
  ipaddress: "10.10.10.10"
  username: "admin"
  password: "admin"
```
You can also run `st2 pack config hpecfm` and answer the promts

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_fs_stats``


### Orquestra Workflows: will not
