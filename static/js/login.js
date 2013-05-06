<script>
function loadTestImage(action){
  frm = document.getElementById('lzform');
  frm.action=action;

  var loc = window.location;
  var cap = document.getElementById('captcha_image');
  if (cap && loc && loc.protocol === 'https:'){
    var ori_src = cap.src;
    var new_src = ori_src.replace(/http:\/\//, "https://");
    cap.src = new_src;
  }
}

function changeWindowSize() {
  var d = document.documentElement;
  var ch = document.getElementById('header').offsetHeight
          + document.getElementById('content').offsetHeight 
          + document.getElementById('side-nav').offsetHeight; 
  if (d.offsetWidth <= 500 
  || d.offsetHeight <= ch) {
  if (!changeWindowSize.changed) {
      window.resizeTo(500, ch);
      changeWindowSize.changed = true;
  }
  d.className = 'narrow-layout';
  resizeEvent(true);
  } else {
  d.className = '';
  resizeEvent(false);
  } 
}

function resizeEvent(bind) {
  if (!bind) {
    window.onresize = null;
    return;
  }
  window.onresize = (function(){
     var delay;
     return function() {
       if (delay) {
           window.clearTimeout(delay);
       }
       delay = window.setTimeout(changeWindowSize, 100);
    }
  })();
}
</script>

