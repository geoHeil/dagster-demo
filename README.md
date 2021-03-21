# dagster demo

A first step with dagster to familiarize with the tool

Showcase how multiple teams or use-cases can interoperate in dagster

> NOTICE: this is still work-in-progress (=unfinished)

## prerequisites

```
# create the environment
make create_environment

# activate
conda activate dagster-demo

# set the environment variable
export DAGSTER_HOME=/path/to/dagster-demo/dagster_home
```

## start the pipelines

Get an overview over all the pipelines available

```
dagit
```

## tutorial examples

stuff from the dagster tutorial 

### 1: minimal first

```
# execute
dagster pipeline execute -f pipelines/hello_dagster.py

# using the UI
DAGSTER_HOME=/path/to/dagster_home dagit -f pipelines/hello_dagster.py is also not fixing it. How can I configure a minimal dagster setup correctly? 
dagit -f pipelines/hello_dagster.py
```

### 2: csv second

execute by choosing any combination:

```
dagster pipeline execute -f pipelines/hello_cereal.py
python pipelines/hello_cereal.py
dagit -f pipelines/hello_cereal.py
```

https://docs.dagster.io/tutorial/execute

### 3: improved csv with path from configuration

https://docs.dagster.io/tutorial/basics_solids

```
dagster pipeline execute -f pipelines/inputs.py -c configs/inputs_env.yaml

dagit -f pipelines/inputs.py

# in the playground enter the configuration YAML:
solids:
  read_csv:
    inputs:
      csv_path:
        value: "cereal.csv"
```

### 4: improved config handling

https://docs.dagster.io/tutorial/basics_solids#parametrizing-solids-with-config

```
dagster pipeline execute -f pipelines/config.py -c configs/config_env.yaml
```

### 5 piplines

https://docs.dagster.io/tutorial/basics_pipelines

```
dagit -f pipelines/serial_pipeline.py
dagit -f pipelines/complex_pipeline.py
```