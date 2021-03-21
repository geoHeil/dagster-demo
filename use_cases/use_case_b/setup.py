from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="use_case_b",
        author="geoHeil",
        author_email="heilerg@csh.ac.at",
        license="Apache-2.0",
        url="https://github.com/geoHeil/dagster-demo/tree/master/use_cases/use_case_b",
        classifiers=[
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
        packages=find_packages(exclude=["test"]),
        install_requires=["dagster"],
        # extras_require={"full": ["seaborn", "scikit-learn"]},
    )
