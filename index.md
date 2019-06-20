---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

<script src="https://d3js.org/d3.v5.min.js"></script>

# Video Clips Showing the Authoring Process

## Mark Instantiation

<div class="video-wrapper">
  <div class="video-item">
    <video src="videos/CreateMark-L.mp4"></video>
    <h4 class="name">Lyra</h4>
    <p>Create a rect by dragging</p>
  </div>
  <div class="video-item">
    <video src="videos/CreateMark-C.mp4"></video>
    <h4 class="name">Charticulator</h4>
    <p>Create a rect by dragging</p>
  </div>
</div>

## Layout Specification

<div class="video-wrapper">
  <div class="video-item">
    <video src="videos/SetupLayout-L.mp4"></video>
    <h4 class="name">Lyra</h4>
    <p>Group by MapX and MapY (see note below), then bind Year to X start</p>
    <p><small>Note: a bug in Lyra prevents the ideal interaction for group layout described in the paper. We demonstrate an alternate workaround instead.</small></p>
  </div>
  <div class="video-item">
    <video src="videos/SetupLayout-C.mp4"></video>
    <h4 class="name">Charticulator</h4>
    <p>Bind MapX and MapY to the X, Y axes of the plot segment, then switch to "Stack X" sublayout</p>
  </div>
</div>

## Data Binding

### Height

<div class="video-wrapper">
  <div class="video-item">
    <video src="videos/HeightMapping-L.mp4"></video>
    <h4 class="name">Lyra</h4>
    <p>Bind PVIScore to height using drop zones; adjust the domain and range of the resulting scale</p>
  </div>
  <div class="video-item">
    <video src="videos/HeightMapping-C.mp4"></video>
    <h4 class="name">Charticulator</h4>
    <p>Bind PVIScore to height using drop zones; scale range is automatically determined</p>
  </div>
</div>

### Color & Scale Editing

<div class="video-wrapper">
  <div class="video-item">
    <video src="videos/ColorMapping-L.mp4"></video>
    <h4 class="name">Lyra</h4>
    <p>Create a "Indication" column with a formula, then bind the Indication column to fill color and adjust the color scale</p>
  </div>
  <div class="video-item">
    <video src="videos/ColorMapping-C.mp4"></video>
    <h4 class="name">Charticulator</h4>
    <p>Bind the <b>pre-computed</b> Indication column to fill color and adjust the color scale</p>
  </div>
</div>

## Adding Labels

<div class="video-wrapper">
  <div class="video-item">
    <video src="videos/CreateText-L.mp4"></video>
    <h4 class="name">Lyra</h4>
    <p>Add a text mark, bind state name to text, and MapY to the Y position</p>
  </div>
  <div class="video-item">
    <video src="videos/CreateText-C.mp4"></video>
    <h4 class="name">Charticulator</h4>
    <p>Add a text mark to the top of the rectangle, bind state name to text, then use conditional visibility to show text for the first year only</p>
  </div>
</div>

<script type="text/javascript">
d3.selectAll("video").each(function() {
  var videoElement = this;
  d3.select(videoElement).on("click", function() {
    if(videoElement.paused) {
      videoElement.play();
    } else {
      videoElement.pause();
    }
  });
  var div = document.createElement("div");
  videoElement.parentNode.insertBefore(div, videoElement.nextSibling);
  d3.select(div).append("button").text("Enlarge").on("click", function() {
    var wrapper = d3.select("body").append("div").attr("class", "popup-video-wrapper");
    var inner = wrapper.append("div").attr("class", "popup-video");
    var popupVideo = inner.append("video")
      .attr("src", videoElement.src)
      .attr("autoplay", true)
      .attr("controls", true);
    inner.on("click", function(e) {
      d3.event.stopPropagation();
    });
    wrapper.on("click", function() {
      wrapper.remove();
      window.removeEventListener("keydown", onEscape);
    });
    var onEscape = function(e) {
      if(e.keyCode == 27) {
        wrapper.remove();
        window.removeEventListener("keydown", onEscape);
      }
    };
    window.addEventListener("keydown", onEscape);
  });
});
</script>
