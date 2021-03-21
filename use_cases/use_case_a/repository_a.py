from dagster import repository
from hello_a import hello_a_pipeline


@repository
def use_case_a_repository():
    # Note that we can pass a dict of functions, rather than a list of
    # pipeline definitions. This allows us to construct pipelines lazily,
    # if, e.g., initializing a pipeline involves any heavy compute
    return {
        "pipelines": {
            "hello_a_pipeline": lambda: hello_a_pipeline,
        }
    }
