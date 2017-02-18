/**
 * Created by wdcxc on 2017/2/18.
 */
var csrftoken = Cookies.get('csrftoken');

var loginForm = new Vue({
    el: '#loginForm',
    data: {
        customer: {
            username: '',
            password: '',
            valicode: '',
        }
    },
    methods: {
        login: function () {
            var that = this;
            this.$http.post('/customer/doLogin', that.customer, {"headers":{"X-CSRFToken":csrftoken}})
                .then(response => {
                    if(response.body.code == 200){
                        // todo
                    } else {
                        // todo
                    }
                }, response => {
                    alert(response);
                });
        }
    }
});