from setuptools import setup, find_packages


setup(
    name="prophesee_dataset_toolbox",
    packages=find_packages(exclude=["media", "prophesee_Dataset_toolbox.egg-info", "dataset_visualization.py", "build"]),  # , "metrics", "visualize"],
    #package_dir={
    #    "prophesee_toolbox": "src",
        #"prophesee_toolbox.io": "src/io",
        #"prophesee_toolbox.metrics": "src/metrics",
        #"prophesee_toolbox.visualize": "src/visualize",
    #},
    version="1.0.0",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["numpy", "opencv-python"],
)
