# st-click-detector

`st-click-detector` is a [Streamlit](https://streamlit.io) component to display some HTML content and detect when hyperlinks are clicked on.

![Screenshot](screenshot.gif)

A more advanced example can be seen live [here](https://huggingface.co/spaces/vivien/semanticsearch).

## Installation

```bash
pip install st-click-detector
```

## Quickstart

Put your HTML content in a string and make sure that `<a>` tags include an `id` (clicks on links without `id` will be ignored by the component)

```python
import streamlit as st
from st_click_detector import click_detector

content1 = """<p><a href='#' id='Link 1'>First link</a></p>
    <p><a href='#' id='Link 2'>Second link</a></p>
    <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    """
clicked = click_detector(content1)

st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")
```

## Usage

**click_detector(html_content, key=None)**

Display HTML content and detect when links are clicked on

### Parameters

- `html_content` (str): content to display and from which clicks should be detected

- `key` (str or None): an optional key that uniquely identifies this component. If this is None, and the component's arguments are changed, the component will be re-mounted in the Streamlit frontend and lose its current state