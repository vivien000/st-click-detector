import { Streamlit, RenderData } from "streamlit-component-lib"
import ResizeObserver from 'resize-observer-polyfill';

// Import Source Sans Pro font
let link = document.createElement('link')
link.rel = 'stylesheet'
link.href = "https://fonts.googleapis.com/css?family=Source+Sans+Pro"
document.head.appendChild(link);

// Transparent pixel so that the iframe's height is properly computed in case of margins
const transparentPixel = "<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='>"

function onRender(event: Event): void {
  const data = (event as CustomEvent<RenderData>).detail

  // Remove existing content
  let child = document.body.lastElementChild;
  if (child) {
    document.body.removeChild(child)
  }

  // Add the HTML content
  let div = document.body.appendChild(document.createElement("div"))
  const resizeObserver = new ResizeObserver((entries: any, observer: any) => {
    Streamlit.setFrameHeight()
  })
  resizeObserver.observe(document.body)
  if (data.theme) {
    div.style.background = data.theme.backgroundColor
    div.style.color = data.theme.textColor
    div.style.fontFamily = data.theme.font
  }
  div.innerHTML = transparentPixel + data.args["html_content"] + transparentPixel

  // Add click detection for each hyperlink
  let links = document.getElementsByTagName("a");
  for (let i = 0; i < links.length; i++) {
    if (links[i].id !== "") {
      links[i].onclick = function (): void {
        Streamlit.setComponentValue(links[i].id)
      }
    }
  }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()