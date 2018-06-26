app.controller('authController',['$scope','authService',function ($scope,authService,
    ) {
    $scope.msg = 'helloo';
    $scope.user = {};
    $scope.login = function () {
        authService.login($scope.user.username,$scope.user.password);
    }
}]);