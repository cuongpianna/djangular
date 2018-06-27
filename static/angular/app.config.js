app.config(function ($stateProvider,$urlRouterProvider,$httpProvider) {
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
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    
})