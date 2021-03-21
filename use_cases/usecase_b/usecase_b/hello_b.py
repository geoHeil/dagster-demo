from dagster import execute_pipeline, pipeline, solid


@solid
def get_name(_):
    return 'B'


@solid
def hello(context, name: str):
    context.log.info('Hello, {name}! from B'.format(name=name))


@pipeline
def hello_b_pipeline():
    hello(get_name())


if __name__ == "__main__":
    execute_pipeline(hello_b_pipeline)  # Hello, dagster!
