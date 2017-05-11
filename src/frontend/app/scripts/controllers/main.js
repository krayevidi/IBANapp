'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
    .controller('MainCtrl', function ($scope, $auth, Restangular) {
      var refreshTokenResource = Restangular.all('refresh_token');
      var token = $auth.getToken();
      if (token) {
        // force refresh token
        var data = {
          token: token
        };
        refreshTokenResource.post(data).then(
            function (response) {
              $auth.setToken(response.token);
              $scope.user = response;
            }
        )
      }
      $scope.login = function () {
        var data = {
          provider: 'google-oauth2'
        };
        $auth.authenticate('google', data).then(
            function (response) {
              $scope.user = response.data;
            });
      };
      $scope.logout = function () {
        if (confirm('Are you sure you want to logout?')) {
          delete $scope.user;
          $auth.logout();
        }
      }
    });
