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
    .config(function ($authProvider, $routeSegmentProvider, RestangularProvider, API_ROOT, GOOGLE_API_CLIENT_ID) {
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
      $routeSegmentProvider.when('/', 'main')
          .segment('main', {
            templateUrl: 'views/main.html'
          });
    });
