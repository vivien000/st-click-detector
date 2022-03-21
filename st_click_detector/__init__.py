import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "click_detector", url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_click_detector", path=build_dir)


def click_detector(html_content, key=None):
    """Display HTML content and detect when links are clicked on".

    Parameters
    ----------
    html_content: str
        Content to display and from which clicks should be detected
    
    Returns
    -------
    str
        The id of the last link clicked on (or "" before any click)

    """
    component_value = _component_func(html_content=html_content, key=key, default="",)

    return component_value


if not _RELEASE:
    import streamlit as st

    content = """<p><a href='#' id='Link 1'>First link</a></p>
        <p><a href='#' id='Link 2'>Second link</a></p>
        <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
        <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
        """
    clicked = click_detector(content)

    st.markdown(
        f"<p><b>{clicked} clicked</b></p>"
        if clicked != ""
        else "<p><b>No click</b></p>",
        unsafe_allow_html=True,
    )
