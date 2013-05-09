<script>

                    ;(function(doc){
                        var $ = function(id) { return doc.getElementById(id); };
                        var placeholder = '邮箱/手机号';
                        var email = $('email'), password = $('password'), capcha = $('captcha_field');
                        email.onfocus = function(){
                        if ( this.value == placeholder ) {
                        this.value = '';
                        this.style.color = '#000';
                        }
                    };
                    email.onblur = function(){
                    if (!this.value) {
                        this.value = placeholder;
                        this.style.color = '#ccc';
                        }
                    };

                    if (email.value == placeholder) {
                        email.style.color = '#ccc';
                        } else if(password.value === '') {
                        password.focus();
                        } else if (capcha) {
                        capcha.focus();
                        }

                    })(document);

                    function trim(str){
                        return str.replace(/^(\s|\u00A0)+/,'').replace(/(\s|\u00A0)+$/,'');
                    }

                    function validateForm(frm) {
                        var error = 0,
                        account = frm.elements['email'],
                        passwd = frm.elements['password'],
                        defaultError = document.getElementById('item-error');

                        account_value = trim(account.value);
                        if (defaultError) {
                        defaultError.style.display = 'none';
                        }
                        if (account && account_value === '') {
                        displayError(account, '请输入邮箱');
                        error = 1;
                        } else if (! (/^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(account_value)
                        || /^1[358](\d){9}$/.test(account_value))){
                        displayError(account, '请输入正确的邮箱/手机号');
                        error = 1;
                        } else {
                        account && clearError(account);
                        }
                        
                        if (passwd && passwd.value === '') {
                        displayError(passwd, '请输入密码');
                        error = 1;
                        } else {
                        passwd && clearError(passwd);
                        }
                        return !error;
                        }

                        function displayError(el, msg) {
                            var err = document.getElementById(el.name + '_err');
                            if (!err) {
                            err = document.createElement('span');
                            err.id = el.name + '_err';
                            err.className = 'error-tip';
                            el.parentNode.appendChild(err);
                            }
                            err.style.display = 'inline';
                            err.innerHTML = msg;
                        }

                        function clearError(el) {
                            var err = document.getElementById(el.name + '-err');
                            if (err) {
                            err.style.display = 'none';
                            }
                        }
                
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

