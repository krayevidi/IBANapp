'use strict';

/**
 * @ngdoc overview
 * @name frontendApp
 * @description
 * # frontendApp
 *
 * Main module of the application.
 */
angular
    .module('frontendApp', [
      'constantsApp',
      'ngAnimate',
      'ngAria',
      'ngCookies',
      'ngMessages',
      'ngResource',
      'ngRoute',
      'ngSanitize',
      'ngTouch',
      'satellizer',
      'route-segment',
      'view-segment',
      'restangular'
    ])
    .config(function ($locationProvider, $authProvider, $routeSegmentProvider, RestangularProvider, API_ROOT, GOOGLE_API_CLIENT_ID) {
      // push state settings
      $locationProvider.html5Mode(true);
      // restangular settings
      RestangularProvider.setBaseUrl(API_ROOT);
      RestangularProvider.setRequestSuffix('/');
      // satellizer settings
      $authProvider.tokenType = 'JWT';
      $authProvider.google({
        clientId: GOOGLE_API_CLIENT_ID,
        url: API_ROOT + '/login/social/jwt_user/',
        scope: [
          'email'
        ],
        redirectUri: window.location.origin + '/'
      });
      // routes
      $routeSegmentProvider
          .when('/', 'main')
          .when('/bank_accounts/', 'main.bank_accounts_list')
          .segment('main', {
            templateUrl: 'views/main.html'
          })
          .within()
          .segment('bank_accounts_list', {
            default: true,
            templateUrl: 'views/bank_accounts/list.html'

          })
      ;
    });
