<script>
    ;(function(doc){
	var $ = function(id) { return doc.getElementById(id); };
	var placeholder = '邮箱/手机号';
	var email = $('email'), password = $('password'), username = $('username'), capcha = $('captcha_field');
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
	} else if(username.value === '') {
	username.focus();
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
        username = frm.elements['username'],
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
	displayError(account, '请输入正确的邮箱');
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

	if (username && username.value === '') {
	displayError(username, '请输入昵称');
	error = 1;
	} else {
	username && clearError(username);
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
</script>
