var app = angular.module("app", ['ui.router']);
app.controller("HelloController", function($scope) {
  $scope.message = "Hello, AngularJS";
});