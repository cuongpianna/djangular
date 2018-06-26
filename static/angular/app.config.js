app.config(function ($stateProvider,$urlRouterProvider) {
    $urlRouterProvider.otherwise('')

    $stateProvider
        .state('login',{
        url: '/login',
        controller: 'authController',
        templateUrl: 'static/angular/components/auth/login.html'
    })
        .state('register',{
            url: '/register',
            controller: 'authController',
            templateUrl: 'static/angular/components/auth/register.html'
        })

    
})