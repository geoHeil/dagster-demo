from dagster import repository
from hello_b import hello_b_pipeline


@repository
def use_case_b_repository():
    # Note that we can pass a dict of functions, rather than a list of
    # pipeline definitions. This allows us to construct pipelines lazily,
    # if, e.g., initializing a pipeline involves any heavy compute
    return {
        "pipelines": {
            "hello_b_pipeline": lambda: hello_b_pipeline,
        }
    }
