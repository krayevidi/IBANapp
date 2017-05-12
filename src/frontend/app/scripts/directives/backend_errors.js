'use strict';

/**
 * @ngdoc directive
 * @name frontendApp.directive:backendErrors
 * @description
 * # backendErrors
 */
angular.module('frontendApp')
    .directive('backendErrors', function () {
      return {
        templateUrl: 'views/directives/backend_errors.html',
        restrict: 'E',
        require: '^form',
        scope: {
          name: "@"
        },
        link: function postLink(scope, element, attrs, form) {
          scope.field = form[scope.name];
          function watchFn() {
            return scope.field.$viewValue
          }

          function watchCallback(newVal) {
            if (newVal && scope.field.backendErrors) {
              scope.field.$setValidity('backend', true);
              delete scope.field.backendErrors;
            }
          }

          scope.$watchCollection(watchFn, watchCallback);
        }
      };
    });
