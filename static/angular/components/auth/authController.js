app.controller('authController',['$scope','authService',function ($scope,authService
    ) {
    $scope.msg = 'helloo';
    $scope.user = {};
    $scope.login = function () {
        authService.login($scope.user.username,$scope.user.password);
    }

    $scope.register = function () {
        authService.register($scope.u.email,$scope.u.username,$scope.u.password);
    }

}]);