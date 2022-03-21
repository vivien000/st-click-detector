import setuptools

setuptools.setup(
    name="st-click-detector",
    version="0.1.3",
    author="",
    author_email="",
    description="A Streamlit component to detect clicks",
    long_description="A Streamlit component to display some HTML and detect which <a> tags are clicked",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
