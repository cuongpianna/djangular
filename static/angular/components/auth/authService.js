app.service('authService',['$http',function ($http) {
    this.login = function (username,password) {
        var data = {
            username : username,
            password: password
        }
        $http.post('http://127.0.0.1:8000/login',data = data)
            .success(function (res) {
                console.log(res['token']);
                localStorage.setItem('token',res['token']);
                console.log($http.defaults.headers.common.Authorization = 'token ' + res['token']);
            })
            .error(function (data) {
                console.log(data);
            })
    }
}]);